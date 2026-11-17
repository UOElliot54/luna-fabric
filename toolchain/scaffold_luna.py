import os, shutil

ROOT = r"C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod"
SRC = os.path.join(ROOT, "chamomile-tea")
DST = os.path.join(ROOT, "luna")

# gradle files to copy verbatim (patched below), plus the wrapper bits that made the build work
copies = [
    "build.gradle",
    "settings.gradle",
    "gradlew.bat",
    os.path.join("gradle", "wrapper", "gradle-wrapper.jar"),
    os.path.join("gradle", "wrapper", "gradle-wrapper.properties"),
]
for rel in copies:
    s = os.path.join(SRC, rel)
    d = os.path.join(DST, rel)
    os.makedirs(os.path.dirname(d), exist_ok=True)
    shutil.copyfile(s, d)
    print("copied: %s (%d bytes)" % (rel, os.path.getsize(d)))

# gradle.properties: same pins, new names
props = open(os.path.join(SRC, "gradle.properties"), encoding="utf-8").read()
props = props.replace("archives_base_name=chamomile-tea", "archives_base_name=luna")
props = props.replace("mod_version=0.0.1", "mod_version=0.0.1")
with open(os.path.join(DST, "gradle.properties"), "w", encoding="utf-8") as f:
    f.write(props)
print("wrote gradle.properties (%d bytes)" % os.path.getsize(os.path.join(DST, "gradle.properties")))

# settings.gradle: rename project
st = open(os.path.join(DST, "settings.gradle"), encoding="utf-8").read()
st = st.replace('rootProject.name = \'chamomile-tea\'', 'rootProject.name = \'luna\'')
with open(os.path.join(DST, "settings.gradle"), "w", encoding="utf-8") as f:
    f.write(st)
print("patched settings.gradle rootProject.name -> luna")

os.makedirs(os.path.join(DST, "src", "main", "java", "com", "example"), exist_ok=True)
os.makedirs(os.path.join(DST, "src", "main", "resources", "assets", "luna"), exist_ok=True)
print("scaffold done")
