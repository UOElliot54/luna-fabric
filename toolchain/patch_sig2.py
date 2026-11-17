EX = r'C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\src\main\java\com\example\LunaCatExtras.java'
FE = r'C:\Users\ElliotPC\Documents\StrataProjects\MinecraftMod\luna\src\main\java\com\example\LunaCatFeature.java'
NEST = 'EntityRendererFactory' + chr(36) + 'Context'
FEATCTX = 'FeatureRendererContext<CatEntity, CatEntityModel<CatEntity>>'

e = open(EX, encoding='utf-8').read()
e = e.replace('public LunaCatExtras(' + FEATCTX + ' context) {\n        super(context);',
              'public LunaCatExtras(' + FEATCTX + ' featureContext, ' + NEST + ' context) {\n        super(featureContext);')
e = e.replace('buildExtras(' + NEST + ' context)', 'buildExtras(' + NEST + ' context)')
e = e.replace('render(MatrixStack matrixStack, VertexConsumerProvider vertexConsumerProvider, int renderOrder, Entity entity,',
              'render(MatrixStack matrixStack, VertexConsumerProvider vertexConsumerProvider, int renderOrder, CatEntity cat,')
e = e.replace('        if (!(entity instanceof CatEntity)) {\n            return;\n        }\n        CatEntity cat = (CatEntity)entity;\n', '')
open(EX, 'w', encoding='utf-8').write(e)
print('extras ok')

f = open(FE, encoding='utf-8').read()
f = f.replace('import net.minecraft.client.render.entity.LivingEntityRenderer;',
              'import net.minecraft.client.render.entity.LivingEntityRenderer;\nimport net.minecraft.client.render.entity.feature.FeatureRendererContext;')
f = f.replace('LivingEntityRenderer renderer,', 'LivingEntityRenderer<LivingEntity,?> renderer,')
f = f.replace('helper.register(new LunaCatExtras(context));',
              'helper.register(new LunaCatExtras((' + FEATCTX + ') renderer, context));')
open(FE, 'w', encoding='utf-8').write(f)
print('feature ok')
