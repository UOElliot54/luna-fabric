"""Make Luna's eyes read bigger and brighter on the 512x256 coat."""
from PIL import Image
import os

COAT = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\src\main\resources\assets\luna\textures\entity\cat\luna.png"
PREV = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain\preview_luna_eyes.png"
S = 8

img = Image.open(COAT).convert("RGBA")
st = img.load()

IRIS = (212, 224, 98, 255)
RIM = (146, 168, 60, 255)
PUPIL = (30, 28, 24, 255)
GLINT = (244, 250, 214, 255)


def put(cx, cy, col):
    for dy in range(S):
        for dx in range(S):
            st[cx * S + dx, cy * S + dy] = col


# Vanilla eye cells sit on row 6, columns 5,6 and 8,9. Widen them one row up and
# down so the colours read from a distance, then add pupils and a small highlight.
for cols, pupil_col in (((5, 6), 6), ((8, 9), 8)):
    for r in (5, 7):
        for c in cols:
            put(r, c, RIM)
    for c in cols:
        put(6, c, IRIS)
    put(6, pupil_col, PUPIL)
    put(5, cols[0], GLINT)

img.save(COAT)
img.resize((img.width, img.height), Image.NEAREST).save(PREV)
print("coat:", img.size, os.path.getsize(COAT), "bytes")
print("crop:", PREV)
crop = img.crop((0, 8 * 3, 8 * 14, 8 * 11)).resize((8 * 14 * 4, 8 * 8 * 4), Image.NEAREST)
crop.save(r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain\preview_luna_face.png")
print("face:", r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain\preview_luna_face.png")
