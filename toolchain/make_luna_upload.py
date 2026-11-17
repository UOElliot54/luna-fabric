"""Build the Modrinth upload archive for Luna: the jar's own layout, plus a changelog file.

Fabric's own rule is the only layout rule that exists: fabric.mod.json sits at the ROOT of the
archive, never nested one folder deep (https://docs.fabricmc.net/develop/loader/fabric-mod-json).
The compiled jar already satisfies that (manifest + META-INF + classes + assets at its root), so
the .zip variant this script writes is just the jar's entries copied over one by one plus
CHANGES.html. The preferred upload file is the jar itself.
"""
import os
import glob
import zipfile

ROOT = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod"
MOD = os.path.join(ROOT, "import-ready", "luna")
OUT = os.path.join(ROOT, "import-ready", "luna-modrinth.zip")
CHANGES = os.path.join(ROOT, "luna", "CHANGES.html")

jars = glob.glob(os.path.join(MOD, "*.jar"))
if len(jars) != 1:
    raise SystemExit("expected exactly one jar in the mod folder, got: %s" % jars)
src_jar, dst_jar = jars[0], os.path.basename(jars[0])

with zipfile.ZipFile(src_jar) as zin, zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zout:
    for info in zin.infolist():
        zout.writestr(info, zin.read(info.filename))
    if os.path.isfile(CHANGES):
        with open(CHANGES, "rb") as fh:
            zout.writestr("CHANGES.html", fh.read())

with zipfile.ZipFile(OUT) as check:
    if not any(i.filename == "fabric.mod.json" for i in check.infolist()):
        raise SystemExit("fabric.mod.json is not at the archive root - do not upload this")

print("upload archive:", OUT, os.path.getsize(OUT), "bytes")
with zipfile.ZipFile(OUT) as zf:
    names = zf.namelist()
print("entries:", len(names))
for n in names:
    if not n.endswith("/"):
        print("  ", n, zf.getinfo(n).file_size)
