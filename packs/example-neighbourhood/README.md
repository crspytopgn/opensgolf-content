# Neighbourhood (example of new objects)

An example of what a pack can add to the game beyond art and numbers (docs/MODDING.md, section 12):

* three new objects in `data/objects.toml`: a street that joins up with its neighbours, a house with four facings and
  three sizes, and a residents' association hall (one only, once three holes are open);
* a tool (Survey a lot), a panel (Residents' association) and a map view (Home site values);
* a script, `scripts/neighbourhood.rhai`, that gives every house a family, collects dues, levels the association up (its
  houses grow), raises land values round the hall, shows the panels, and asks the residents' question at a year end.

Switch it on in Preferences > Content, restart, start a game and open Information > Mods.

The art is drawn by `art/make_art.py` (Pillow). Everything here is CC0: copy it and make it your own.
