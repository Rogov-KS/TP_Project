import pygame as pg


class Army(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y, num, color, type):
        super().__init__()
        self.images_ = pg.image.load("images/" + type + "_icon_" + color)
        self.image = self.images_
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.is_under = False
        self.is_players = False
        self.num_ = num
        self.is_clicked = False

    def rect(self):
        return self.rect()

    def reset(self):
        self.is_under = False
        #self.image = self.images_[0]
        return

    def click(self):
        self.is_clicked = not self.is_clicked
        #self.image = self.images_[int(self.is_clicked) * 2]
        return

    def under(self):
        self.is_under = True
        #self.image = self.images_[1]
        return

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        return

    def num(self):
        return self.num_

    #def update(self):
    #    self.people_amount += self.people_increase