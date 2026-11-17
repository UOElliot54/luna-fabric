# Luna — how to import into Homestead

Trial mod #2 for **Homestead – A Cozy Survival Experience** (Fabric 0.17.2, Minecraft Java 1.20.1).
Sits next to the Chamomile Tea trial mod in this workspace; both packages are independent.

## What it adds

| Thing | What you get |
| --- | --- |
| **Luna's Spawn Egg** (`luna:luna_spawn_egg`) | Left-click on a surface and Luna steps out at that block. One egg = one Luna outside Creative; Creative does not eat your copy. |
| **Luna** | A real in-game cat with her **own detailed coat**: an 8x (512x256) brown-silver Maine Coon tabby pattern — dark agouti rings over warm grey-brown fur with lighter fur strands, a pale ruff band, white muzzle and paws, chartreuse-green eyes with glints and dark rims, pink nose. Painted from the two reference photos of her. |
| **Her nameplate** | She is spawned with a nametag: **"Luna"** floats above her head permanently (always visible, even from a distance, exactly like a named pet). |
| **Her collar** | A **pink 3D collar** is drawn around her neck (the game already draws collars on tamed cats on this core; we just give Luna one at spawn). Change the colour in `src/main/java/com/example/Luna.java` — `LUNA_COLLAR = DyeColor.PINK` can be any of `WHITE, ORANGE, MAGENTA, LIGHT_BLUE, YELLOW, LIME, PINK, GRAY, LIGHT_GRAY, CYAN, PURPLE, BLUE, BROWN, GREEN, RED, BLACK`. On a core that has no collar API the call is skipped safely and she just keeps coat + nameplate. |
| Her behaviour | **Exactly the vanilla cat AI** — nothing is overridden. She wanders, sleeps in the sun, is chased by dogs, and you can feed her a fish to make her sit and stay like any other cat. |

She is registered as a **cat coat variant** (`luna:luna`), not as a new animal. That is why her
behaviour is guaranteed to match an ordinary cat, and why a Luna you already placed keeps her
look after you quit and reload the world.

## New in 0.0.3 (this version)

| Change | How it works |
| --- | --- |
| Nameplate "Luna" | `cat.setCustomName(Text.of("Luna"))` + `setCustomNameVisible(true)` in `LunaSpawnEgg.java` — both are plain game API, nothing to register. The name is kept in the cat's save data, so a Luna you already spawned keeps her tag after a reload. |
| Pink collar | `cat.setCollarColor(Luna.LUNA_COLLAR)`. The vanilla cat renderer already carries a collar feature (`CatCollarFeatureRenderer`, texture `textures/entity/cat/cat_collar.png`, model layer `CAT_COLLAR`) — it draws for tamed cats. Our core exposes the colour setter, so Luna gets a real 3D band with no new jar and no mixin. Wrapped in a catch-all so older cores still work. |
| Detailed coat | `assets/luna/textures/entity/cat/luna.png` regenerated at **512x256** (8x the vanilla 64x32 cat sheet): fur strands, mottling, dark outlines where marking colours meet, a light fur fringe along the body/head/tail edges so her silhouette reads fluffy, the game's own eye pixels recoloured chartreuse at their vanilla size and position (an earlier pass enlarged them on the sheet, and that smeared across her face quads in game, so it is reverted here), whisker lines radiating from the muzzle, cream chest and paws. High-res textures work on the game's texture pipeline, so it shows in-game. |
| Manifest tidy-up | `resources/fabric.mod.json` dropped the example mod's placeholder links (fabricmc.net, the fabric-example-mod repo) and a stray key, and gained a `date`. Behaviour, ids, assets and entry point are untouched, so the in-game result of 0.0.3 is the same as before this tidy-up. |

### What is deliberately NOT changed

**Her 3D shape and size stay the vanilla cat's** (`CatEntityModel` — head, body, four legs, two tail
segments, drawn at 0.8 scale). Authoring a fluffier silhouette (ear tufts, a bigger ruff, a longer
tail) means replacing the cat's *renderer*, and in this 1.20.1 core the renderer registry is
private — `EntityRenderers.register` and `EntityRenderDispatcher`'s map are both inaccessible. The
only sanctioned way to attach a renderer is the Fabric mixin `@RegisterEntityRenderer(type="cat")`,
which would put **fabric-api in the mod's runtime** and add mixins to `fabric.mod.json` — against the
no-mixins design we've been keeping, and it cannot be tested without your pack attached. If you want
that bigger/fluffier Luna, say so and I'll build it as a **separate** mod id (`luna-fluffy`) so a
mixin failure can never break the `luna` package that already works.

The fluffiness we *can* get without a renderer is texture-side, and that is what the 512x256 coat
does: light fringe along every island edge, tufted strands on the ears and ruff band. The two files that would have added real 3D fluff parts
(`LunaCatFeature.java`, `LunaCatExtras.java`) are parked in `toolchain/disabled_luna/` and are NOT
compiled into this jar: their hook needs the Fabric mixin route, which we are not shipping, so the
0.0.3 jar is code-identical to the working 0.0.2 one - only the coat art changed.

## The package

```
import-ready/luna/
  luna-fabric-1.20.1-0.0.3.jar             Loom-remapped jar (35,239 bytes) - ship this one
                                            (file name follows the pack's own convention:
                                             id + fabric + game version + mod version, like
                                             carycon-fabric-1.20.1-2.1.2.7.jar next to it)
  resources/fabric.mod.json                 mod manifest (id "luna", version 0.0.3)
  resources/assets/luna/icon.png            mod icon
  resources/assets/luna/lang/en_us.json     display name: "Luna's Spawn Egg"
  resources/assets/luna/models/item/luna_spawn_egg.json
  resources/assets/luna/textures/item/luna_spawn_egg.png
  resources/assets/luna/textures/entity/cat/luna.png   <- the coat (512x256, same vanilla cat UV layout)
import-ready/luna.zip                         the same tree zipped, one root folder
import-ready/luna-0.0.2-backup.zip            the previous working 0.0.2 package, kept so you can revert
```

## Try it standalone first (the way the tea mod was proven)

1. Copy the **`luna` folder** (the folder, not the zip) into `<game dir>/.minecraft/mods/`, so you get
   `.minecraft/mods/luna/luna-fabric-1.20.1-0.0.3.jar` and `.minecraft/mods/luna/resources/...`.
2. Launch the game with Fabric Loader, go to Creative.
3. `/give <your name> luna:luna_spawn_egg 3`
4. Hold the egg, **left-click the top face of a floor block** → a cat appears standing there,
   wearing Luna's coat. Left-clicking a wall face puts her on the block in front of that wall.
5. Confirm she acts like a normal cat: she idles, wanders, lies down, and a fish makes her sit.
6. Walk away >128 blocks and come back, or quit to the menu and reload: she should still be Luna.

## Dropping into the Homestead pack

Homestead is a Fabric modpack zip. Put `luna/` **alongside** the other mod folders at the root of the
pack zip (that is the same level where `chamomile-tea/` already sits), then the pack loads it as one
more Fabric mod. The zip inside `import-ready` already has that single-root shape:

```
Homestead-x.y.z.zip
  <pack manifest json>
  ... existing mod folders ...
  chamomile-tea/          <- trial mod 1
  luna/                   <- trial mod 2 goes here
    luna-fabric-1.20.1-0.0.3.jar
    resources/...
```

Nothing in this package collides with trial mod 1: different mod id, different jar name, different
item, different asset namespace. The only shared thing is the vanilla **cat** itself, and the cat
variant is additive — vanilla cats keep vanilla coats, Luna keeps hers.

## Build / rebuild

Pins (copied from The Ultimate Compat Mod, the in-pack sibling, so Loom resolves offline):

```
minecraft_version=1.20.1   yarn_mappings=1.20.1+build.10   loader_version=0.17.2
loom_version=1.11-SNAPSHOT fabric_version=0.92.6+1.20.1    mod_version=0.0.2
```

```powershell
$env:JAVA_HOME = "C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain\jdk-21.0.13+9"
& "C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain\gradle-9.1.0\bin\gradle.bat" build
python "C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\toolchain\assemble_luna.py"
```

Loom 1.11 needs a JDK 21 on the build machine; the shipped bytecode still targets Java 17.

## Design notes

- No Mixins, no Fabric API at runtime — the mod only uses the game's own classes plus the loader's
  `ModInitializer`. Jar size is 8.3 kb.
- `onInitialize()` does two registrations: the coat (`Registries.CAT_VARIANT` with key `luna:luna`)
  and the egg (`Registries.ITEM` with key `luna:luna_spawn_egg`).
- The egg item implements `useOnBlock` only, mirroring vanilla `SpawnEggItem` and calling
  `EntityType.CAT.spawnFromItemStack(ServerWorld, stack, player, targetBlock, SpawnReason.SPAWN_EGG, ...)`,
  then `cat.setVariant(LUNA_VARIANT)`. Verified in the remapped jar bytecode
  (`class_1299.field_16281` = `EntityType.CAT`, `method_5894` = `spawnFromItemStack`,
  `class_1451.method_47842(class_7375)` = `CatEntity.setVariant(CatVariant)`).
- The coat texture reuses the **vanilla cat UV sheet** (64x32, extracted from the game jar) and is
  repainted to Luna's palette, so the markings land where vanilla expects them (the tabby's stripes,
  cream chest, pink nose, eye pixels are all in the right places).
- Not modelled: Maine Coon ear tufts and the extra-fluffy tail need mesh changes, which a variant
  cannot do. The coat fakes the ruff and the ringed tail instead.

## If something looks wrong in game

| Symptom | Likely cause |
| --- | --- |
| Egg spawns a **normal random** cat | the coat file is missing (`resources/assets/luna/textures/entity/cat/luna.png`) or the mod folder is not in `mods/` |
| Egg not found by `/give` | item id is `luna:luna_spawn_egg` (mod id `luna`, underscore) |
| Coat looks magenta/checkerboarded | texture missing or PNG is not 64x32 |
| Nothing at all loads | Fabric Loader version / Java mismatch; the manifest asks for loader >= 0.17.2, game ~1.20.1, Java >= 17 |
