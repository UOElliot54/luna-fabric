import zipfile

JAR = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\chamomile-tea\.gradle\loom-cache\minecraftMaven\net\minecraft\minecraft-merged-e572a196b7\1.20.1-net.fabricmc.yarn.1_20_1.1.20.1+build.10-v2\minecraft-merged-e572a196b7-1.20.1-net.fabricmc.yarn.1_20_1.1.20.1+build.10-v2.jar"
OUT = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain\itemdata.txt"

keys = ("items/honey_bottle", "items/milk_bucket", "items/suspicious_stew", "items/chorus_fruit")
z = zipfile.ZipFile(JAR)
names = z.namelist()
hits = [n for n in names if n.endswith(".json") and any(k in n for k in keys)]
with open(OUT, "w", encoding="utf-8") as f:
    for n in hits:
        f.write("=== " + n + " ===\n")
        f.write(z.read(n).decode("utf-8", "replace") + "\n")
    f.write("### grep: lines with time/duration/effect across a wider sample\n")
    import json
    cnt = 0
    for n in names:
        if not n.endswith(".json"):
            continue
        if "items/" not in n:
            continue
        try:
            txt = z.read(n).decode("utf-8")
        except Exception:
            continue
        low = txt.lower()
        if "use_time" in low or "duration" in low:
            f.write("--- " + n + " ---\n")
            f.write(txt + "\n")
            cnt += 1
            if cnt >= 6:
                break
print("hits:", len(hits))
