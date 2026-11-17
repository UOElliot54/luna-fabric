import zipfile, os

JAR = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\chamomile-tea\.gradle\loom-cache\minecraftMaven\net\minecraft\minecraft-merged-e572a196b7\1.20.1-net.fabricmc.yarn.1_20_1.1.20.1+build.10-v2\minecraft-merged-e572a196b7-1.20.1-net.fabricmc.yarn.1_20_1.1.20.1+build.10-v2.jar"
OUT = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain\cat_tex"

z = zipfile.ZipFile(JAR)
targets = [n for n in z.namelist() if n.startswith("assets/minecraft/textures/entity/cat/") and n.endswith(".png")]
os.makedirs(OUT, exist_ok=True)
for t in targets:
    data = z.read(t)
    dest = os.path.join(OUT, os.path.basename(t))
    with open(dest, "wb") as f:
        f.write(data)
    print("%s -> %d bytes" % (os.path.basename(t), len(data)))
