"""List merged-core jar entries around the render API (registry / factory / feature)."""
import zipfile, re, sys

JAR = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\chamomile-tea\.gradle\loom-cache\minecraftMaven\net\minecraft\minecraft-merged-e572a196b7\1.20.1-net.fabricmc.yarn.1_20_1.1.20.1+build.10-v2\minecraft-merged-e572a196b7-1.20.1-net.fabricmc.yarn.1_20_1.1.20.1+build.10-v2.jar"
OUT = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain\render-api.txt"

z = zipfile.ZipFile(JAR)
names = z.namelist()
pats = ["client/render/", "client/model/", "Registr", "DisplayEntity", "EntityTypeFix", "CatTypeFix"]
seen = {}
for n in names:
    for p in pats:
        if p in n:
            seen.setdefault(p, []).append(n)
with open(OUT, "w", encoding="utf-8") as f:
    for p in pats:
        lst = sorted(seen.get(p, []))
        f.write("== " + p + " : " + str(len(lst)) + "\n")
        for n in lst[:120]:
            f.write(n + "\n")
    f.write("total jar entries: %d\n" % len(names))
print(OUT)
