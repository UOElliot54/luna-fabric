from PIL import Image
import os

RES = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\src\main\resources\assets\luna"
OUT = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain"

cat = Image.open(os.path.join(RES, "textures", "entity", "cat", "luna.png")).convert("RGBA")
cat_big = cat.resize((cat.width * 10, cat.height * 10), Image.NEAREST)
# put on a light checker-ish backdrop so transparent areas read clearly
bg = Image.new("RGBA", cat_big.size, (236, 236, 236, 255))
bg.paste(cat_big, (0, 0), cat_big)
p1 = os.path.join(OUT, "preview_luna_cat.png")
bg.convert("RGB").save(p1)
print("cat preview:", bg.size, os.path.getsize(p1))

egg = Image.open(os.path.join(RES, "textures", "item", "luna_spawn_egg.png")).convert("RGBA")
egg_big = egg.resize((egg.width * 12, egg.height * 12), Image.NEAREST)
bg2 = Image.new("RGBA", egg_big.size, (250, 250, 250, 255))
bg2.paste(egg_big, (0, 0), egg_big)
p2 = os.path.join(OUT, "preview_egg.png")
bg2.convert("RGB").save(p2)
print("egg preview:", egg_big.size, os.path.getsize(p2))
