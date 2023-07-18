import pygame
from pygame.locals import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x: y):
        super().__init__()
        self.image = pygame.image.load('data/assets/left_obs.png')
        self.rect = self.image.get_rect()

