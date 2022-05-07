import pygame as pg
import configuration as config


class Player:
    def __init__(self):
        self.in_store = -1

    def set_store(self, ind: int):
        self.in_store = ind

    def reset(self):
        self.in_store = -1