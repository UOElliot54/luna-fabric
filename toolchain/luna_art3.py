"""Regenerate Luna's coat at 8x (512x256) with painted fur, fluff edges, bright eyes and whiskers."""
from PIL import Image
import os, re

MAP = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain\tabby-map.txt"
RES = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\src\main\resources\assets\luna"
PREV = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain\preview_luna_cat_v3.png"
S = 8

LUNA = {
    (94, 66, 45): (56, 51, 47), (83, 60, 40): (66, 60, 54), (116, 86, 62): (104, 92, 80),
    (135, 101, 74): (132, 116, 100), (149, 114, 86): (156, 128, 100), (209, 183, 161): (198, 180, 162),
    (230, 181, 148): (204, 178, 152), (222, 169, 132): (188, 164, 142), (243, 233, 219): (232, 226, 213),
    (233, 217, 194): (212, 203, 187), (241, 218, 60): (196, 208, 90), (187, 137, 16): (150, 172, 64),
    (190, 115, 115): (199, 139, 143),
}

legend, grid, mode = {}, [], "L"
for line in open(MAP, encoding="utf-8"):
    line = line.rstrip("\n")
    if line.startswith("grid"):
        mode = "G"
        continue
    if mode == "L":
        m = re.match(r"\s*(.) = rgba\((\d+), (\d+), (\d+), (\d+)\)", line)
        if m:
            legend[m.group(1)] = tuple(int(v) for v in m.groups()[1:])
    elif len(line) >= 64 and all(c in legend for c in line[:64]):
        grid.append(line[:64])

H, W = len(grid), len(grid[0])
FUR, CREAM, EYE, NOSE = set("1237ck"), set("89a"), set("gh"), set("r")


def kind(ch):
    if ch in EYE:
        return "e"
    if ch in NOSE:
        return "n"
    if ch in CREAM:
        return "c"
    if ch in FUR:
        return "f"
    return "."


K = [[kind(grid[y][x]) for x in range(W)] for y in range(H)]
BW, BH = W * S, H * S
C = [[(0, 0, 0, 0)] * BW for _ in range(BH)]
for y in range(BH):
    for x in range(BW):
        k = K[y // S][x // S]
        if k == ".":
            continue
        r, g, b, a = legend[grid[y // S][x // S]]
        t = LUNA.get((r, g, b), (r, g, b))
        C[y][x] = (t[0], t[1], t[2], a)


def sh(c, mul, add=0):
    return (max(0, min(255, int(c[0] * mul + add))), max(0, min(255, int(c[1] * mul + add))),
            max(0, min(255, int(c[2] * mul + add))), c[3])


NB = ((1, 0), (-1, 0), (0, 1), (0, -1))


def nb(y, x):
    return [(y + d[0], x + d[1]) for d in NB if 0 <= y + d[0] < BH and 0 <= x + d[1] < BW]


for y in range(BH):
    for x in range(BW):
        if K[y // S][x // S] == "f":
            st = 0.90 if x % 12 < 2 else (0.95 if x % 12 in (5, 6) else 1.0)
            C[y][x] = sh(C[y][x], st, (((x * 131 + y * 17) % 11) - 5) * 1.6)

for y in range(BH):
    for x in range(BW):
        k = K[y // S][x // S]
        if k in (".", "e", "n"):
            continue
        if any((K[b[0] // S][b[1] // S] not in (".", k)) for b in nb(y, x)):
            C[y][x] = sh(C[y][x], 0.72)

for y in range(BH):
    for x in range(BW):
        k = K[y // S][x // S]
        if k in ("f", "c") and any(K[b[0] // S][b[1] // S] == "." for b in nb(y, x)):
            jag = ((x + y * 3) % 16) < 8
            C[y][x] = sh(C[y][x], 1.22 if jag else 0.86, 14 if jag else -6)

for y in range(BH):
    for x in range(BW):
        if K[y // S][x // S] != "e":
            continue
        C[y][x] = sh(C[y][x], 1.06, 18)
        if (y < S or K[(y - 1) // S][x // S] == ".") and (x < S or K[y // S][(x - 1) // S] == "."):
            C[y][x] = sh(C[y][x], 1.15, 40)
        for b in nb(y, x):
            if K[b[0] // S][b[1] // S] not in (".", "e"):
                C[b[0]][b[1]] = sh(C[b[0]][b[1]], 0.82)

EYE_C = (196, 208, 90)
nxy = [(y, x) for y in range(H) for x in range(W) if grid[y][x] == "r"]
if nxy:
    nx = sum(p[1] for p in nxy) / len(nxy) * S + S / 2
    ny = sum(p[0] for p in nxy) / len(nxy) * S + S / 2
    WH = (246, 240, 226, 255)
    for side in (-1, 1):
        for ang in (-0.16, 0.02, 0.2):
            for t in range(9, 46):
                x = int(nx + side * t)
                y = int(ny + ang * t + (side * t) * 0.012)
                if not (0 <= x < BW and 0 <= y < BH):
                    continue
                if K[y // S][x // S] in (".", "e"):
                    continue
                C[y][x] = WH
                if y + 1 < BH and K[(y + 1) // S][(x + 1) % BW // S] not in (".", "e"):
                    C[y + 1][x] = sh(WH, 0.72)

img = Image.new("RGBA", (BW, BH), (0, 0, 0, 0))
st = img.load()
for y in range(BH):
    for x in range(BW):
        st[x, y] = C[y][x]

cat = os.path.join(RES, "textures", "entity", "cat")
os.makedirs(cat, exist_ok=True)
img.save(os.path.join(cat, "luna.png"))
print("coat:", img.size, os.path.getsize(os.path.join(cat, "luna.png")), "bytes")
img.resize((BW, BH), Image.NEAREST).save(PREV)
print("preview:", PREV)
