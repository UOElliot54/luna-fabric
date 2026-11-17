package com.example;

import net.fabricmc.fabric.api.client.rendering.v1.LivingEntityFeatureRendererRegistrationCallback;
import net.fabricmc.fabric.api.client.rendering.v1.LivingEntityFeatureRendererRegistrationCallback.RegistrationHelper;
import net.minecraft.client.render.entity.EntityRendererFactory$Context;
import net.minecraft.client.render.entity.LivingEntityRenderer;
import net.minecraft.client.render.entity.feature.FeatureRendererContext;
import net.minecraft.entity.EntityType;
import net.minecraft.entity.LivingEntity;
import net.minecraft.entity.passive.CatEntity;

// Hands Luna's extra shape to the game's cat renderer. Fabric API calls this while
// the game builds the renderer for cats, so we never replace the renderer itself and
// no other cat is affected.
public class LunaCatFeature implements LivingEntityFeatureRendererRegistrationCallback {
    @Override public void registerRenderers(EntityType<? extends LivingEntity> entityType, LivingEntityRenderer<LivingEntity,?> renderer, LivingEntityFeatureRendererRegistrationCallback.RegistrationHelper helper, EntityRendererFactory.Context context) {
        if (entityType == EntityType.CAT) {
            helper.register(new LunaCatExtras((FeatureRendererContext<CatEntity, CatEntityModel<CatEntity>>) renderer, context));
        }
    }
}
