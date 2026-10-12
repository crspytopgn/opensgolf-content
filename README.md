# ⛳ OpenSGolf content

Mods, scenarios and translations for [OpenSGolf](https://github.com/crspytopgn/simgolf-native), the free game that plays
like Sid Meier's SimGolf.

## Playing with mods

In the game: **System Functions → Preferences → Content packs → Find more…**, pick a pack and click **Download**. Switch it
on in the Content packs list, then restart the game. That's all.

## Adding your own pack

1. Make your pack (see [MODDING.md](https://github.com/crspytopgn/simgolf-native/blob/main/docs/MODDING.md)) and try it in
   the game from your packs folder.
2. Put its folder in `packs/` here. The folder name must be the pack's `id` from its `pack.toml`.
3. Open a pull request. A check runs automatically and tells you if anything needs fixing.
4. Once it's merged, the list rebuilds itself and your pack appears in every player's **Find more…** list.

To update a pack, change its files and raise `version` in `pack.toml`; players see it as an update.

## Rules

* **A free licence** in `pack.toml` (`license`), for example `CC0-1.0`, `CC-BY-4.0`, `CC-BY-SA-4.0` or `GPL-2.0-or-later`.
* **Nothing from the original game**: no art, sounds, music or files from SimGolf, not even edited or upscaled.
* **Your own work**, or work whose licence lets you share it (credit it in your pack's README).
* Keep it friendly: no hateful or adult content.

## How it works

`index.json` is the list the game reads, and `dist/` holds each pack as a `.zip`. Both are made by
`tools/build_index.py` from the folders in `packs/` (a GitHub Action runs it on every merge), so never edit them by hand.
The format is described in the game's
[docs/CONTENT_INDEX.md](https://github.com/crspytopgn/simgolf-native/blob/main/docs/CONTENT_INDEX.md).
