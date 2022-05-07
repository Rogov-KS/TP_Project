import random
import sys
import pygame as pg
import configuration as config
from fortresses import Fortress
import Store
import update
from check import Check
import draw
from keeper import Keeper

player = config.player
clock = pg.time.Clock()
keeper = Keeper()

check = Check(keeper=keeper)
while config.is_run:
    clock.tick(config.FPS)
    # Ввод процесса (события)
    check.check(player=player, fortress_group=keeper.get_fortresses(), timer=pg.time.get_ticks())
    # Обновление
    update.update(fortress_group=keeper.get_fortresses(), army_group=keeper.get_armies(),
                  cursor_group=keeper.cursor_group, timer=pg.time.get_ticks())
    # Визуализация (сборка)
    draw.draw(screen=config.screen, player=player, background=config.background, fortress_group=keeper.get_fortresses(),
              army_group=keeper.get_armies(), cursor_group=keeper.cursor_group)
