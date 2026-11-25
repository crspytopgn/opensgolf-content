// The residents' association of the example neighbourhood (docs/MODDING.md, sections 6 and 12).
//
// `this` is the pack's own state, saved with the game: the association's level, its experience and its funds.

fn family_names() {
    ["Ashby", "Brook", "Carver", "Dale", "Ellis", "Frost", "Grant", "Hale", "Irwin", "Jordan", "Kemp", "Lowe"]
}

fn level_name(n) {
    let levels = ["Street committee", "Residents' club", "Homeowners' association", "Country club estate"];
    levels[n.min(levels.len() - 1)]
}

fn houses() {
    objects_of("nb-house").len()
}

fn on_start() {
    this.level = 0;
    this.xp = 0;
    this.funds = 0;
    this.dues = 50;
    show_message("A neighbourhood can grow next to your course: build streets and houses from Information > Mods.");
}

fn on_load() {
    // games saved before the pack was switched on start from nothing
    if this.level == () { this.level = 0; this.xp = 0; this.funds = 0; this.dues = 50; }
}

fn on_object_placed(obj) {
    if obj.type != "nb-house" { return; }
    let names = family_names();
    let name = names[random(names.len())];
    set_object_data(obj.uid, #{ family: name, since: year() });
    // a new house looks like the ones of the association's level
    set_object_level(obj.uid, (this.level ?? 0).min(2));
    toast(`The ${name} family moves in.`);
}

fn on_object_removed(obj) {
    if obj.type == "nb-house" && obj.data.family != () {
        show_message(`The ${obj.data.family} family moves away.`);
    }
}

fn on_month() {
    let n = houses();
    if n == 0 { return; }
    let dues = n * this.dues;
    this.funds += dues / 2;
    add_money(dues / 2, "association dues");
    this.xp += n;
    let need = 20 * (this.level + 1);
    if this.xp >= need && this.level < 3 {
        this.xp -= need;
        this.level += 1;
        show_message(`The neighbourhood is now a ${level_name(this.level)}! Its houses grow.`);
        for h in objects_of("nb-house") {
            set_object_level(h.uid, this.level.min(2));
        }
        // the association's hall makes the lots round it dearer as it grows
        for hall in objects_of("nb-hall") {
            for x in (hall.x - 6)..(hall.x + 9) {
                for y in (hall.y - 6)..(hall.y + 9) {
                    set_land_value_bonus(x, y, 10 * this.level);
                }
            }
        }
    }
}

fn on_year_end() {
    if houses() >= 4 && this.funds >= 20000 && this.pool != true {
        ask("pool", `The residents want a pool for the neighbourhood. Pay ${20000} from the association's funds?`, ["Build it", "Not now"]);
    }
}

fn on_answer(question, button) {
    if question == "pool" && button == "Build it" {
        this.funds -= 20000;
        this.pool = true;
        this.xp += 30;
        show_message("The residents' pool opens. The association is proud of it.");
    }
}

fn on_object_clicked(obj) {
    if obj.type == "nb-house" {
        show_panel("house", #{
            title: `The ${obj.data.family ?? "empty"} house`,
            rows: [
                #{ text: `Living here since ${obj.data.since ?? year()}.` },
                #{ text: `A home site here would sell for ${land_value(obj.x, obj.y) * 25}.` },
                #{ bar: obj.level + 1, max: 3, label: "Size" },
            ]
        });
    } else if obj.type == "nb-hall" {
        // a script function called on `this` sees the pack's state
        this.on_panel_open("association");
    }
}

fn on_panel_open(panel) {
    let n = houses();
    show_panel("association", #{
        title: level_name(this.level),
        rows: [
            #{ heading: `${n} houses, dues ${this.dues} a month each` },
            #{ text: `Association funds: ${this.funds}` },
            #{ bar: this.xp, max: 20 * (this.level + 1), label: "To the next level" },
            #{ gap: true },
            #{ button: "party", label: "Hold a street party (2,000)", enabled: this.funds >= 2000 },
            #{ button: "dues_up", label: "Raise the dues" },
            #{ button: "dues_down", label: "Lower the dues", enabled: this.dues > 10 },
        ]
    });
}

fn on_panel_button(panel, button) {
    if panel != "association" { return; }
    switch button {
        "party" => { this.funds -= 2000; this.xp += 10; toast("A good party: the street gets to know each other."); }
        "dues_up" => { this.dues += 10; this.xp = (this.xp - 3).max(0); }
        "dues_down" => { this.dues -= 10; this.xp += 2; }
    }
    this.on_panel_open(panel);
}

fn on_tool(tool, x, y, remove) {
    if tool == "survey" {
        if !owned(x, y) {
            toast("That is not your land.");
        } else {
            toast(`A home site at ${x}, ${y} would sell for about ${land_value(x, y) * 25}.`);
        }
    }
}

fn on_overlay_open(id) {
    if id != "value" { return; }
    let n = map_size();
    let values = [];
    let best = 1;
    for x in 0..n {
        for y in 0..n {
            if owned(x, y) {
                let v = land_value(x, y);
                values.push(v);
                if v > best { best = v; }
            } else {
                values.push(());
            }
        }
    }
    set_overlay("value", values, 0, best, "green sells best");
}
