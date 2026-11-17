import zipfile, os

JAR = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\build\libs\luna-0.0.3.jar"
z = zipfile.ZipFile(JAR)
names = z.namelist()
print("entries:", len(names))
ours = [n for n in names if "com" in n]
for n in ours:
    print(" ", n)

# string constants that prove the identifier / texture wiring survived remapping
want = [b"luna_spawn_egg", b"textures/entity/cat/luna.png", b"luna", b"CatVariant", b"CAT_VARIANT"]
found = {w.decode(): 0 for w in want}
total = 0
for n in names:
    if not n.endswith(".class"):
        continue
    data = z.read(n)
    total += len(data)
    for w in want:
        found[w.decode()] += data.count(w)
print("jar class bytes:", total)
for k, v in found.items():
    print("  contains %r x%d" % (k, v))
