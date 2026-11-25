"""Draws the example neighbourhood pack's sprite sheets (CC0). Run from this folder: python3 make_art.py (needs Pillow).

Each sheet is views x frames: houses 4 views (the facings) x 3 frames (the levels), the hall 1 x 1, the road 1 x 16 (one
frame for each set of neighbours: 1 north, 2 east, 4 south, 8 west). A tile's edge is about 45 pixels on the screen, so a
tile's diamond is 64 x 32.
"""
from PIL import Image, ImageDraw

TW, TH = 64, 32


def diamond(cx, cy, w, h):
    return [(cx, cy - h / 2), (cx + w / 2, cy), (cx, cy + h / 2), (cx - w / 2, cy)]


def shade(c, k):
    return tuple(max(0, min(255, int(v * k))) for v in c) + (255,)


def box(d, cx, base, w, h, height, wall, roof, door_side, level):
    """A house on a footprint diamond w x h (pixels) centred at (cx, base): walls, a pitched roof and windows."""
    top = base - height
    left = [(cx - w / 2, base), (cx, base + h / 2), (cx, top + h / 2), (cx - w / 2, top)]
    right = [(cx, base + h / 2), (cx + w / 2, base), (cx + w / 2, top), (cx, top + h / 2)]
    d.polygon(left, fill=shade(wall, 0.78), outline=shade(wall, 0.45))
    d.polygon(right, fill=shade(wall, 1.0), outline=shade(wall, 0.45))
    # windows: one row a level
    for row in range(level + 1):
        wy = top + 10 + row * 14
        for k in (0.3, 0.7):
            for side, sx in ((-1, cx - w / 2), (1, cx)):
                x0 = sx + k * w / 2
                y0 = wy + (k * h / 2 if side < 0 else (1 - k) * h / 2)
                d.rectangle([x0 - 3, y0, x0 + 3, y0 + 7], fill=(250, 240, 170, 255), outline=(60, 50, 40, 255))
    # the door on one face
    if door_side in (0, 1):
        dx = cx - w / 4 if door_side == 0 else cx + w / 4
        dy = base + h / 4
        d.rectangle([dx - 4, dy - 14, dx + 4, dy], fill=(110, 60, 30, 255), outline=(40, 20, 10, 255))
    # the roof
    peak = top - 22 - 4 * level
    ridge_l, ridge_r = (cx - w / 4, peak + h / 4 - 6), (cx + w / 4, peak - h / 4 + 6)
    d.polygon([(cx - w / 2 - 3, top), (cx, top + h / 2 + 3), ridge_r, ridge_l], fill=shade(roof, 0.8), outline=shade(roof, 0.5))
    d.polygon([(cx, top + h / 2 + 3), (cx + w / 2 + 3, top), ridge_r], fill=shade(roof, 1.0), outline=shade(roof, 0.5))
    d.polygon([(cx - w / 2 - 3, top), ridge_l, (cx, top - h / 2 - 3), ridge_r], fill=shade(roof, 1.15), outline=shade(roof, 0.5))


def houses():
    fw, fh = 140, 130
    walls = [(230, 220, 200), (200, 220, 235), (240, 210, 190)]
    roofs = [(160, 70, 50), (70, 90, 140), (60, 120, 70)]
    img = Image.new("RGBA", (fw * 3, fh * 4), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for view in range(4):
        for level in range(3):
            # the footprint's middle (the anchor in objects.toml) is (70, 96) in each frame
            cx, base = level * fw + fw / 2, view * fh + fh - TH - 2
            d.polygon(diamond(cx, base, 2 * TW, 2 * TH), fill=(120, 170, 90, 255), outline=(70, 110, 50, 255))
            box(d, cx, base, 2 * TW - 36, 2 * TH - 18, 30 + 14 * level, walls[level], roofs[level], view % 2, level)
    img.save("house.png")
    return fw, fh


def hall():
    fw, fh = 210, 190
    img = Image.new("RGBA", (fw, fh), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # the footprint's middle (the anchor in objects.toml) is (105, 138)
    cx, base = fw / 2, fh - 3 * TH / 2 - 4
    d.polygon(diamond(cx, base, 3 * TW, 3 * TH), fill=(150, 150, 140, 255), outline=(90, 90, 80, 255))
    box(d, cx, base, 3 * TW - 50, 3 * TH - 25, 52, (235, 235, 225), (120, 40, 40), 1, 1)
    # a flagpole
    d.line([(cx + 70, base - 10), (cx + 70, base - 110)], fill=(80, 80, 80, 255), width=2)
    d.polygon([(cx + 71, base - 110), (cx + 95, base - 102), (cx + 71, base - 94)], fill=(40, 90, 180, 255))
    img.save("hall.png")


def road():
    img = Image.new("RGBA", (TW * 16, TH), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # edge middles on the screen: north (y - 1) up right, east (x + 1) down right, south down left, west up left
    ends = {1: (TW * 3 / 4, TH / 4), 2: (TW * 3 / 4, TH * 3 / 4), 4: (TW / 4, TH * 3 / 4), 8: (TW / 4, TH / 4)}
    for bits in range(16):
        ox = bits * TW
        d.polygon([(ox + x, y) for x, y in diamond(TW / 2, TH / 2, TW - 2, TH - 2)], fill=(85, 85, 90, 255), outline=(60, 60, 64, 255))
        for b, (ex, ey) in ends.items():
            if bits & b:
                d.line([(ox + TW / 2, TH / 2), (ox + ex, ey)], fill=(240, 220, 90, 255), width=2)
        if bits == 0:
            d.ellipse([ox + TW / 2 - 3, TH / 2 - 2, ox + TW / 2 + 3, TH / 2 + 2], fill=(240, 220, 90, 255))
    img.save("road.png")


if __name__ == "__main__":
    houses()
    hall()
    road()
