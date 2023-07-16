import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('data/assets/blob_sprite.png')
        self.rect = self.image.get_rect()

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= 10
        if keys[K_RIGHT]:
            self.rect.x += 10
        if keys[K_UP]:
            self.rect.y -= 10
        if keys[K_DOWN]:
            self.rect.y += 10

        

        