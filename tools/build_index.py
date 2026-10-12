#!/usr/bin/env python3
"""Builds the OpenSGolf content index from the pack folders.

Every folder in packs/ with a pack.toml becomes dist/<id>-<version>.zip (zipped the same way every time, so its checksum
only changes when its files do) and an entry in index.json, the list the game's "Find more..." reads
(docs/CONTENT_INDEX.md in the OpenSGolf repository). `--check` only validates and fails on any problem (used for pull
requests).
"""
import hashlib
import json
import os
import re
import sys
import tomllib
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKS, DIST = os.path.join(ROOT, "packs"), os.path.join(ROOT, "dist")
# free licences only (SPDX identifiers)
LICENCES = {"CC0-1.0", "CC-BY-4.0", "CC-BY-SA-4.0", "GPL-2.0-or-later", "GPL-3.0-or-later", "MIT", "Apache-2.0",
            "OFL-1.1", "Unlicense", "CC-BY-3.0", "CC-BY-SA-3.0", "LGPL-2.1-or-later", "BSD-3-Clause", "MPL-2.0"}
KINDS = {"mod", "translation", "scenario", "base"}
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{1,63}$")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
# the original game's file types: a pack must not carry the original's files
SUSPECT = (".pcx", ".flc", ".bik", ".dta", ".chr", ".glf", ".pro", ".exe", ".dll")
MAX_ZIP = 50 * 1024 * 1024


def deterministic_zip(folder, out):
    files = []
    for root, dirs, names in os.walk(folder):
        dirs.sort()
        for n in sorted(names):
            files.append(os.path.join(root, n))
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            rel = os.path.relpath(f, os.path.dirname(folder)).replace(os.sep, "/")
            info = zipfile.ZipInfo(rel, date_time=(2001, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            with open(f, "rb") as fh:
                z.writestr(info, fh.read())


def main():
    check_only = "--check" in sys.argv
    problems, entries, seen = [], [], set()
    os.makedirs(DIST, exist_ok=True)
    for name in sorted(os.listdir(PACKS)):
        folder = os.path.join(PACKS, name)
        if not os.path.isdir(folder):
            continue
        where = f"packs/{name}"
        try:
            with open(os.path.join(folder, "pack.toml"), "rb") as fh:
                pack = tomllib.load(fh)["pack"]
        except (OSError, KeyError, tomllib.TOMLDecodeError) as e:
            problems.append(f"{where}: no readable [pack] in pack.toml ({e})")
            continue
        pid, version, kind = pack.get("id", ""), pack.get("version", ""), pack.get("kind", "")
        licence = pack.get("license", pack.get("licence", ""))
        for ok, msg in [
            (pid == name, f"the folder name must be the pack id ({pid!r})"),
            (ID_RE.match(pid), "id: lower case letters, digits and dashes"),
            (VERSION_RE.match(version), "version: like 1.0.0"),
            (kind in KINDS, f"kind: one of {sorted(KINDS)}"),
            (licence in LICENCES, f"license: a free licence, one of {sorted(LICENCES)}"),
            (pack.get("name"), "name: missing"),
            (pid not in seen, "id listed twice"),
        ]:
            if not ok:
                problems.append(f"{where}: {msg}")
        seen.add(pid)
        for root, _, names in os.walk(folder):
            for n in names:
                if n.lower().endswith(SUSPECT):
                    problems.append(f"{where}: {n}: files of the original game's types are not allowed")
        zpath = os.path.join(DIST, f"{pid}-{version}.zip")
        deterministic_zip(folder, zpath)
        data = open(zpath, "rb").read()
        if len(data) > MAX_ZIP:
            problems.append(f"{where}: the zip is over {MAX_ZIP // 1024 // 1024} MB")
        entry = {
            "id": pid, "name": pack.get("name", ""), "version": version, "kind": kind, "licence": licence,
            "authors": pack.get("authors", []), "description": pack.get("description", ""),
            "url": f"dist/{pid}-{version}.zip", "sha256": hashlib.sha256(data).hexdigest(), "size": len(data),
            "requires": pack.get("requires", []),
        }
        entries.append(entry)
    # zips of packs no longer listed are removed
    keep = {os.path.basename(e["url"]) for e in entries}
    for f in os.listdir(DIST):
        if f.endswith(".zip") and f not in keep:
            os.remove(os.path.join(DIST, f))
    for p in problems:
        print("problem:", p)
    if problems:
        sys.exit(1)
    if not check_only:
        with open(os.path.join(ROOT, "index.json"), "w") as fh:
            json.dump({"format": 1, "packs": entries}, fh, indent=2)
            fh.write("\n")
    print(f"{len(entries)} packs ok")


if __name__ == "__main__":
    main()
