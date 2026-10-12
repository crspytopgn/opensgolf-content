# Staff Pay Rise (example mod)

Every employee earns more, so money is tighter: a harder game for players who know SimGolf well.

| Employee | Built in | With this mod |
|----------|----------|---------------|
| Club Pro | 300 / 700 | 500 / 1,000 |
| Ranger | 200 / 300 | 300 / 500 |
| Groundskeeper | 200 / 400 | 300 / 600 |
| Soda Vendor | 200 / 500 | 300 / 700 |

(new hire / experienced, per week as the hire panel shows it)

## Install

In the game: **System Functions → Preferences → Content packs → Find more…**, pick this pack, click **Download**, switch it
on and restart. Or copy this folder into your `packs` folder yourself (see the main README).

## How it works

`data/staff.toml` names each employee kind by its `id` (club-pro, ranger, groundskeeper, soda-vendor) and gives its
`wage` and `wage_experienced`, in multiples of 100. You can also give a kind a new `name`.
