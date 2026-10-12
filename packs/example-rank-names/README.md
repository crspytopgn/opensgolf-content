# New Rank Names (example mod)

Changes the names of the four course ranks: Municipal becomes **Village Links**, Daily Fee **Town Course**, Country Club
**Private Club** and Championship **Major Venue**.

## Install

In the game: **System Functions → Preferences → Content packs → Find more…**, pick this pack, click **Download**, switch it
on and restart. Or copy this folder into your `packs` folder yourself (see the main README).

## How it works

`lang/en.txt` holds lines of `KEY :text`. Every piece of text the game shows has a key; the full list is the game's
[lang/en.txt](https://github.com/crspytopgn/opensgolf/blob/main/lang/en.txt). A pack only lists the keys it changes.
To translate the game into another language, make a pack with `kind = "translation"` and a `lang/<code>.txt`, for
example `lang/fr.txt` (see docs/TRANSLATING.md).
