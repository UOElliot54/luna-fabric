import zipfile, re, sys

JAR = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\chamomile-tea\.gradle\loom-cache\minecraftMaven\net\minecraft\minecraft-merged-e572a196b7\1.20.1-net.fabricmc.yarn.1_20_1.1.20.1+build.10-v2\minecraft-merged-e572a196b7-1.20.1-net.fabricmc.yarn.1_20_1.1.20.1+build.10-v2.jar"
OUT = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain\jar-assets.txt"

z = zipfile.ZipFile(JAR)
names = z.namelist()
pat = re.compile(r"(cat|ocelot|feline|pet|texturas|textures|models/entity|models/mob|assets)", re.I)
rows = []
for n in names:
    if pat.search(n):
        info = z.getinfo(n)
        rows.append((n, info.file_size))

rows.sort()
with open(OUT, "w", encoding="utf-8") as f:
    f.write("total entries in jar: %d\n" % len(names))
    for n, s in rows:
        f.write("%s\t%d\n" % (n, s))
print("matches:", len(rows))
