import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('data/assets/blob_sprite.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velX = 0
        self.velY = 0
        self.acc = 0.5
        self.friction = 0.2
        self.maxVel = 5

    def update_position(self):
        keys = pygame.key.get_pressed()

        
        if (keys[K_LEFT] or keys[K_a]) and self.velX > -self.maxVel:
            self.velX -= self.acc
        if (keys[K_RIGHT] or keys[K_d]) and self.velX < self.maxVel:
            self.velX += self.acc
        if (keys[K_UP] or keys[K_w]) and self.velY > -self.maxVel:
            self.velY -= self.acc
        if (keys[K_DOWN] or keys[K_s]) and self.velY < self.maxVel:
            self.velY += self.acc

        
        if not (keys[K_LEFT] or keys[K_RIGHT]) and not (keys[K_a] or keys[K_d]):
            if self.velX < 0:
                self.velX += self.friction
            elif self.velX > 0:
                self.velX -= self.friction
        if not (keys[K_UP] or keys[K_DOWN]) and not (keys[K_w] or keys[K_s]):
            if self.velY < 0:
                self.velY += self.friction
            elif self.velY > 0:
                self.velY -= self.friction

        
        self.rect.x += self.velX
        self.rect.y += self.velY

        
        self.rect.x = max(0, min(self.rect.x, 352 - 52))
        self.rect.y = max(0, min(self.rect.y, 640 - 52))
