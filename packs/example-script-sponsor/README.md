# Local Sponsor (example script)

Every month a local business pays **$200 for each open hole** on your course, and a message says so.

## Install

In the game: **System Functions → Preferences → Content packs → Find more…**, pick this pack, click **Download**, switch it
on and restart. Or copy this folder into your `packs` folder yourself (see the main README).

## How it works

`scripts/sponsor.rhai` is a [Rhai](https://rhai.rs) script with one hook, `on_month()`, which the game calls at the
start of every month. It reads `hole_count()`, pays with `add_money` and shows a message with `show_message`. Try
changing the 200, or pay only once the course has a high `fun_rating()`. Every hook and function is listed in
[docs/MODDING.md, section 6](https://github.com/crspytopgn/opensgolf/blob/main/docs/MODDING.md).
