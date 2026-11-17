"""Paint Luna's coat from the vanilla tabby UV layout, plus her spawn-egg icon."""
from PIL import Image, ImageDraw
import os

TABBY = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain\cat_tex\tabby.png"
RES = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\src\main\resources\assets\luna"

# ---- 1) cat coat: recolour the vanilla tabby 64x32 sheet, alpha preserved ----
# Luna (from the photos): brown-silver tabby Maine Coon -- dark agouti stripes over
# warm grey-brown fur, tan ruff, pale silver chest/muzzle, chartreuse eyes, pink nose.
LUNA = {
    (94, 66, 45):    (56, 51, 47),    # darkest fur -> near-black agouti
    (83, 60, 40):    (66, 60, 54),    # dark brown -> dark grey-brown
    (116, 86, 62):   (104, 92, 80),   # mid brown -> warm grey-brown
    (135, 101, 74):  (132, 116, 100), # light brown -> silvered tan
    (149, 114, 86):  (156, 128, 100), # warm highlight -> Maine Coon ruff tan
    (209, 183, 161): (198, 180, 162), # inner ear / muzzle
    (230, 181, 148): (204, 178, 152),
    (222, 169, 132): (188, 164, 142),
    (243, 233, 219): (232, 226, 213), # whiskers + chest cream
    (233, 217, 194): (212, 203, 187), # pale chest / belly
    (241, 218, 60):  (196, 208, 90),  # eye -> chartreuse green
    (187, 137, 16):  (150, 172, 64),  # eye shade -> green
    (190, 115, 115): (199, 139, 143), # nose -> pink
}

src = Image.open(TABBY).convert("RGBA")
out = Image.new("RGBA", src.size, (0, 0, 0, 0))
sp, dp = src.load(), out.load()
seen = set()
for y in range(src.size[1]):
    for x in range(src.size[0]):
        r, g, b, a = sp[x, y]
        if a == 0:
            dp[x, y] = (0, 0, 0, 0)
            continue
        base = (r, g, b)
        mapped = LUNA.get(base, base)
        dp[x, y] = (mapped[0], mapped[1], mapped[2], a)
        seen.add(base)
missing = sorted(seen - set(LUNA))
print("opaque colours not in map:", missing)

cat_dir = os.path.join(RES, "textures", "entity", "cat")
os.makedirs(cat_dir, exist_ok=True)
out.save(os.path.join(cat_dir, "luna.png"))
print("cat coat:", out.size, os.path.getsize(os.path.join(cat_dir, "luna.png")), "bytes")

# ---- 2) spawn egg item texture, 16x16 ----
CREAM = (214, 204, 188, 255)
MID = (150, 128, 100, 255)
SHADE = (104, 92, 80, 255)
DARK = (56, 51, 47, 255)
EYE = (170, 190, 80, 255)

egg = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
d = ImageDraw.Draw(egg)
for yy in range(16):
    for xx in range(16):
        # egg silhouette: narrower at the top
        half = 1.6 + 4.6 * (yy - 2.2) / 11.0 if yy < 4 else 5.4 - 0.16 * max(0, yy - 13)
        cx = 7.5
        if abs(xx + 0.5 - cx) <= half and 2 <= yy <= 14:
            d.point((xx, yy), CREAM)
for xx in range(16):
    for yy in range(16):
        if egg.getpixel((xx, yy))[3] == 0:
            continue
        # left edge shading + bottom shading
        if xx <= 3 and yy > 4:
            egg.putpixel((xx, yy), SHADE)
        elif yy >= 13:
            egg.putpixel((xx, yy), SHADE)
for (sx, sy) in [(5, 6), (9, 5), (7, 8), (10, 9), (4, 10), (11, 7), (6, 12), (9, 12), (5, 8)]:
    d.point((sx, sy), DARK)
    d.point((sx + 1, sy), MID)
    d.point((sx, sy + 1), MID)
d.point((6, 7), EYE)
d.point((10, 7), EYE)
egg_path = os.path.join(RES, "textures", "item", "luna_spawn_egg.png")
os.makedirs(os.path.dirname(egg_path), exist_ok=True)
egg.save(egg_path)
print("egg texture:", egg.size, os.path.getsize(egg_path), "bytes")

# ---- 3) mod icon 128x128 (egg scaled, on a soft tabby roundel) ----
BG = (74, 64, 56, 255)
BG2 = (96, 84, 74, 255)
icon = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
dd = ImageDraw.Draw(icon)
dd.ellipse((8, 8, 120, 120), fill=BG2, outline=BG, width=4)
dd.ellipse((20, 20, 108, 108), fill=BG)
scaled = egg.resize((16 * 6, 16 * 6), Image.NEAREST)
icon.paste(scaled, (34, 26), scaled)
icon_path = os.path.join(RES, "icon.png")
icon.save(icon_path)
print("icon:", icon.size, os.path.getsize(icon_path), "bytes")
