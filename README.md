# Luna (Java Minecraft 1.20.1, Fabric Mod)

A spawn egg that summons **Luna**. An ordinary vanilla cat wearing her own coat,
a pink collar and a floating nameplate that says **Luna**. Nothing else is added or
changed which is why the egg works in Creative as well as in a survival
world.

## Targets

| | |
| --- | --- |
| Game version | Java `1.20.1` |
| Loader | Fabric `>=0.17.2` |
| Build toolchain | Loom `1.11-SNAPSHOT`, yarn `1.20.1+build.10`, Java 21 to build |
| Fabric API | **not required** — the code uses only Minecraft's own classes |

## Repository layout

| Path | What it is |
| --- | --- |
| `luna/src/` | The two Java files (`Luna`, `LunaSpawnEgg`) and the resources: her coat, egg icon, item model, display name |
| `luna/fabric.mod.json` | The manifest source (the `version` field is a template filled in by the build) |
| `luna/build.gradle`, `luna/settings.gradle`, `luna/gradle.properties`, `gradlew.bat` | The Fabric/Gradle project, with the version pins above written into `gradle.properties` |
| `import-ready/luna/` | The built artifact: `luna-fabric-1.20.1-0.0.3.jar` (the file hosted on Modrinth) plus the same resources in loose folder form for a `.minecraft/mods` drop |
| `toolchain/` | How the coat, the icon and the packaging were made. These scripts use absolute local paths, so they are for reading, not a build entry point |

## Building

Point `JAVA_HOME` at a Java 21 (the pinned Loom requires it) and run Gradle from the
`luna/` folder:

```
cd luna
./gradlew build
```

That produces `luna/build/libs/luna-0.0.3.jar`. The shipped copy is renamed to
`luna-fabric-1.20.1-0.0.3.jar` — the way the other Homestead jars are named — and the
manifest inside still declares id `luna`, version `0.0.3`. Renaming the file changes
nothing about how it loads.

## Installing

Put the jar from `import-ready/luna/` in `.minecraft/mods/`, or install from the
Modrinth listing https://modrinth.com/mod/luna-elliot01ka (Currently Project Under Review). The jar needs no Fabric API dependency.

## Licence

MIT — see `LICENSE`. Her coat texture was generated from photographs
of the real cat and built on top of Minecraft's own cat texture, so Minecraft's usage
rules govern that material; MIT covers the code, the artwork and the packaging written
for this project.

The manifest inside the jar carries this repository twice — a `contact` block whose `sources`
member is the repository URL and whose `issues` member is the issue tracker — so a downloaded
copy of the file points back here. Fabric's v1 manifest spec has no `source_url` key; `contact`
is the name, with `email`, `irc`, `homepage`, `issues` and `sources` as its defined members
(<https://wiki.fabricmc.net/documentation:fabric_mod_json_spec>).

## How it was made

The code, the coat and the icon were produced with Qwen3.8-Flash-Next Coder IQ1_M running locally with Strata; the design
decisions, art direction, testing and bug reports were mine.