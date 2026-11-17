# Luna — the Maine Coon (Java Minecraft 1.20.1, Fabric loader)

A spawn egg that conjures **Luna**, a cat modelled on my own Maine Coon. Left-click a
surface with the egg and she steps out: an ordinary vanilla cat wearing her own coat,
a pink collar and a floating nameplate that says **Luna**. Nothing else is added or
changed — she sleeps with you, follows you, gets fed, and behaves exactly like a cat
the game would spawn, which is why the egg works in Creative as well as in a survival
world.

## Targets

| | |
| --- | --- |
| Game version | Java `1.20.1` (the version the Homestead pack pins) |
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
| `luna/CHANGES.html` | The changelog text the Modrinth page shows |
| `luna/IMPORT-INTO-HOMESTEAD.md` | How the package drops into the Homestead pack zip |
| `luna/MODRINTH-PUBLISH.md` | The publishing notes: which file to attach, which fields to set, what the moderation queue does |
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

Put the jar in `.minecraft/mods/luna/` with `resources/` beside it, or install the
Modrinth listing. The jar needs no Fabric API dependency.

## Licence

MIT — see `LICENSE`. One honest caveat: her coat texture was generated from photographs
of the real cat and built on top of Minecraft's own cat texture, so Minecraft's usage
rules govern that material; MIT covers the code, the artwork and the packaging written
for this project.

## How it was made

The code, the coat and the icon were produced with an AI coding assistant; the design
decisions, art direction, testing and bug reports were mine (a stack of 64 eggs drinking
all at once, a face that rendered wrong after an over-enlarged eye pass, an icon that
read as nothing). Other experiments from the same workspace, including a chamomile-tea
trial mod, are kept out of this repository.
