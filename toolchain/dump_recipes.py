import zipfile, json

JAR = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\chamomile-tea\.gradle\loom-cache\minecraftMaven\net\minecraft\minecraft-merged-e572a196b7\1.20.1-net.fabricmc.yarn.1_20_1.1.20.1+build.10-v2\minecraft-merged-e572a196b7-1.20.1-net.fabricmc.yarn.1_20_1.1.20.1+build.10-v2.jar"

z = zipfile.ZipFile(JAR)
names = [n for n in z.namelist() if n.startswith("data/") and n.endswith(".json") and "/recipes/" in n]
shapes = {}
out = []
for n in names:
    try:
        txt = z.read(n).decode("utf-8")
    except Exception:
        continue
    i = txt.find('"type"')
    if i < 0:
        continue
    t = txt[i:i + 60].split(":")[1].strip().strip('",')[:40]
    shapes.setdefault(t, []).append(n)

for t, files in shapes.items():
    print("TYPE:", t, "count:", len(files))
    for f in files[:2]:
        print("  ", f)
        print(z.read(f).decode("utf-8", "replace")[:700])
print("TOTAL RECIPE FILES:", len(names))
