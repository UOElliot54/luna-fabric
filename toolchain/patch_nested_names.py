import re

for p in (r'C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\src\main\java\com\example\LunaCatExtras.java',
          r'C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\src\main\java\com\example\LunaCatFeature.java'):
    s = open(p, encoding='utf-8').read()
    s = s.replace("'$'", '.')
    open(p, 'w', encoding='utf-8').write(s)
    print(p.split('\\')[-1], s.count('.'))
