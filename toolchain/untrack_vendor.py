"""Drop third-party / vendored material out of the index (files stay on disk).

Everything under toolchain/ that is not one of our own .py scripts, the parked
extras sources, or a README is evidence about the game core, other authors'
reference sources, vendored jars and first-party game textures. Keeping those
out of the repo means a public clone or a zip upload can never carry licensed
material that is not ours.
"""
import os
import subprocess

ROOT = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod"
listed = subprocess.run(
    ["git", "ls-files", "--", "toolchain"],
    cwd=ROOT, capture_output=True, text=True,
).stdout.split()

drop = []
for f in listed:
    if f.endswith(".py"):
        continue
    if f.startswith("toolchain/disabled_luna/"):
        continue
    if f.startswith("toolchain/README"):
        continue
    drop.append(f)

print("tracked under toolchain:", len(listed), "-> dropping:", len(drop))
if drop:
    subprocess.run(["git", "rm", "--cached", "-q", "--"] + drop, cwd=ROOT, check=True)
    subprocess.run(["git", "add", "-f", "--", ".gitignore", ".gitattributes"], cwd=ROOT, check=True)
after = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout.split()
print("tracked total now:", len(after))
for bad in (".jar", ".zip", ".png"):
    hits = [f for f in after if f.endswith(bad)]
    print(bad, "->", len(hits), "files:", [h for h in hits if h.startswith("toolchain/")])
