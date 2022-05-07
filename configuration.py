import pygame as pg
import Player
import Store

WIDTH = 1920
HEIGHT = 1080
FPS = 30
GAME_NAME = "Age of war"
is_run = True

program_time = 0
updates_in_second = 2
lag = 50
speed = 10
horse_speed = 10

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(GAME_NAME)

player = Player.Player()

store_image = pg.image.load("images/store_background.png")
store_image = pg.transform.scale(store_image, (int(WIDTH * 2 / 3), int(HEIGHT * 4 / 5)))

swordmen_image = pg.image.load("images/button_swordsman.png")
swordmen_image = pg.transform.scale(swordmen_image, (200, 350))
pikeman_image = pg.image.load("images/button_pikeman.png")
pikeman_image = pg.transform.scale(pikeman_image, (200, 350))
horse_image = pg.image.load("images/button_horse.png")
horse_image = pg.transform.scale(horse_image, (200, 350))

close_image = pg.image.load("images/closing_icon.png")
items_imagse = [swordmen_image, pikeman_image, horse_image]

store = Store.Store(back_ground=store_image, closing_image=close_image, items_images=items_imagse)
background = pg.image.load("images/background.jpg")
background = pg.transform.scale(background, (WIDTH, HEIGHT))

FontTitle = pg.font.SysFont("arial", 50)

RED = (255, 0, 0)
BLACK = (0, 0, 0)

damage_bonus = 2