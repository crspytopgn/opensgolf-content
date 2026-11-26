# What is still needed from Michael's Mac

Status, 2026-11-26: the sprite exports are here, the rest is not. The full EA art pack cannot be finished until the folders below arrive. Do not invent EA art, and do not fetch it from the web.

## The real game folder

The real game folder on Michael's Mac is:

    /Volumes/nvme.fanxiang/Claude/simgolf/game/Program_Files_(ENGLISH)/

That folder holds Flics, Interface, Data, Heads, Bodies, Themes and Sounds. The earlier path /Volumes/nvme.fanxiang/Claude/simgolf/game/ is the CD layout, not the game folder itself.

## What the VM already has: the sprite exports

Pulled 2026-11-26 and unzipped to ~/workspace/opensgolf-upscale/game-src/, 1,894 PNG files, 51 MB, from three zips:

- sprites_buildings.zip, 17.9 MB
- sprites_people.zip, 12.1 MB
- sprites_scenery.zip, 17.7 MB

These are PNG exports from Flics/*.flc, one PNG per sprite, a row per camera view and a column per animation frame, with _base, _ANIM and _shadow variants. Backgrounds are transparent.

Checked against the layout list in crates/sg-core/src/freeset/manifest.txt (1,893 sprite entries):

- 1,311 sprite sheets that go in the pack, every non-people sprite entry has one, and every non-people export matches an entry. Nothing is missing, nothing is extra.
- 974 sheets are the full animation, 337 are sampled to 12 frames only, where the original has 13 to 35 frames. Those 337 get a small .json file next to the sheet saying frames: 12, so the game plays the first 12 frames. No frames are invented.
- 582 exports are people (Male 204, Female 232, Celebs 84, Employee 62). They are not in the pack: the game recolours people while you play, so they are drawn from the classic art, as the game's own HD pack does.
- 607 of the 1,311 sheets are shadow sheets (black, with the alpha as the shadow strength). They are not in the pack either: the game's own HD pack leaves shadows out, and the game smooths the classic shadows itself. That also saves about 101 million pixels of AI work, 44 percent of the total.

So the sprite part of the pack is 704 sheets: normal, animated and base sprites, at 131.2 million source pixels.

## What is still missing

These folders are not in the three sprite zips. They are needed for a complete pack, with pictures and terrain textures as well as sprites. Counted on the Mac 2026-11-26:

- Interface/**/*.pcx, 137 pictures, including Interface/infoscreens/*.pcx. Send the whole Interface folder.
- Data/Textures/**/*, about 2,653 files, mostly small 64x64 .bmp terrain textures, in theme folders Desert, Links, Parkland and others, plus files at the top of Data/Textures. Send the whole Data/Textures folder.
- Data/*.pcx, 5 theme pictures: desert.pcx, desert tiles.pcx, links.pcx, parkland.pcx, tropical.pcx, plus Data/WaterShallow*.bmp, 20 files.
- 9 *.pcx files in the root of the game folder: bink64.pcx, BLDG.PCX, cliffs01.pcx, course1.pcx, creditsbckgrd.pcx, GBUBBLES.pcx, Jackal.pcx, logo.pcx, Radiobut.pcx.
- Heads/*.pcx, for the record, even though a high resolution mod pack cannot replace Heads or Bodies, see docs/MODDING.md section 11.

The easiest way to send them is the same as the sprites were sent: zip each folder on the Mac and upload the zip. Pulling them one file at a time is not practical: Data/Textures alone has about 2,653 files, and the Mac link only sends one file per call.

## How the sprite pack is made from the exports

The maker does not need the original FLC files any more. The exports are already sheets, so the layout (views, frames, frame size) is read from the layout list, not from an FLC. The upscaler is the game's own built-in AI upscaler, crates/sg-core/src/aiscale.rs through crates/sg-core/src/hdgen.rs, run by the tool in crates/sg-core/examples/hd_upscale_sheets.rs. Colours come from the AI model, transparency from the same sheet upscaled with xBRZ, exactly as the game's Make HD graphics does.

The finished sprite sheets are saved as WebP at quality 95, about a tenth of the size of the PNG. The game needs Michael's WebP change before it can read WebP in a mod pack, see PUBLISH-BLOCKERS.md. A PNG form of the pack can be made with the same tool if his change is not in yet.

## Two ways to get the pack made

1. Send the folders above to Muse, and Muse runs the maker here, then reports back.
2. Or run the maker on the Mac, in the repo copy there. For sprites from the exports, the tool is crates/sg-core/examples/hd_upscale_sheets.rs, then tools/hd_mod_pack/make_hd_mod.py lays out the mod pack. For pictures and textures from the game folder itself, the maker is tools/hd_pack/hd_pack.py, which checks for Flics and Interface.

Either way, the finished pack is large in PNG form, about 1.2 GB at 4x and about 0.6 GB at 2x in the game's own HD mode, before zipping. As WebP at quality 95 it should be about a tenth of that, see PUBLISH-BLOCKERS.md.

## What NOT to send as pack files

The two test PNGs already sent are not pack files, and they are not used in this pack:

- /Volumes/nvme.fanxiang/Claude/simgolf/game/sprites_export/sprites_buildings/Bldgs/Park/clubL1.png, 177x528
- /Volumes/nvme.fanxiang/Claude/simgolf/game/sprites_export/sprites_buildings/Bldgs/Park/clubL2.png, 204x640

Those are PNG exports from Flics/*.flc, one PNG per sprite, 4 camera views stacked. The 4x previews made from them with Muse's image tool are about 5.15x, not exact 4x, and they lost transparency, RGB not RGBA. The real pack must use the game's own upscaler, with proper transparency, exact 2x and 4x sizes, and a manifest. The preview files live in ~/workspace/opensgolf-test-images/, and they stay there as previews only.

## What the VM already has

- The repo at main 41dd4a6, OpenSGolf 0.9.6, mod API 2, branch feature/ai-hd-pack
- The maker in tools/hd_mod_pack, tested on a placeholder game folder, see BUILD-TEST.md
- The pack template in packs/simgolf-hd-ea and packs/simgolf-hd-ea-2x, with pack.toml, README, PERMISSION and LICENSE, and an empty gfx folder
- The sprite exports in game-src/, 1,894 PNG files, 51 MB, checked against the layout list
- No Interface pictures, no Data textures, no root PCX files yet
