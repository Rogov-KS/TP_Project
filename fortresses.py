import pygame.sprite
import pygame as pg


class Fortress(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, num, im_path, im_path_2, im_path_3, im_path_4, is_enemy: bool):
        super().__init__()
        self.images_ = [pg.image.load(im_path), pg.image.load(im_path_2), pg.image.load(im_path_3), pg.image.load(im_path_4)]
        self.image = self.images_[0]
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.is_under = False
        self.is_friend = not is_enemy
        self.num_ = num
        self.people_amount = 0
        self.people_max = 1000
        self.people_increase = 2
        self.army = {"swordsmen": 0, "pikemen": 0, "horse": 0}

    def rect(self):
        return self.rect()

    def reset(self):
        self.is_under = False
        self.image = self.images_[(not self.is_friend) * 2]
        return

    def under(self):
        self.is_under = True
        self.image = self.images_[(not self.is_friend) * 2 + self.is_under]
        print(9999999)
        return

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        return

    def num(self):
        return self.num_

    def update(self):
        self.people_amount += self.people_increase * 30
        self.people_amount = min(self.people_max, self.people_amount)