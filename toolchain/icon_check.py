"""Confirm every copy of Luna's icon carries the same bytes, and report the size."""
import hashlib
import os
import zipfile

ROOT = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod"
JAR = os.path.join(ROOT, r"import-ready\luna\luna-fabric-1.20.1-0.0.3.jar")
FILES = [
    r"luna\src\main\resources\assets\luna\icon.png",
    r"luna\build\resources\main\assets\luna\icon.png",
    r"import-ready\luna\resources\assets\luna\icon.png",
]
NAME = "assets/luna/icon.png"

with zipfile.ZipFile(JAR) as z:
    inside = z.read(NAME)
    print("jar icon:", len(inside), "bytes;", len(z.namelist()), "entries in jar")

digests = {hashlib.sha256(inside).hexdigest()}
for rel in FILES:
    p = os.path.join(ROOT, rel)
    blob = open(p, "rb").read()
    digests.add(hashlib.sha256(blob).hexdigest())
    print(rel, os.path.getsize(p), "bytes, sha256", hashlib.sha256(blob).hexdigest()[:12])

with zipfile.ZipFile(os.path.join(ROOT, "import-ready", "luna-modrinth.zip")) as z:
    up = z.read(NAME)
    digests.add(hashlib.sha256(up).hexdigest())
    print("upload zip copy:", len(up), "bytes")
    print("jar bytes:", os.path.getsize(JAR))
    print("upload zip icon entry present:", NAME in z.namelist())

print("all copies identical:", len(digests) == 1)
