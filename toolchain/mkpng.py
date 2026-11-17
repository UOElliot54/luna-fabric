"""Generate PNG assets for the Chamomile Tea trial mod (PIL-based)."""
import os
from PIL import Image, ImageDraw

TEX = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\chamomile-tea\src\main\resources\assets\chamomile-tea\textures\item\chamomile_tea.png"
ICON = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\chamomile-tea\src\main\resources\assets\chamomile-tea\icon.png"

TRANSPARENT = (0, 0, 0, 0)
RIM = (236, 236, 230, 255)
BODY = (222, 222, 214, 255)
SHADE = (198, 198, 190, 255)
TEA = (214, 158, 66, 255)
TEA_HI = (240, 196, 110, 255)
PETAL = (252, 220, 110, 255)
WHITE = (255, 255, 255, 255)
STEAM = (214, 214, 214, 120)
SAUCER = (206, 206, 200, 255)

S = 16
img = Image.new("RGBA", (S, S), TRANSPARENT)
px = img.load()

# steam wisps
for y, xs in ((0, (5, 9)), (1, (6, 10)), (2, (5, 9)), (3, (6, 10))):
    for x in xs:
        px[x, y] = STEAM

# rim + tea surface
for x in range(3, 12):
    px[x, 4] = RIM
for x in range(4, 11):
    px[x, 5] = TEA_HI
    px[x, 6] = TEA
px[6, 5] = PETAL
px[7, 5] = WHITE
px[8, 6] = WHITE
px[9, 5] = PETAL

# cup body with a left shadow edge and a small handle on the right
for y in range(7, 13):
    for x in range(3, 12):
        px[x, y] = BODY
    px[3, y] = SHADE
for y in (8, 11):
    px[12, y] = BODY
for y in (9, 10):
    px[13, y] = SHADE

# saucer
for x in range(1, 15):
    px[x, 13] = SAUCER
for x in range(2, 14):
    px[x, 14] = SHADE

os.makedirs(os.path.dirname(TEX), exist_ok=True)
img.save(TEX)

# ---- icon: warm tile, cup scaled up, a few chamomile flowers ----
T = 128
icon = Image.new("RGBA", (T, T), (248, 238, 216, 255))
d = ImageDraw.Draw(icon)
d.rounded_rectangle([4, 4, T - 5, T - 5], radius=18, fill=(255, 250, 235, 255))
d.rounded_rectangle([10, 10, T - 11, T - 11], radius=14, outline=(231, 213, 175, 255), width=3)

cup = img.resize((104, 104), Image.NEAREST)
icon.alpha_composite(cup, (12, 12))

for cx, cy in ((24, 22), (104, 26), (22, 104), (102, 100)):
    for ang in range(0, 360, 60):
        pass
    d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=WHITE)
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=PETAL)

icon.save(ICON)
print("texture saved:", TEX, "icon saved:", ICON)
