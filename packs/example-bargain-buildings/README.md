# Bargain Buildings (example mod)

The Marina, Resort Hotel and Airstrip cost half price, ball washers cost $1,000, and the Snack Bar is called the
**Hot Dog Stand**.

## Install

In the game: **System Functions → Preferences → Content packs → Find more…**, pick this pack, click **Download**, switch it
on and restart. Or copy this folder into your `packs` folder yourself (see the main README).

## How it works

* `data/buildings.toml`: each `[[building]]` names a building by its `id` and gives only what changes (`price`,
  `name`).
* `data/amenities.toml`: the same for paths, benches, flower beds, ball washers and the rest.

Building ids: home-site, putting-green, snack-bar, pro-shop, swim-club, driving-range, cart-garage, marina, resort-hotel,
airstrip, clubhouse. Amenity ids: pathway, benches, flower-bed, ball-washer, landmark, willow-tree, tv-tower, tv-booth,
scenic-bridge. Prices are in multiples of 100.
