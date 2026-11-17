package com.example;

import net.minecraft.entity.EntityType;
import net.minecraft.entity.player.PlayerEntity;
import net.minecraft.entity.passive.CatEntity;
import net.minecraft.entity.SpawnReason;
import net.minecraft.item.Item;
import net.minecraft.item.ItemUsageContext;
import net.minecraft.item.ItemStack;
import net.minecraft.server.world.ServerWorld;
import net.minecraft.util.ActionResult;
import net.minecraft.util.math.BlockPos;
import net.minecraft.util.math.Direction;
import net.minecraft.world.event.GameEvent;
import net.minecraft.world.World;

public class LunaSpawnEgg extends Item {
   public LunaSpawnEgg(Item.Settings settings) {
      super(settings);
   }

   // Left click on a surface: put Luna in the world at the aimed block, like a spawn egg.
   @Override public ActionResult useOnBlock(ItemUsageContext context) {
      World world = context.getWorld();
      if (!(world instanceof ServerWorld)) {
         return ActionResult.SUCCESS;
      }

      ItemStack stack = context.getStack();
      PlayerEntity player = context.getPlayer();
      BlockPos blockPos = context.getBlockPos();
      Direction side = context.getSide();
      BlockPos targetPos = blockPos.offset(side);

      CatEntity cat = EntityType.CAT.spawnFromItemStack(
         (ServerWorld) world,
         stack,
         player,
         targetPos,
         SpawnReason.SPAWN_EGG,
         true,
         side == Direction.UP
      );

      if (cat == null) {
         return ActionResult.SUCCESS;
      }

      // Ordinary cat behaviour, Luna's own coat.
      cat.setVariant(Luna.LUNA_VARIANT);
      cat.setCustomName(Luna.LUNA_NAME);
      cat.setCustomNameVisible(true);
      try {
        // Cores that model a cat's collar (the core this pack runs on does) also get a
        // pink band drawn around her neck, on top of the shape she already has.
        cat.setCollarColor(Luna.LUNA_COLLAR);
      } catch (Throwable ignore) {
        // Cores without a collar API: Luna still gets her coat and her nameplate.
      }
      world.emitGameEvent(player, GameEvent.ENTITY_PLACE, blockPos);
      stack.decrement(1);

      return ActionResult.CONSUME;
   }
}
