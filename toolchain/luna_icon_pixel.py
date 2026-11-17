"""Draw a pixel-art icon of Luna (head and ruff) from her coat palette."""
from PIL import Image
import os

ICON = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\src\main\resources\assets\luna\icon.png"
PREV = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain\preview_icon_pixel.png"
B = 64          # base pixel grid; icon is saved upscaled
S = 4           # upscale factor for the shipped icon (256x256)

FUR_M = (132, 116, 100, 255)
FUR_D = (104, 92, 80, 255)
FUR_L = (156, 128, 100, 255)
FUR_XD = (66, 60, 54, 255)
FUR_XD2 = (56, 51, 47, 255)
CREAM = (232, 226, 213, 255)
CREAM2 = (212, 203, 187, 255)
EAR_IN = (224, 178, 160, 255)
EYE = (212, 224, 98, 255)
EYE_D = (150, 172, 64, 255)
PUP = (30, 28, 24, 255)
GLINT = (244, 250, 214, 255)
NOSE = (199, 139, 143, 255)
NOSE_D = (170, 120, 124, 255)
WHISK = (246, 240, 226, 255)

G = [[(0, 0, 0, 0)] * B for _ in range(B)]


def box(x0, y0, x1, y1, col):
    for y in range(max(0, y0), min(B, y1 + 1)):
        for x in range(max(0, x0), min(B, x1 + 1)):
            G[y][x] = col


def band(x0, y0, x1, y1):
    for y in range(y0, y1 + 1):
        c = (FUR_D if (y - y0) % 4 < 2 else FUR_M) if (y - y0) % 8 < 4 else FUR_L
        box(x0, y, x1, y, c)


# head, ears and ruff, banded like her agouti coat
box(12, 16, 52, 50, FUR_M)
band(12, 16, 52, 50)
box(12, 8, 22, 17, FUR_D)
box(42, 8, 52, 17, FUR_D)
box(15, 10, 19, 15, EAR_IN)
box(45, 10, 49, 15, EAR_IN)
box(22, 16, 24, 27, FUR_XD)        # tabby M on the forehead
box(30, 16, 34, 27, FUR_XD2)
box(38, 16, 40, 27, FUR_XD)
for y in range(18, 49):            # fluffy edge on both cheeks
    box(11, y, 11, y, FUR_L)
    box(53, y, 53, y, FUR_L)
box(10, 26, 10, 40, CREAM2)
box(54, 26, 54, 40, CREAM2)

# eyes: chartreuse with dark pupils and a highlight
box(16, 26, 24, 33, EYE)
box(40, 26, 48, 33, EYE)
box(16, 32, 24, 33, EYE_D)
box(40, 32, 48, 33, EYE_D)
box(19, 27, 22, 31, PUP)
box(42, 27, 45, 31, PUP)
box(16, 26, 17, 27, GLINT)
box(40, 26, 41, 27, GLINT)

# muzzle, pink nose and a small mouth
box(24, 36, 40, 47, CREAM)
box(26, 44, 38, 47, CREAM2)
box(29, 36, 35, 39, NOSE)
box(29, 39, 35, 39, NOSE_D)
box(31, 39, 33, 43, NOSE_D)
box(27, 43, 29, 43, NOSE_D)
box(35, 43, 37, 43, NOSE_D)

# whiskers stick out past the face
box(4, 38, 23, 38, WHISK)
box(4, 42, 23, 42, WHISK)
box(7, 46, 23, 46, WHISK)
box(41, 38, 60, 38, WHISK)
box(41, 42, 60, 42, WHISK)
box(41, 46, 57, 46, WHISK)

# mane ruff under the chin
box(8, 48, 56, 58, FUR_L)
band(8, 48, 56, 58)
box(6, 50, 7, 57, CREAM)
box(57, 50, 58, 57, CREAM)
box(8, 58, 56, 58, CREAM2)

img = Image.new("RGBA", (B, B), (0, 0, 0, 0))
st = img.load()
for y in range(B):
    for x in range(B):
        st[x, y] = G[y][x]

img = img.resize((B * S, B * S), Image.NEAREST)
img.save(ICON)
img.resize((512, 512), Image.NEAREST).save(PREV)
print("icon:", img.size, os.path.getsize(ICON), "bytes")
print("preview:", PREV)
