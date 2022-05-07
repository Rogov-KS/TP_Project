import time

import check
from Fight import Fight
import pygame as pg
from army import Army
from fortresses import Fortress

class FightCheck:
    # fortreses
    # castles and armies
    # armies
    # only armies
    fight: Fight

    def __init__(self, army_group, fortreses):
        self.fight = Fight()
        self.fortreses = fortreses
        self.armies = army_group

    def check(self):
        for army in self.armies:
            for castle in self.fortreses:
                # if castle.color != army.color and castle.num() == army.target_fort is not None and pg.sprite.collide_rect(army, castle):
                #     print("Fight")
                #     self.fight.fortress_fight(army, castle)
                #
                # if army.target_fort == castle.num_ and castle.color == army.color and castle is not None and \
                #         army.home_fort == castle.num() and pg.sprite.collide_rect(army, castle):  # To do сразу же при создании принимает обратно
                #     self.fight.accept_friend_army(army, castle)

                if army.target_fort == castle.num() and castle is not None and \
                        pg.sprite.collide_rect(army, castle):
                    if army.color == castle.color:
                        self.fight.accept_friend_army(army, castle)
                    else:
                        self.fight.fortress_fight(army, castle)

            for castle in self.armies:
                if army != castle and castle is not None and pg.sprite.collide_rect(army, castle):
                    time.sleep(2)
                    self.fight.army_fight(army, castle)
