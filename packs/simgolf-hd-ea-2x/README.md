# SimGolf HD 2x (EA art)

The original SimGolf art, AI upscaled 2 times so the game looks sharper on today's screens. The layouts, the sprite cuts and the click areas stay the same, the pictures are just sharper.

## What is in this pack

Sprites from the original game: buildings, trees, scenery, animals, water, bridges, landmarks, homes, flowers and tees, for all four themes, Park, Links, Desert and Tropical. They are packed as sheets, one row per view and one column per frame, as docs/MODDING.md section 11 asks for.

They were upscaled with the same AI upscaler OpenSGolf already uses for HD mode (Real-ESRGAN, built into the game), and saved as WebP at quality 95. That is lossy, not pixel-perfect, but looks the same and is about a tenth of the size of the PNG. Lossless WebP is also read by the game, if zero loss matters more than size.

This pack needs a game build that reads WebP in mod packs. That change is being made separately, and it is not in OpenSGolf 0.9.6 yet. Until it lands, this pack will not load. A PNG form of the same pack can be made with the same maker if needed, see tools/hd_mod_pack/README.md.

Not in this pack yet: the Interface pictures and the Data terrain textures. Those are still missing, see NEEDS-FROM-MAC.md, and they will follow as the pack grows.

Not in this pack: golfers, celebrities and staff, and the body sheets. The game recolours those per person while you play, so they are not upscaled. They are drawn from the classic art, with smooth filtering. Sprite shadows are not in this pack either: the game smooths the classic shadows itself, as its own HD pack does.

Some animations are shorter than the original: 337 sheets were sampled to 12 frames, where the original has 13 to 35 frames. Each of those has a small .json file next to the sheet saying frames: 12, so the game plays the first 12 frames. No frames are invented.

A 2x pack is about 0.6 GB in the game's own HD mode, and it needs less video memory than the 4x pack. As WebP at quality 95 it is much smaller, about a tenth of the PNG size. Use this pack on a small graphics card and in a browser.

## How to install it

You need OpenSGolf and your own copy of SimGolf. This pack does not include the game files.

1. Put this folder in your packs folder. On Linux that is ~/.local/share/opensgolf/packs, on macOS ~/Library/Application Support/OpenSGolf/packs, on Windows %APPDATA%/OpenSGolf/packs, or packs next to the program. In the browser version, use Add a content pack on the start page.
2. Start OpenSGolf, go to System Functions, Preferences, Content packs, and switch SimGolf HD 2x (EA art) on.
3. Start the game again. The pack loads from the next start.

In the game you can also find packs in Preferences, Content packs, Find more.

## How to go back to the originals

Switch the pack off in Preferences, Content packs, and start the game again. Nothing in your SimGolf folder is changed, and the classic art comes back. If you also have an HD pack in your save folder, the order is: this pack first, then the HD pack, then the original art.

## How this pack was made

It was made locally from the player's own copy of SimGolf. The sprites were exported from the original FLC files as PNG sheets, then upscaled with the game's own built-in AI upscaler, in crates/sg-core/src/aiscale.rs through crates/sg-core/src/hdgen.rs, run by the tool in crates/sg-core/examples/hd_upscale_sheets_both.rs. Colours come from the AI model, transparency from the same sheet upscaled with xBRZ, exactly as the game's Make HD graphics does. The sheets were then laid out as a mod pack by tools/hd_mod_pack/assemble_from_exports.py. It does not build a new upscaler.

## Permission

The art belongs to EA. This pack is shared only under the EA permission dated 2026-11-26, which covers distribution of the upscaled EA art pack. See PERMISSION.md. The written form of that permission is not yet filed with this pack. Michael authorised sharing it in opensgolf-content on 2026-11-26, and said the licence is fine.
