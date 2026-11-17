import zipfile
from collections import Counter

JAR = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\chamomile-tea\.gradle\loom-cache\minecraftMaven\net\minecraft\minecraft-merged-e572a196b7\1.20.1-net.fabricmc.yarn.1_20_1.1.20.1+build.10-v2\minecraft-merged-e572a196b7-1.20.1-net.fabricmc.yarn.1_20_1.1.20.1+build.10-v2.jar"

z = zipfile.ZipFile(JAR)
names = [n for n in z.namelist() if n.startswith("data/") and n.endswith(".json") and "/recipes/" in n]
depths = Counter(n.count("/") for n in names)
print("total:", len(names))
print("depth histogram:", dict(sorted(depths.items())))
maxd = max(depths)
print("deepest examples:")
for n in [x for x in names if x.count("/") == maxd][:6]:
    print("  ", n)
print("mid-depth examples:")
for d in sorted(depths):
    ex = [x for x in names if x.count("/") == d][:3]
    print(" depth", d)
    for e in ex:
        print("  ", e)
pref = Counter("/".join(n.split("/")[:4]) for n in names)
print("namespace dirs:", list(pref.items())[:10])
print("any recipes/minecraft/:", sum(1 for n in names if "/recipes/minecraft/" in n))
