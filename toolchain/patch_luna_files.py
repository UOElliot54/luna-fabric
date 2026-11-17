import re, os

EX = r'C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\src\main\java\com\example\LunaCatExtras.java'
FE = r'C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\src\main\java\com\example\LunaCatFeature.java'
LU = r'C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\src\main\java\com\example\Luna.java'

s = open(EX, encoding='utf-8').read()
s = re.sub(r'\bPLACEHOLDER\b', '', s)
s = re.sub(r'\bn[aeiouA-Z]{0,3}ckX\b', 'midX', s)
s = s.replace('_PLACEHOLDER', '')
open(EX, 'w', encoding='utf-8').write(s)
print('extras lines:', s.count(chr(10)))

f = open(FE, encoding='utf-8').read()
f = re.sub(r'new LunaCatExtras<[^>]*>\(', 'new LunaCatExtras(', f)
open(FE, 'w', encoding='utf-8').write(f)
print('feature fixed new-line count:', f.count(chr(10)))

l = open(LU, encoding='utf-8').read()
if 'LunaCatFeature' not in l:
    l = l.replace('import net.minecraft.item.Item;',
                  'import net.fabricmc.fabric.api.client.rendering.v1.LivingEntityFeatureRendererRegistrationCallback;\nimport net.minecraft.item.Item;', 1)
    hook = ('       // Hand Luna her extra shape to the game\'s cat renderer (Fabric API event).\n'
            '       try {\n'
            '          LivingEntityFeatureRendererRegistrationCallback.EVENT.register(new LunaCatFeature());\n'
            '       } catch (Throwable ignore) {\n'
            '          // If the pack has no Fabric API, Luna keeps her coat, collar and nameplate.\n'
            '       }\n')
    l = l.replace('       Registry.register(Registries.CAT_VARIANT,', hook + '       Registry.register(Registries.CAT_VARIANT,', 1)
    open(LU, 'w', encoding='utf-8').write(l)
    print('luna patched')
else:
    print('luna already patched')
