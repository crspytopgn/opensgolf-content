# Hole-in-One Bonus (example script)

A small example of an OpenSGolf game script, made for OpenSGolf (CC0-1.0: do what you like with it). When a golfer makes a
hole-in-one on your course, a sponsor pays you $500, $1,000 or $1,500 and a message says so.

## Install

Copy this folder (or a .zip of it) into a `packs` folder (docs/MODDING.md, section 1), start the game, switch the pack on
in **System Functions > Preferences > Content packs...** and restart the game.

## What is in it

* `pack.toml`: a `mod` like any other.
* `scripts/bonus.rhai`: the script, in [Rhai](https://rhai.rs). It defines three hooks (`on_start`,
  `on_hole_finished`, `on_year_end`) and keeps its count of aces in `this`, the pack's state, which is saved with the game.
  docs/MODDING.md, section 6, lists every hook and function.

A script that goes wrong never stops the game: the error is shown on the Content packs screen and in the terminal.
