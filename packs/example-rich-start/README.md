# Rich Start (example mod)

The simplest mod there is: new games start with **$300,000** instead of $100,000.

## Install

In the game: **System Functions → Preferences → Content packs → Find more…**, pick this pack, click **Download**, switch it
on and restart. Or copy this folder into your `packs` folder yourself (see the main README).

## How it works

`data/economy.toml` has one line, `start_funds = 300000`. Change the number and you have your own mod. Other things you
can change in the same file: `sandbox_funds`, `firing_cost`, `hole_maintenance`, `debt_interest_percent`, the world
map's `offer_prices` and `rank_holes` (how many holes each course rank needs).
