import zipfile

JAR = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\chamomile-tea\.gradle\loom-cache\minecraftMaven\net\minecraft\minecraft-merged-e572a196b7\1.20.1-net.fabricmc.yarn.1_20_1.1.20.1+build.10-v2\minecraft-merged-e572a196b7-1.20.1-net.fabricmc.yarn.1_20_1.1.20.1+build.10-v2.jar"

z = zipfile.ZipFile(JAR)
names = [n for n in z.namelist() if n.startswith("data/") and n.endswith(".json") and "/recipes/" in n]
shown = 0
freeform = 0
for n in names:
    try:
        txt = z.read(n).decode("utf-8")
    except Exception:
        continue
    if "crafting_shapeless" in txt and shown < 3:
        print("== SHAPELESS", n)
        print(txt[:600])
        shown += 1
    if "freeform" in txt:
        freeform += 1
        if freeform <= 2:
            print("== FREEFORM", n)
            print(txt[:600])
print("shapeless shown:", shown, "freeform count:", freeform)
