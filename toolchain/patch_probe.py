import re
EX = r'C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\src\main\java\com\example\LunaCatExtras.java'
FE = r'C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\src\main\java\com\example\LunaCatFeature.java'
D = chr(36)
EM = 'net.minecraft.client.render.entity.model.EntityModel'

e = open(EX, encoding='utf-8').read()
# drop the Context import (unused now), add EntityModel import
e = re.sub(r'import net\.minecraft\.client\.render\.entity\.EntityRendererFactory' + D + r'Context;\r?\n', '', e)
e = e.replace('import net.minecraft.client.render.entity.feature.FeatureRendererContext;',
              'import net.minecraft.client.render.entity.feature.FeatureRendererContext;\nimport ' + EM + ';')
# ctor back to a single feature-context param
e = e.replace('public LunaCatExtras(FeatureRendererContext<CatEntity, CatEntityModel<CatEntity>> featureContext, ',
              'public LunaCatExtras(FeatureRendererContext<CatEntity, CatEntityModel<CatEntity>> context, UNUSED_HEAD')
e = e.replace('context, UNUSED_HEAD' + D + 'Context context) {\n        super(featureContext);',
              'context) {\n        super(context);')
# buildExtras now takes the feature context and reads the vanilla model from it
e = re.sub(r'private static ModelPart buildExtras\(EntityRendererFactory' + D + r'Context context\) \{',
           'private static ModelPart buildExtras(FeatureRendererContext<CatEntity, CatEntityModel<CatEntity>> context) {', e)
e = e.replace('        ModelPart cat = context.getPart(EntityModelLayers.CAT);',
              '        EntityModel<CatEntity> vanilla = context.getModel();\n        ModelPart cat = vanilla.getModel();')
open(EX, 'w', encoding='utf-8').write(e)

f = open(FE, encoding='utf-8').read()
f = f.replace('    public void registerRenderers', '    private static void probeA(EntityRendererFactory' + D + 'Context p) { }\n    private static void probeB(EntityRendererFactory<>.Context p) { }\n    private static void probeC(EntityRendererFactory<?>.Context p) { }\n\n    public void registerRenderers')
open(FE, 'w', encoding='utf-8').write(f)
print('patched', len(e), len(f))
