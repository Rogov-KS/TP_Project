import pygame as pg
import pygame.sprite

from fortresses import Fortress
from army import Army
import random
from cursor import Cursor


class Keeper:

    def __init__(self):
        self.fortress_group = pg.sprite.Group()
        self.army_group = pg.sprite.Group()
        self.cursor_group = pygame.sprite.Group()
        #self.cursor_group.add(self.cursor)
        self.create_fortresses()

    def create_fortresses(self):
        for i in range(9):
            new_fort = Fortress((i % 3) * 800 + 100, (i // 3) * 400 + 100, i, color=("red" if bool(random.randint(0, 1)) else "blue"))
            new_fort.reset()
            self.fortress_group.add(new_fort)

    def remember_fortress(self, cur_fort, type_):
        self.remembered_fort = cur_fort
        self.remembered_fort_type = type_

    def create_remember_army(self):
        self.create_army(pos_x=self.remembered_fort.pos_x, pos_y=self.remembered_fort.pos_y,
                         num=self.remembered_fort.army[self.remembered_fort_type],
                         color=self.remembered_fort.color, type_=self.remembered_fort_type,
                         home_fort=self.remembered_fort.num())
        self.remembered_fort.army[self.remembered_fort_type] = 0

    def create_army(self, pos_x, pos_y, num: int, color: str, type_: str, home_fort: int):
        new_army = Army(pos_x, pos_y, num, color, type_, home_fort)
        self.army_group.add(new_army)

    def get_fortresses(self):
        return self.fortress_group

    def get_armies(self):
        return self.army_group

    def make_cursor(self, cursor_parth):
        cursor = Cursor(cursor_parth)
        self.cursor_group.add(cursor)

    def kill_cursor(self):
        self.cursor_group.empty()
