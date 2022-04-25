import sys
import pygame
import configuration as config
from fortresses import Fortress

class GameState():
    def __init__(self):
        self.state = "main_game"

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.is_run = False
                # pygame.quit()
                sys.exit()
        screen.blit(background, (0, 0))
        fortress_group.draw(screen)
        clock.tick(config.FPS)
        pygame.display.flip()


    def city_window(self):


        clock.tick(config.FPS)
        pygame.display.flip()



pygame.init()
game_state = GameState()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption(config.GAME_NAME)
clock = pygame.time.Clock()
background = pygame.image.load("images/background.jpg")
background = pygame.transform.scale(background, (config.WIDTH, config.HEIGHT))

fortress_group = pygame.sprite.Group()
for i in range(9):
    new_fort = Fortress((i % 3) * 800 + 100, (i // 3) * 400 + 100, "images/red_fortess.png")
    fortress_group.add(new_fort)

while config.is_run:
    game_state.main_game()
    # Ввод процесса (события)
    # Обновление
    # Визуализация (сборка)
