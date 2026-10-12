// Local sponsor: an example game script (docs/MODDING.md, section 6).
// Every month a local business pays $200 for each open hole on the course.

fn on_month() {
    let n = hole_count();
    if n == 0 {
        return;
    }
    let pay = 200 * n;
    add_money(pay, "local sponsor");
    show_message(`A local business sponsors your ${n} holes this month: $${pay}.`);
}
