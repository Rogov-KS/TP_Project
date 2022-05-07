import configuration as config
import sys
import pygame as pg
from FightCheck import FightCheck


class Check:
    def __init__(self, keeper):
        self.keeper = keeper
        self.check_timer = 0
        self.store = config.store
        self.army_wait = 0
        self.fight_checker = FightCheck(keeper.army_group, keeper.fortress_group)

    def check(self, player, fortress_group, timer):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                config.is_run = False
                pg.quit()
                sys.exit()

        self.fight_checker.check()
        pos = pg.mouse.get_pos()
        for fort in fortress_group:
            fort.reset()

        for fort in fortress_group:

            if pg.mouse.get_pressed()[0] and fort.rect.collidepoint(pos) \
                    and player.in_store == -1 and self.army_wait == 0:
                player.in_store = fort.num()

            if pg.mouse.get_pressed()[0] and fort.rect.collidepoint(pos)\
                    and player.in_store == -1 and self.army_wait == 1:
                self.keeper.create_remember_army()
                self.keeper.get_armies().sprites()[-1].set_target_fort(fort.num())
                self.keeper.get_armies().sprites()[-1].set_target_coordinates(pos_x=fort.pos_x, pos_y=fort.pos_y)
                self.army_wait = 0
                self.keeper.kill_cursor()

            if pg.mouse.get_pressed()[2] and self.army_wait == 1:
                self.army_wait = 0
                self.keeper.kill_cursor()

            if fort.rect.collidepoint(pos) and player.in_store == -1:
                fort.under()

        if player.in_store != -1:
            cur_fort = fortress_group.sprites()[player.in_store]

            if (pg.mouse.get_pressed()[0]) and (timer >= self.check_timer):
                self.check_timer = timer + config.lag
                if self.store.close_rect.collidepoint(pos):
                    player.reset()
                for type_, key in self.store.items.items():
                    if key.button_rect.collidepoint(pos):
                        delta = min(cur_fort.people_amount, int(cur_fort.people_max * 0.1))
                        cur_fort.people_amount -= delta
                        cur_fort.army[type_] += delta

                    if key.button_create_rect.collidepoint(pos):
                        self.keeper.remember_fortress(cur_fort=cur_fort, type_=type_)
                        self.keeper.make_cursor("images/" + type_ + "_icon_" + cur_fort.color + ".png")
                        player.in_store = -1
                        self.army_wait = 1
                        print(key.type)

        return
