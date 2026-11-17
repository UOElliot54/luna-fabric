package com.example;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.client.rendering.v1.LivingEntityFeatureRendererRegistrationCallback;
import net.minecraft.item.Item;
import net.minecraft.entity.passive.CatVariant;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.text.Text;
import net.minecraft.util.DyeColor;
import net.minecraft.util.Identifier;

public class Luna implements ModInitializer {
   public static final String MOD_ID = "luna";

   // The cat coat that makes Luna look like Luna: assets/luna/textures/entity/cat/luna.png
   public static final Identifier LUNA_TEXTURE_ID = new Identifier(MOD_ID, "textures/entity/cat/luna.png");
   public static final Identifier LUNA_VARIANT_ID = new Identifier(MOD_ID, "luna");
   public static final CatVariant LUNA_VARIANT = new CatVariant(LUNA_TEXTURE_ID);

   // The nameplate that floats above her, like she was given a nametag.
   public static final Text LUNA_NAME = Text.of("Luna");

    // Vanilla draws a 3D collar around a tamed cat's neck; Luna wears a pink one so she
    // stands out against her brown-silver coat. Change this to any DyeColor you like.
    public static final DyeColor LUNA_COLLAR = DyeColor.PINK;

   // The item you hold to bring her into the world
   public static final Identifier LUNA_EGG_ID = new Identifier(MOD_ID, "luna_spawn_egg");
   public static final LunaSpawnEgg LUNA_SPAWN_EGG = new LunaSpawnEgg(new Item.Settings());

   @Override public void onInitialize() {
      // Teach the game about Luna's coat, then add her spawn egg to the item registry.
      Registry.register(Registries.CAT_VARIANT, LUNA_VARIANT_ID, LUNA_VARIANT);
      Registry.register(Registries.ITEM, LUNA_EGG_ID, LUNA_SPAWN_EGG);
   }
}
