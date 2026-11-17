import re

EX = r'C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\src\main\java\com\example\LunaCatExtras.java'
FE = r'C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\src\main\java\com\example\LunaCatFeature.java'

e = open(EX, encoding='utf-8').read()
e = e.replace('import net.minecraft.client.render.entity.EntityRendererFactory;',
              'import net.minecraft.client.render.entity.feature.FeatureRendererContext;')
e = e.replace('private static ModelPart buildExtras(EntityRendererFactory'$'Context context)'.replace('$'+"'"+'$',''),
              'PLACEHOLDER')
e = e.replace('import net.minecraft.entity.Entity;', '')
e = e.replace('public void render(MatrixStack matrixStack, VertexConsumerProvider vertexConsumerProvider, int renderOrder, Entity entity, float f0, float f1, float f2, float f3, float f4, float f5) {',
              'public void render(MatrixStack matrixStack, VertexConsumerProvider vertexConsumerProvider, int renderOrder, CatEntity cat, float f0, float f1, float f2, float f3, float f4, float f5) {')
e = e.replace('        if (!(entity instanceof CatEntity)) {\n            return;\n        }\n        CatEntity cat = (CatEntity)entity;\n',
              '')
open(EX, 'w', encoding='utf-8').write(e)
print('extras written')

f = open(FE, encoding='utf-8').read()
f = f.replace('LivingEntityRenderer renderer,', 'LivingEntityRenderer<?, ?> renderer,')
f = f.replace('helper.register(new LunaCatExtras(context));',
              'helper.register(new LunaCatExtras(renderer, context));')
open(FE, 'w', encoding='utf-8').write(f)
print('feature written')
