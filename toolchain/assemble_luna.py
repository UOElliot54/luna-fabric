"""Assemble the drop-in Fabric mod package for the Luna trial mod.

Adds (without touching the chamomile-tea package already sitting there):
  import-ready/luna/
    luna-fabric-1.20.1-0.0.3.jar  (loom-remapped jar from build/libs; the filename carries
                                   mod id, loader, game version and mod version like the
                                   other jars in the Homestead pack do)
    resources/fabric.mod.json
    resources/assets/...
  import-ready/luna.zip          (same tree, single root folder -> drop into a pack zip root)
"""
import glob
import os
import shutil
import zipfile
import json

ROOT = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod"
PROJ = os.path.join(ROOT, "luna")
SRC_RES = os.path.join(PROJ, "build", "resources", "main")  # loom's processed tree (${version} expanded)
LIBS = os.path.join(PROJ, "build", "libs")
CANDIDATES = glob.glob(os.path.join(LIBS, "luna-*.jar"))
JAR = max(CANDIDATES, key=os.path.getmtime)
OUT_ROOT = os.path.join(ROOT, "import-ready")
MOD_DIR = os.path.join(OUT_ROOT, "luna")

# Naming follows the in-pack convention seen next to the other Homestead jars:
#   carycon-fabric-1.20.1-2.1.2.7.jar, celestconfig-fabric-1.20.1-1.1.2.jar,
#   balm-fabric-1.20.1-7.3.3.jar, chipped-fabric-1.20.1-3.0.7.jar
# so: <mod id>-fabric-<game version>-<mod version>.jar. The manifest inside the jar still
# says id "luna" and version 0.0.3; the file name is only ever the human-readable label.
JAR_NAME = "luna-fabric-1.20.1-0.0.3.jar"

assert os.path.isfile(JAR), "missing built jar"

# only this mod's folder is rebuilt; the tea package next to it stays put
shutil.rmtree(MOD_DIR, ignore_errors=True)
os.makedirs(MOD_DIR, exist_ok=True)

shutil.copyfile(JAR, os.path.join(MOD_DIR, JAR_NAME))

for dirpath, _dirnames, filenames in os.walk(SRC_RES):
    for name in filenames:
        src = os.path.join(dirpath, name)
        rel = os.path.relpath(src, SRC_RES)
        dst = os.path.join(MOD_DIR, "resources", rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(src, dst)

mod_json = json.load(open(os.path.join(MOD_DIR, "resources", "fabric.mod.json"), encoding="utf-8"))
print("id:", mod_json.get("id"), "version:", mod_json.get("version"))

zip_path = os.path.join(OUT_ROOT, "luna.zip")
if os.path.exists(zip_path):
    os.remove(zip_path)
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for dirpath, _dirnames, filenames in os.walk(MOD_DIR):
        for name in sorted(filenames):
            src = os.path.join(dirpath, name)
            arc = os.path.relpath(src, OUT_ROOT).replace("\\", "/")
            zf.write(src, arc)

names = zipfile.ZipFile(zip_path).namelist()
print("zip entries:", len(names))
for n in names:
    print(" ", n)
print("jar bytes:", os.path.getsize(os.path.join(MOD_DIR, JAR_NAME)))
print("zip bytes:", os.path.getsize(zip_path))
