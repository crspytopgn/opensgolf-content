# ⛳ OpenSGolf mods

Mods, scenarios and translations for [OpenSGolf](https://github.com/crspytopgn/opensgolf), the free game that plays
Sid Meier's SimGolf. **If you own SimGolf, these work on top of your own copy**: you keep the original look and sound,
and a mod changes the game. They also work with the free graphics.

## Playing with mods

In the game: **System Functions → Preferences → Content packs → Find more…**, pick a pack and click **Download**. Switch it
on in the Content packs list, then restart the game. That's all.

## Make your own mod: it's easy

A mod is a folder with a `pack.toml` (its name and version) and one or more small text files. No programming needed
for most mods. Start by copying one of the examples below, change a number, and try it.

| Example | What it shows | Files |
|---------|---------------|-------|
| [Rich Start](packs/example-rich-start) | the simplest mod: start with $300,000 | `data/economy.toml` (one line) |
| [Cheap Fairways](packs/example-cheap-fairways) | change what course tiles cost | `data/terrain.toml` |
| [Bargain Buildings](packs/example-bargain-buildings) | change building prices and names | `data/buildings.toml`, `data/amenities.toml` |
| [Staff Pay Rise](packs/example-staff-wages) | change employees' wages | `data/staff.toml` |
| [New Rank Names](packs/example-rank-names) | change any text in the game | `lang/en.txt` |
| [Local Sponsor](packs/example-script-sponsor) | a 10-line script: money every month | `scripts/sponsor.rhai` |
| [Hole-in-One Bonus](packs/example-script-bonus) | a script that reacts to golfers | `scripts/bonus.rhai` |
| [Hawaii Resort](packs/example-scenario-hawaii) | a scenario with goals | `scenario.toml` |
| [Desert Challenge](packs/example-scenario-desert-challenge) | a harder scenario | `scenario.toml` |

To try your mod, put its folder in your `packs` folder (next to the program, or `packs` in your save folder; in the
browser version use "Add a content pack" on the start page), switch it on in **Content packs** and restart.

What a mod can change: money rules, prices, buildings, staff, the sixteen properties, any text, scenarios and goals, and
game rules through scripts. To see every value the game uses, run `sgtool dump-data somefolder`; the full guide is
[MODDING.md](https://github.com/crspytopgn/opensgolf/blob/main/docs/MODDING.md).

**One rule above all:** a mod must never contain SimGolf's own files (its pictures, sounds, music, videos or data), not
even edited or upscaled ones. Your mod changes the game; each player brings their own copy of SimGolf. New art or sound
that you made yourself is welcome.

## Sharing your mod

1. Put its folder in `packs/` here. The folder name must be the pack's `id` from its `pack.toml`.
2. Open a pull request. A check runs automatically and tells you if anything needs fixing.
3. Once it's merged, your pack appears in every player's **Find more…** list.

To update a pack, change its files and raise `version` in `pack.toml`; players see it as an update.

Rules:

* **A free licence** in `pack.toml` (`license`), for example `CC0-1.0`, `CC-BY-4.0`, `CC-BY-SA-4.0` or `GPL-2.0-or-later`.
* **Nothing from the original game** (see above).
* **Your own work**, or work whose licence lets you share it (credit it in your pack's README).
* Keep it friendly: no hateful or adult content.

## How it works

`index.json` is the list the game reads, and `dist/` holds each pack as a `.zip`. Both are made by
`tools/build_index.py` from the folders in `packs/` (a GitHub Action runs it on every merge), so never edit them by hand.
The format is described in the game's
[docs/CONTENT_INDEX.md](https://github.com/crspytopgn/opensgolf/blob/main/docs/CONTENT_INDEX.md).
