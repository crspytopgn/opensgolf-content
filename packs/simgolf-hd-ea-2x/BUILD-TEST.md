# Build and test record: SimGolf HD (EA art) mod pack

Date: 2026-11-26
Repo: crspytopgn/opensgolf, main 41dd4a6, OpenSGolf 0.9.6, mod API 2
Branch: feature/ai-hd-pack, local only, no push, no PR

## What was tested, and what was not

Tested on a placeholder game folder made by sgtool fixture, in /tmp/fixture-game. That folder has placeholder art, not EA art, and not the free art. It is 22 MB, 1140 files. The tests prove the pipeline works, they do not prove the EA pictures look right.

Not tested: the real EA art, all themes and buildings at full size, the in-game load of the EA pack, and a live play test. Those need Michael's full SimGolf folder, see NEEDS-FROM-MAC.md.

## Test 1: full 2x pack, Lanczos, fixture

Command:
python3 tools/hd_pack/hd_pack.py --game /tmp/fixture-game --out /tmp/hdpack-test --scale 2 --method lanczos
python3 tools/hd_mod_pack/make_hd_mod.py --game /tmp/fixture-game --hd-pack /tmp/hdpack-test --out /tmp/hd-mod-test --scale 2

Result:
- HD pack: 1222 pictures upscaled 2x, 17 MB, 10 seconds, method lanczos
- Mod pack: 10 images, 1040 textures, 49 sprites at 2x, 13.8 MB of gfx files, 1099 files in total, nothing skipped
- The fixture has only 10 PCX pictures outside Flics, so the image count is low. The real game has about 160 pictures, see docs/HD.md.
- A bug was found and fixed in make_hd_mod.py: sprite sheets were first written to a gfx folder in the repo root, not to the pack folder. Fixed, the stray folder was removed, and the test was run again.

## Test 2: pack-check, 2x fixture pack

Command:
./target/release/sgtool pack-check /tmp/hd-mod-test --game /tmp/fixture-game

Result: 1099 files checked, 0 errors, 0 warnings, the pack looks good.

## Test 3: country club, 4x, fixture

Command:
python3 tools/hd_pack/hd_pack.py --game /tmp/fixture-game --out /tmp/hdpack-4x-club --scale 4 --method lanczos --only "club"
python3 tools/hd_mod_pack/make_hd_mod.py --game /tmp/fixture-game --hd-pack /tmp/hdpack-4x-club --out /tmp/hd-mod-4x-club --scale 4 --only "club"

Result:
- HD pack: 32 pictures upscaled 4x, 276 KB, 1 second
- Mod pack: 8 sprites at 4x, 0.2 MB, for example gfx/flics/bldgs/park/clubl2.png at 480x1600, and gfx/flics/bldgs/desert/desclubl1base.png at 640x1280
- Pack-check: 8 files checked, 0 errors, 0 warnings, the pack looks good

These are placeholder club pictures, not EA art. They show the sheet sizes are exact 4x, and the pack-check passes.

## Test 4: build

Command: cargo build -p sgtool --release
Result: finished in 3 minutes 47 seconds, sgtool 0.9.6. No cargo check of the full game was run, as no code in the game was changed, only new pack and tool files were added.

## Sizes to expect for the real EA pack

From docs/HD.md and tools/hd_pack/README.md, not measured here:
- About 25,000 pictures in a full pack
- About 1.2 GB at 4x, about 0.6 GB at 2x, in the game's own HD mode
- About 10 minutes on an 8-core laptop, 25 minutes on a 4-core one, with the built-in AI upscaler
- In this test, Lanczos was used, not AI, because there is no Real-ESRGAN binary or GPU on this VM. The real pack must use Real-ESRGAN, either the built-in one in crates/sg-core/src/aiscale.rs, or realesrgan-ncnn-vulkan with tools/hd_pack.

## Test previews, not pack files

The country club test previews in ~/workspace/opensgolf-test-images/ were made with Muse's image tool, not with the game's upscaler. They are 912x2736 and 864x2880, about 5.15x, RGB with no transparency, not exact 4x. They are not in this pack, and they must not be used as pack files. Michael approved the look of those previews on 2026-11-26, which is why the full pack work went ahead.

## Test 5: sgtool unit tests

Command: cargo test -p sgtool --release
Result: 5 passed, 0 failed, including pack-check tests for a good pack and a bad pack.

## Test 6: WebP game change stopped and reverted, 2026-11-26

Michael is doing the change to read WebP in mod packs himself, on Claude. This copy stopped that work and reverted it in full with git checkout: crates/sg-core/src/vfs.rs, hires.rs and png.rs, crates/sgtool/src/kit.rs, docs/HD.md and docs/MODDING.md are back to main 41dd4a6. Nothing in the game code is changed in this copy any more. The pack itself is still built as WebP at quality 95, ready for his change, and a PNG form is the fallback.

What the reverted attempt found, for whoever lands the change: sgtool's test kit::tests::a_bad_pack_is_explained checks the exact pack-check messages. While the messages said PNG or WebP, that test failed (4 passed, 1 failed). After the revert it passes again (5 passed, 0 failed). The WebP change needs to update that test's expected messages too.

Note on the post-revert sg-core tests: a cargo test -p sg-core --release --lib run was started after the revert to confirm the reverted code, but it was stopped part way through (2026-11-26) to give the shared CPU to the AI upscale run, which is the long job. The revert itself is a byte-exact git checkout of main's files, and sgtool's tests pass on the reverted code (5 passed, 0 failed, Test 5 above), so the revert is sound. Re-run the sg-core tests on a quiet machine if a clean record is wanted.

## Test 7: sprite exports checked against the layout list, 2026-11-26

Source: game-src/, 1,894 PNG exports from Flics/*.flc, checked against crates/sg-core/src/freeset/manifest.txt (1,893 sprite entries).

- 1,311 sheets go in the pack, and every non-people sprite entry has one. Nothing missing, nothing extra.
- 974 sheets are the full animation, 337 are sampled to 12 frames only, where the original has 13 to 35 frames. Those get a .json file saying frames: 12.
- 582 exports are people (Male 204, Female 232, Celebs 84, Employee 62). Not in the pack, the game recolours them while you play.
- 607 sheets are shadows (black, alpha as the strength). Not in the pack, the game smooths the classic shadows itself, as its own HD pack does. That saves 101.4 million pixels of AI work, 44 percent of the total.
- The pack's sprite part is 704 sheets, 131.2 million source pixels. Shadow PNGs checked: pure black, alpha 0 to 160. Normal sprites: alpha 0 or 255 only.
- One odd case: ScenicElm and its shadow have views 0 and 52 frames in the layout list. The export is one row of 12 frames. It is treated like the other 12-frame sheets, with frames: 12.

## Test 8: the AI upscaler on this VM, 2026-11-26

Tool: crates/sg-core/examples/hd_upscale_sheets.rs, which runs the game's own built-in AI upscaler (sg_core::hdgen::upscale_ai, the Real-ESRGAN model in crates/sg-core/src/aiscale.rs). Colours come from the AI model, transparency from the xBRZ upscale of the same sheet, exactly as Make HD graphics does.

Measured on this VM (shared CPU, no graphics card):
- clubL1, 177x528: 10.0 seconds at 4x. clubL2, 204x640: 15.1 seconds at 4x.
- The model alone runs at about 8,000 source pixels a second, about 9 to 10 GMAC/s. A 46-file sample of 25.55 million pixels ran at about 23,900 pixels a second, because the upscaler skips fully transparent areas.
- Full non-shadow run, 131.2 million pixels, is about 1.5 hours at that rate, for both scales together, see below.
- A second tool, crates/sg-core/examples/hd_upscale_sheets_both.rs, runs the AI model once per sheet and writes both the 2x and the 4x pictures. Its outputs are byte-identical to running the single-scale tool twice (checked with SHA-256 on clubL1 and clubL2, both scales). That halves the work.
- Making the 2x pack by plainly shrinking the 4x pictures does NOT match: on clubL1 and clubL2 the biggest difference per colour was 248 out of 255, average 37 to 60. The game's 2x pictures average the AI colours only, while a plain shrink also mixes in the transparent pixels' fill colours. So the 2x pack needs its own upscale run, which the both-scales tool does in the same pass.

## Test 9: mini pack from real EA sprites, 2026-11-26

16 real EA sprite sheets upscaled at 4x with the AI upscaler, assembled with tools/hd_mod_pack/assemble_from_exports.py into /tmp/mini-pack, PNG form.

Result: 16 sheets, 6 frames json files, 0 problems, 13.1 MB. Pack-check with no game folder: 22 files checked, 0 errors, 0 warnings, the pack looks good.

Pack-check with --game /tmp/fixture-game gave 1 error, and that error is the fixture's fault, not the pack's: the fixture's placeholder FLC for TROPmarL1 is 120x100, while EA's original is 136x118, and pack-check trusts the game folder first when it has the file. For the EA pack, run pack-check with no --game folder (it then checks against the layout list), or with the real game folder when it is available. Never check the EA pack against the fixture folder.

## Test 10: WebP size measured on the mini pack, 2026-11-26

The 16-sheet mini pack from Test 9, PNG form 13.1 MB, converted to WebP at quality 95 with Pillow: 3.09 MB, 23.5 percent of the PNG. Every WebP file reads back at the same size as its PNG.

That is not a tenth, as docs/HD.md says for HD packs. Sprite sheets with hard edges and AI detail compress less well than pictures. The full sprite pack will be measured when it is assembled, but plan on about a quarter of the PNG size, not a tenth. Even so, a 4x sprite pack of roughly 580 MB in PNG should come to roughly 140 MB as WebP, under the 256 MB Find more limit. The 2x pack will be smaller still.

## Note: runtime restart during the AI run, 2026-11-26

The VM runtime restarted while the full AI upscale was running, and /tmp was wiped: the fixture game folder, the sample outputs and the analysis file in /tmp were all lost. The upscaled sheets survived because they were on the home disk, in ~/workspace/ai-out2 and ai-out4 (70 sheets done at the restart). One file, ai-out2/Bldgs/Desert/DesHotelL1.png, was cut off mid-write by the kill and was deleted after a Pillow check found it unreadable; its sheet is redone by the driver. The run was restarted with all paths on the home disk (input ~/workspace/ai-in, outputs ~/workspace/ai-out2 and ai-out4), so a restart no longer loses the work. The analysis was rebuilt from game-src and the layout list and saved at ~/workspace/export-analysis.json, with the same numbers as before. Lesson: keep every intermediate on the home disk, never in /tmp, for a run this long.

## Test 11: full sprite pack built and pack-checked, 2026-11-26

The full AI upscale ran on this VM with crates/sg-core/examples/hd_upscale_sheets_both.rs: 704 sheets, 131.2 million source pixels, both scales from one run of the model each. It took about 2 hours of wall time in total, across a runtime restart that was recovered from by resuming (the driver skips sheets already written). Final run: 634 sheets upscaled, 70 already there, 107.6 million pixels in 3,533 seconds, about 30,000 pixels a second on average. The upscaled PNGs are in ~/workspace/ai-out2 (269 MB) and ~/workspace/ai-out4 (1,017 MB).

Assembly with tools/hd_mod_pack/assemble_from_exports.py, WebP at quality 95:
- 4x pack, packs/simgolf-hd-ea: 703 sheets, 191 frames json files, 170.7 MB of WebP. Zip of the pack folder: 167.4 MB.
- 2x pack, packs/simgolf-hd-ea-2x: 704 sheets, 192 frames json files, 62.5 MB of WebP. Zip of the pack folder: 62.1 MB.
- Both zips are under the 256 MB Find more limit, for the sprite part of the pack. The Interface pictures and Data textures are not in these packs yet, and they will add size, so the complete pack is not yet proven under the limit. See PUBLISH-BLOCKERS.md.
- WebP is about 22 percent of the PNG size at 4x (170.7 of 779.8 MB) and about 27 percent at 2x (62.5 of 233.8 MB), not a tenth as docs/HD.md says for HD packs. Sprite sheets compress less well than pictures.

Pack-check (sgtool, no game folder, so it checks against the layout list):
- 4x PNG form: 894 files checked, 0 errors, 0 warnings, the pack looks good.
- 2x PNG form: 896 files checked, 0 errors, 0 warnings, the pack looks good.
- The WebP packs themselves were checked file by file with Pillow: every .webp opens, is RGBA, and is the same size as its checked PNG; every .json is valid, says frames: 12, and has its sheet next to it. 4x: 703 webp, 191 json, 0 bad. 2x: 704 webp, 192 json, 0 bad.
- The game's own decoder was spot-checked on three WebP files with crates/sg-core/examples/webp_check.rs: clubL1 at 4x, CastleL2_ANIM at 2x, TreeMapleLarge at 4x. All three decode, the size matches, the alpha is exactly the same (mean and max difference 0), and the colours differ by 2 to 5 out of 255 on average, which is what lossy quality 95 does.

CastleL2_ANIM is not in the 4x pack: at 4x its sheet is 17,664 pixels wide, and the game's PNG decoder in crates/sg-core/src/png.rs refuses pictures over 16,384 pixels wide. It falls back to the classic art for that one building. It is in the 2x pack, where it is 8,832 pixels wide. The maker skips it at 4x only, in tools/hd_mod_pack/assemble_from_exports.py (SKIP_AT_4X), and the skip is listed in BUILD-REPORT.json.

Not tested: loading either pack in the game. The WebP packs need Michael's game change to read WebP in mod packs before they load at all, and no live play test has been run. The PNG forms are the fallback if his change is not in yet.
