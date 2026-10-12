// Hole-in-one bonus: an example game script (docs/MODDING.md, section 6).
//
// The game calls the hooks below. Inside a hook `this` is this pack's own state: a map that is saved with the game.

// A new game starts.
fn on_start() {
    this.aces = 0;
    show_message("The club's sponsor pays a bonus for every hole-in-one on your course!");
}

// A golfer has finished a hole: `golfer` is a map (name, hole, strokes, member, pro).
fn on_hole_finished(golfer, hole, strokes) {
    if strokes != 1 {
        return;
    }
    this.aces = (this.aces ?? 0) + 1;
    // a little luck in the amount: 500, 1000 or 1500 (random() is the script's own generator, saved with the game)
    let bonus = 500 * (1 + random(3));
    add_money(bonus, "hole-in-one bonus");
    show_message(`${golfer.name} made a hole-in-one on hole ${hole}! The sponsor pays a bonus of $${bonus}.`);
}

// The end of each year: a word about the year's aces.
fn on_year_end() {
    let n = this.aces ?? 0;
    if n > 0 {
        print(`hole-in-one bonus: ${n} aces so far`);
    }
}
