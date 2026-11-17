"""Build Luna's item icon from the reference photo (head-on shot)."""
from PIL import Image
import os

PHOTO = r"C:\Users\ElliotPC\.strata\data\agent\home\attachments\v1\objects\a2\a245c83b6aeb55f611bc59147800ce99fee084d33a252aae0dd6e9b3e2284fe0"
OUT = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\src\main\resources\assets\luna\icon.png"
PREVIEW = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain\preview_icon.png"

os.makedirs(os.path.dirname(OUT), exist_ok=True)
im = Image.open(PHOTO).convert("RGB")
print("photo size:", im.size)

# Head-on photo: her face sits in the upper middle. Square crop, side = S.
W, H = im.size
cx = int(W * 0.50)
cy = int(H * 0.44)
S = int(W * 0.34)
box = (cx - S // 2, cy - S // 2, cx + S // 2, cy + S // 2)
print("crop box:", box)

face = im.crop(box).resize((128, 128), Image.LANCZOS)
face.save(OUT)
face.resize((384, 384), Image.NEAREST).save(PREVIEW)
print("icon bytes:", os.path.getsize(OUT))
print("preview:", PREVIEW)
