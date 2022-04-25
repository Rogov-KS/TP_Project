import configuration as config
import sys
import pygame as pg

store = config.store


def check(player, fortress_group):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            config.is_run = False
            pg.quit()
            sys.exit()

    pos = pg.mouse.get_pos()
    for fort in fortress_group:
        if fort.is_under:
            fort.reset()

    for fort in fortress_group:
        if pg.mouse.get_pressed()[0] and fort.rect.collidepoint(pos) and fort.is_friend and player.in_store == -1:
            player.in_store = fort.num()

        if fort.rect.collidepoint(pos):
            fort.under()

    if player.in_store != -1:
        cur_fort = fortress_group.sprites()[player.in_store]

        if pg.mouse.get_pressed()[0]:
            if store.close_rect.collidepoint(pos):
                player.reset()
            for type_, key in store.items.items():
                if key.button_rect.collidepoint(pos):
                    delta = min(cur_fort.people_amount, int(cur_fort.people_max * 0.1))
                    cur_fort.people_amount -= delta
                    cur_fort.army[type_] += delta
                    print(1000000000)

    return
