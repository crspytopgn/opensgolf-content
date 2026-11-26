# Publish blockers: read this before any GitHub publish

Do not push, do not open a pull request, and do not upload the EA art anywhere until Michael says so.

## 1. No EA files yet, except the sprites

The sprite exports are on the VM, see NEEDS-FROM-MAC.md, and the sprite part of the pack is being built from them. The full pack still needs the Interface pictures and the Data textures, which are not here yet. The pack template and the maker are ready, the upscaled EA pictures and textures are not.

## 2. Written EA permission not yet filed

Permission note, in PERMISSION.md:
- Source: EA
- Date: 2026-11-26
- Covers: distribution of the upscaled EA art pack

The written form of that permission is not yet filed with the pack. File it here before the pack is shared, with who gave it, when, and what it covers, in writing.

## 3. Pack size over the Find more limit

docs/CONTENT_INDEX.md and crates/sg-core/src/index.rs set a 256 MB limit for a pack zip downloaded through Find more, MAX_PACK_SIZE = 256 MB.

Measured 2026-11-26, sprite part only: the 4x pack is 170.7 MB as WebP at quality 95 (779.8 MB as PNG), zip 167.4 MB. The 2x pack is 62.5 MB as WebP (233.8 MB as PNG), zip 62.1 MB. Both sprite-only zips are under the limit. WebP is about 22 percent of the PNG size at 4x and 27 percent at 2x, not a tenth.

The Interface pictures (137) and Data textures (about 2,653) are not in these packs yet, and they will add size. The complete pack is not yet proven under the limit, so do not promise it until those are built and measured.

WebP in mod packs: Michael is doing that game change himself, on Claude, 2026-11-26. This copy does NOT change the game to read WebP in mod packs. An earlier attempt here was reverted in full (crates/sg-core/src/vfs.rs, hires.rs and png.rs, crates/sgtool/src/kit.rs, docs/HD.md and docs/MODDING.md are back to main), so the two copies do not clash. This copy only builds the pack itself, with .webp files at quality 95, ready to use once his change lands. If his change is not in yet, a PNG form of the pack can be made with the same maker (--format png).

Note for his change: the current pack-check (sgtool, back to main) only checks PNG files under gfx/. A .webp sheet is skipped without being checked, and each .json next to a .webp sheet warns that there is no .png sheet for it. So the WebP pack itself cannot be fully checked until his change teaches pack-check about .webp too. Until then, check the PNG form of the pack (same maker, --format png), then convert the checked PNGs to WebP at quality 95. The sizes are the same either way, so the check still proves the layouts.

Note for his change: the reverted attempt here found that sgtool's test kit::tests::a_bad_pack_is_explained checks the exact pack-check messages, and it failed while the messages said PNG or WebP. Whoever lands the WebP change needs to update that test's expected messages too.

Options if the WebP pack is still over the limit, to decide with Michael before publishing:
- Split the pack by theme, for example Park, Links, Desert and Tropical as separate packs, each under 256 MB, or
- Ship the pack outside Find more, as a direct download, with the index entry pointing elsewhere, if the rules allow it.

Do not pick one of these without asking Michael first.

## 4. Licence field is not a free licence

docs/CONTENT_INDEX.md says an index entry needs a free licence, for example CC0-1.0, CC-BY-4.0, CC-BY-SA-4.0 or GPL-2.0-or-later. The opensgolf-content README says the same, and that a mod must never contain SimGolf's own files, not even edited or upscaled ones.

This pack uses license = "LicenseRef-EA-Permission-2026-11-26" in pack.toml, because the art belongs to EA and is shared only under the EA permission above. That is not a free licence, and the index checker may refuse it. Ask Michael, and check with the opensgolf-content rules, how this pack should be listed, before opening a pull request there.

## 5. Compatibility, checked

- OpenSGolf 0.9.6, mod API 2, pack.toml api = 2, kind = mod, see crates/sg-core/src/packs.rs MOD_API = 2
- Pack format follows docs/MODDING.md section 11: scale 2 or 4, gfx/ pictures at the path of the original, exact scale times the original's size, sprites as sheets. The pack ships WebP at quality 95, as docs/HD.md does for HD packs, so it needs the WebP game change above before it loads as a mod pack. A PNG form is the fallback until then.
- Sprite part only, for now: 704 sheets (normal, animated and base sprites). People are not in the pack, the game recolours them while you play. Shadow sheets are not in the pack, the game smooths the classic shadows itself, as its own HD pack does. Interface pictures and Data textures are not in the pack yet, they are still missing, see NEEDS-FROM-MAC.md.
- 337 sheets are sampled to 12 frames, where the original has 13 to 35 frames. Each of those has a .json file next to the sheet saying frames: 12, so the game plays the first 12 frames. No frames are invented.
- Load order, file by file: enabled mod pack file first, then HD pack upscale, then original art. Switching the pack off in Preferences, Content, and starting the game again brings back the originals. Nothing in the SimGolf folder is changed.
- The pack was checked with sgtool pack-check on a placeholder game folder: 1099 files, 0 errors, 0 warnings. That check has not yet been run on the real EA pack.
