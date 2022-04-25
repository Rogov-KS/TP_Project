import pygame as pg
import configuration as config


def make_title_from_text(text, font_title, rect):
    score_title = font_title.render(
        text, True, config.BLACK)
    score_rect = score_title.get_rect()
    score_rect = rect
    return score_title, score_rect


def make_people_am_title(font_title, am, max_am, rect):
    text = f"Aviable {am}/{max_am}"
    return make_title_from_text(text=text, font_title=font_title, rect=rect)


def make_cur_amount(font_title, am, rect):
    text = f"{am}"
    return make_title_from_text(text, font_title, rect)


class Item(pg.sprite.Sprite):
    def __init__(self, image, store_rect, ind, type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect = (self.rect.midleft[0] + (int(config.WIDTH * 5 / 21) * ind + 300) + 50, self.rect.midleft[1])

        self.amount = 0
        self.type = type
        self.button_image = pg.image.load("images/button_background.png")
        self.button_image = pg.transform.scale(self.button_image, (200, 50))
        self.button_rect = self.button_image.get_rect()
        self.button_rect.topleft = (self.rect[0], self.rect[1] + int(config.HEIGHT * 5 / 14))
        # self.button_rect = self.button_image.get_rect()

    def draw(self, screen, amount):
        screen.blit(self.image, self.rect)
        screen.blit(self.button_image, self.button_rect)
        text_rect = (self.rect[0] + 80, self.rect[1] - 30)
        # text_rect = self.image.get_rect().midtop
        screen.blit(*make_cur_amount(font_title=config.FontTitle, am=amount, rect=text_rect))

    def set_amount(self, am):
        self.amount = am


class Store(pg.sprite.Sprite):
    def __init__(self, back_ground, closing_image, items_images):
        super().__init__()
        self.image = back_ground
        self.rect = self.image.get_rect()
        self.rect.center = (config.WIDTH / 2, config.HEIGHT / 2)
        self.close_image = closing_image
        self.close_rect = self.close_image.get_rect()
        self.close_rect.topright = self.rect.topright

        sword_item = Item(items_images[0], self.rect, ind=0, type="swordsmen")
        pike_item = Item(items_images[1], self.rect, ind=1, type="pikemen")
        horse_item = Item(items_images[2], self.rect, ind=2, type="horse")
        self.items = {"swordsmen": sword_item, "pikemen": pike_item, "horse": horse_item}

    def draw(self, screen, fort):
        screen.blit(self.image, self.rect)
        screen.blit(self.close_image, self.close_rect)
        text_rect = self.rect.bottomleft
        text_rect = (text_rect[0], text_rect[1] - 50)
        screen.blit(*make_people_am_title(font_title=config.FontTitle, rect=text_rect, am=fort.people_amount,
                                          max_am=fort.people_max))
        for item in self.items.values():
            item.draw(screen, fort.army[item.type])
