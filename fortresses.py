import pygame.sprite


class Fortress(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, im_path):
        super().__init__()
        self.image = pygame.image.load(im_path)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)


