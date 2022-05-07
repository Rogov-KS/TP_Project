import pygame as pg
import configuration as config
import math


class Army(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, num, color, type_, home_fort):
        super().__init__()
        self.images_ = pg.image.load("images/" + type_ + "_icon_" + color + ".png")
        self.image = self.images_
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.is_players = False
        self.num_ = num
        self.initialisation_pos_x = pos_x
        self.initialisation_pos_y = pos_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.target_coordinate_x = pos_x
        self.target_coordinate_y = pos_y
        self.speed = config.speed
        self.color = color
        self.home_fort = home_fort
        if type_ == "horse":
            self.speed = config.horse_speed
        self.type = type_

    def rect(self):
        return self.rect()

    def set_target_fort(self, target: int):
        self.target_fort = target

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        return

    def num(self):
        return self.num_

    def update(self, fortress_group):
        if abs(self.target_coordinate_x - self.pos_x) > abs(self.dx) or \
                abs(self.target_coordinate_y - self.pos_y) > abs(self.dy):
            self.pos_x += self.dx
            self.pos_y += self.dy
        else:
            #self.pos_x = self.initialisation_pos_x
            #self.pos_y = self.initialisation_pos_y
            self.kill()
        self.rect.center = (self.pos_x, self.pos_y)

    def set_target_coordinates(self, pos_x, pos_y):
        self.target_coordinate_x = pos_x
        self.target_coordinate_y = pos_y
        degree = math.atan2(self.target_coordinate_y - self.initialisation_pos_y,
                            self.target_coordinate_x - self.initialisation_pos_x)
        self.dx = math.cos(degree) * self.speed
        self.dy = math.sin(degree) * self.speed
