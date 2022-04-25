import configuration as config
import sys
import pygame as pg

store = config.store


def draw(screen, background, player, fortress_group):
    screen.blit(background, (0, 0))
    fortress_group.draw(screen)
    if player.in_store != -1:
        store.draw(screen, fortress_group.sprites()[player.in_store])

    pg.display.flip()
