from PIL import Image
import os

TABBY = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain\cat_tex\tabby.png"
OUT = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain\tabby-map.txt"

im = Image.open(TABBY).convert("RGBA")
w, h = im.size
px = im.load()

codes = {}
order = []
for y in range(h):
    for x in range(w):
        c = px[x, y]
        if c not in codes:
            codes[c] = len(order)
            order.append(c)

n = len(order)
print("size:", w, "x", h, " unique colors:", n)

DIGITS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"


def label(i):
    if n <= 36:
        return DIGITS[i]
    return DIGITS[i // 36] + DIGITS[i % 36]


legend = []
for i, c in enumerate(order):
    legend.append("%s = rgba%s (%d px)" % (label(i), c, sum(1 for y in range(h) for x in range(w) if px[x, y] == c)))

lines = ["legend (%s colors)" % n] + legend + ["", "grid %dx%d, %d chars per cell" % (w, h, 1 if n <= 36 else 2)]
for y in range(h):
    row = []
    for x in range(w):
        row.append(label(codes[px[x, y]]))
    lines.append("".join(row))

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("wrote", OUT)
