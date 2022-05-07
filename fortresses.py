import pygame.sprite
import pygame as pg


class Fortress(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, num, color: str):
        super().__init__()
        self.color = color
        self.image = pg.image.load("images/fortress_" + self.color + ".png")
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_under = False
        self.num_ = num
        self.people_amount = 0
        self.people_max = 1000
        self.people_increase = 3
        self.army = {"swordsmen": 0, "pikemen": 0, "horse": 0}

    def rect(self):
        return self.rect()

    def reset(self):
        self.image = pg.image.load("images/fortress_" + self.color + ".png")

    def under(self):
        self.image = pg.image.load("images/fortress_" + self.color + "_enlarged.png")

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        return

    def num(self):
        return self.num_

    def update(self):
        self.people_amount += self.people_increase
        self.people_amount = min(self.people_max, self.people_amount)

    def change_obtainer(self, color: str):
        self.color = color
        self.image = pg.image.load("images/fortress_" + color + ".png")