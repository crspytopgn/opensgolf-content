# Cheap Fairways (example mod)

A small example of an OpenSGolf content pack: it makes fairways cost 100 a tile instead of 300, and firm fairways 200
instead of 300. It is made for OpenSGolf and contains nothing from the original game (CC0-1.0: do what you like with it).

## Install

Copy this folder (or a .zip of it) into a `packs` folder:

* next to the program, or
* in your save folder: `~/.local/share/simgolf/packs` (Linux), `~/Library/Application Support/SimGolf/packs` (macOS),
  `%APPDATA%\SimGolf\packs` (Windows); in the browser version, use "Add a content pack" on the start page.

Then start the game, open **System Functions > Preferences > Content packs...**, switch the pack on and restart the game.
The Build Course panel then shows "Fairway 100".

## What is in it

* `pack.toml`: who made the pack, its version and licence, what it needs (`original >= 1.0`, the built-in base set).
* `data/terrain.toml`: the two entries it changes. Each entry names a tile type by its `id` and gives only the fields that
  change; see docs/MODDING.md for every field, or run `sgtool dump-data DIR` for the full built-in tables.
