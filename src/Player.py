import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('data/assets/blob_sprite.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update_position(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] or keys[K_a] and self.rect.x > 0:
            self.rect.x -= 10
        if keys[K_RIGHT] or keys[K_d] and self.rect.x < 352 - 67:
            self.rect.x += 10
        if keys[K_UP] or keys[K_w] and self.rect.y > 0:
            self.rect.y -= 10
        if keys[K_DOWN] or keys[K_s] and self.rect.y < 640 - 67:
            self.rect.y += 10

        

        