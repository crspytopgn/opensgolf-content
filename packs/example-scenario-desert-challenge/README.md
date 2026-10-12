# Desert Challenge (example scenario)

A small example of an OpenSGolf scenario pack, made for OpenSGolf (CC0-1.0: do what you like with it). It works with any
base set (your own copy of SimGolf or the free OpenSGolf graphics) and needs nothing else.

You start near Phoenix with $60,000 at the Moderate difficulty and three goals:

* open 9 holes by the end of 2002,
* reach a fun rating of 30,
* have $150,000 in cash by the end of 2004.

## Play it

Copy this folder (or a .zip of it) into a `packs` folder (see docs/MODDING.md, section 1). Then choose **Start New Game**
on the title screen: with a scenario pack installed it lists *Free game* and the scenarios. Click *Desert Challenge* twice
(or pick it and press Enter, or click the tick).
The goals are in **Information > Scenario Goals**; a message tells you when one is reached or missed.

## What is in it

* `pack.toml`: `kind = "scenario"`.
* `scenario.toml`: the property, money, difficulty, the texts and the goals. See docs/MODDING.md, section 5, for every
  field. A scenario can also start from a saved course (`course = "course.sgs"`): the Save dialog's *Export as
  scenario pack* button (System Functions > Save the current game, then the button or Tab) writes such a pack from the game
  you are playing.
