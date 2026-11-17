package com.example;

import net.minecraft.client.render.entity.feature.FeatureRenderer;
import net.minecraft.client.render.entity.feature.FeatureRendererContext;
import net.minecraft.client.render.entity.model.CatEntityModel;
import net.minecraft.client.render.VertexConsumerProvider;
import net.minecraft.client.util.math.MatrixStack;
import net.minecraft.client.model.ModelData;
import net.minecraft.client.model.ModelPart;
import net.minecraft.client.model.ModelPartBuilder;
import net.minecraft.client.model.ModelPartData;
import net.minecraft.client.model.ModelTransform;
import net.minecraft.client.model.TexturedModelData;
import net.minecraft.entity.passive.CatEntity;
import net.minecraft.util.Identifier;

// Luna's extra shape, drawn on top of the vanilla cat body: a mane ruff, cheek fluff,
// ear tufts, whiskers, a bushy tail and furry ankles. Each piece hangs off one of the
// game's own cat parts, so it follows the head, tail and leg animations the same way
// the vanilla cat collar does. The part names and pivots below match the vanilla cat
// model, which is why these extras land in the right places. Only Luna gets them.
public class LunaCatExtras extends FeatureRenderer<CatEntity, CatEntityModel<CatEntity>> {
    // Fluff texture sheet: assets/luna/textures/entity/cat/luna_fluff.png (128x64)
    private static final int SHEET_W = 128;
    private static final int SHEET_H = 64;
    private static final int MANE_UV = 0;
    private static final int CHEEK_UV = 32;
    private static final int TUFT_UV = 56;
    private static final int WHISK_UV = 80;
    private static final int TAIL_UV = 104;
    private static final int PAW_UV = 0;

    private final CatEntityModel<CatEntity> model;

    public LunaCatExtras(FeatureRendererContext context) {
        super(context);
        this.model = new CatEntityModel<CatEntity>(buildExtras());
    }

    // Local coordinates below are relative to each vanilla part's own pivot.
    private static ModelPart buildExtras() {
        ModelData data = new ModelData();
        ModelPartData root = data.getRoot();

        ModelPartData head = root.addChild("head", ModelPartBuilder.create(), ModelTransform.pivot(0f, 15f, -9f));
        head.addChild("mane_back", ModelPartBuilder.create().uv(MANE_UV, 0).cuboid(-3.5f, -3f, 1.5f, 3.5f, 3f, 4.5f), ModelTransform.NONE);
        head.addChild("mane_top", ModelPartBuilder.create().uv(MANE_UV, 0).cuboid(-3f, -3.5f, -1f, 3f, -2f, 3f), ModelTransform.NONE);
        head.addChild("mane_left", ModelPartBuilder.create().uv(MANE_UV, 0).cuboid(-5.5f, -3f, -1f, -3f, 3f, 3f), ModelTransform.NONE);
        head.addChild("mane_right", ModelPartBuilder.create().uv(MANE_UV, 0).cuboid(3f, -3f, -1f, 5.5f, 3f, 3f), ModelTransform.NONE);
        head.addChild("cheek_left", ModelPartBuilder.create().uv(CHEEK_UV, 0).cuboid(-5f, -1f, -3f, -3f, 2.5f, 0.5f), ModelTransform.NONE);
        head.addChild("cheek_right", ModelPartBuilder.create().uv(CHEEK_UV, 0).cuboid(3f, -1f, -3f, 5f, 2.5f, 0.5f), ModelTransform.NONE);
        head.addChild("ear_tuft_left", ModelPartBuilder.create().uv(TUFT_UV, 0).cuboid(-3.2f, -5f, -1f, -1.6f, -2f, 1f), ModelTransform.NONE);
        head.addChild("ear_tuft_right", ModelPartBuilder.create().uv(TUFT_UV, 0).cuboid(1.6f, -5f, -1f, 3.2f, -2f, 1f), ModelTransform.NONE);

        ModelPartData whiskers = head.addChild("whiskers", ModelPartBuilder.create(), ModelTransform.NONE);
        whiskers.addChild("whisk_left_high", ModelPartBuilder.create().uv(WHISK_UV, 8).cuboid(-8f, 0.5f, -2f, -2.5f, 1f, -1.5f), ModelTransform.NONE);
        whiskers.addChild("whisk_left_low", ModelPartBuilder.create().uv(WHISK_UV, 14).cuboid(-8f, 1.5f, -2f, -2.5f, 2f, -1.5f), ModelTransform.NONE);
        whiskers.addChild("whisk_left_brow", ModelPartBuilder.create().uv(WHISK_UV, 20).cuboid(-6.5f, -1.5f, -3f, -2.5f, -1f, -2.5f), ModelTransform.NONE);
        whiskers.addChild("whisk_right_high", ModelPartBuilder.create().uv(WHISK_UV, 8).cuboid(2.5f, 0.5f, -2f, 8f, 1f, -1.5f), ModelTransform.NONE);
        whiskers.addChild("whisk_right_low", ModelPartBuilder.create().uv(WHISK_UV, 14).cuboid(2.5f, 1.5f, -2f, 8f, 2f, -1.5f), ModelTransform.NONE);
        whiskers.addChild("whisk_right_brow", ModelPartBuilder.create().uv(WHISK_UV, 20).cuboid(2.5f, -1.5f, -3f, 6.5f, -1f, -2.5f), ModelTransform.NONE);

        root.addChild("body", ModelPartBuilder.create(), ModelTransform.of(0f, 12f, -10f, 1.5707964f, 0f, 0f));

        ModelPartData tail1 = root.addChild("tail1", ModelPartBuilder.create(), ModelTransform.of(0f, 15f, 8f, 0.9f, 0f, 0f));
        tail1.addChild("tail_fluff", ModelPartBuilder.create().uv(TAIL_UV, 0).cuboid(-1.8f, 0.5f, -1.3f, 1.8f, 7.5f, 2.3f), ModelTransform.NONE);
        ModelPartData tail2 = root.addChild("tail2", ModelPartBuilder.create(), ModelTransform.pivot(0f, 20f, 14f));
        tail2.addChild("tail_tip", ModelPartBuilder.create().uv(TAIL_UV, 16).cuboid(-1.8f, 0f, -1.3f, 1.8f, 6.5f, 2.3f), ModelTransform.NONE);

        ModelPartData legLeftHind = root.addChild("left_hind_leg", ModelPartBuilder.create(), ModelTransform.pivot(1.1f, 18f, 5f));
        legLeftHind.addChild("ankle_fluff", ModelPartBuilder.create().uv(PAW_UV, 40).cuboid(-1.7f, 3.5f, -0.7f, 1.7f, 6f, 3.7f), ModelTransform.NONE);
        ModelPartData legRightHind = root.addChild("right_hind_leg", ModelPartBuilder.create(), ModelTransform.pivot(-1.1f, 18f, 5f));
        legRightHind.addChild("ankle_fluff", ModelPartBuilder.create().uv(PAW_UV, 40).cuboid(-1.7f, 3.5f, -0.7f, 1.7f, 6f, 3.7f), ModelTransform.NONE);
        ModelPartData legLeftFront = root.addChild("left_front_leg", ModelPartBuilder.create(), ModelTransform.pivot(1.2f, 14.1f, -5f));
        legLeftFront.addChild("toe_fluff", ModelPartBuilder.create().uv(PAW_UV + 8, 48).cuboid(-1.7f, 6.5f, -0.7f, 1.7f, 9f, 2.7f), ModelTransform.NONE);
        ModelPartData legRightFront = root.addChild("right_front_leg", ModelPartBuilder.create(), ModelTransform.pivot(-1.2f, 14.1f, -5f));
        legRightFront.addChild("toe_fluff", ModelPartBuilder.create().uv(PAW_UV + 8, 48).cuboid(-1.7f, 6.5f, -0.7f, 1.7f, 9f, 2.7f), ModelTransform.NONE);

        return TexturedModelData.of(data, SHEET_W, SHEET_H).createModel();
    }

    @Override public void render(MatrixStack matrixStack, VertexConsumerProvider vertexConsumerProvider, int renderOrder, CatEntity cat, float f0, float f1, float f2, float f3, float f4, float f5) {
        if (cat.getVariant() != Luna.LUNA_VARIANT) {
            return;
        }
        // The game's own feature renderer draws these parts and handles the animation
        // for us, so no cat behaviour or movement code is touched.
        FeatureRenderer.render(getContextModel(), model, Luna.LUNA_FLUFF_TEXTURE_ID, matrixStack, vertexConsumerProvider, renderOrder, cat, f0, f1, f3, f4, f5, f2, 1f, 1f, 1f);
    }
}
