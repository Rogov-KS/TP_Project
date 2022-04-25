import random
import sys
import pygame as pg
import configuration as config
from fortresses import Fortress
import Store
import update
import check
import draw

player = config.player
clock = pg.time.Clock()
background = pg.image.load("images/background.jpg")
background = pg.transform.scale(background, (config.WIDTH, config.HEIGHT))


fortress_group = pg.sprite.Group()
for i in range(9):
    new_fort = Fortress((i % 3) * 800 + 100, (i // 3) * 400 + 100, i, "images/fortess_red.png", "images/fortess_red_enlarged.png", "images/fortress_blue.png", "images/fortress_blue_enlarged.png", is_enemy=random.randint(0, 1))
    new_fort.reset()
    fortress_group.add(new_fort)

while config.is_run:
    clock.tick(config.FPS)
    # Ввод процесса (события)
    check.check(player=player, fortress_group=fortress_group)
    # Обновление
    update.update(fortress_group=fortress_group, timer=pg.time.get_ticks())
    # Визуализация (сборка)
    draw.draw(screen=config.screen, player=player, background=background, fortress_group=fortress_group)
