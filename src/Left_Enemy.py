import pygame
from pygame.locals import *
import math


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('data/assets/left_obs.png')
        self.rect = self.image.get_rect()
        #Enemy spawns at the top of the screen off screen to the left, moves down the screen, once reaches off screen on the bottom, reset y position to top of screen
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update_position(self):
        self.rect.y += self.speed
        if self.rect.y > 640:
            self.rect.y = -64
        #Make enemy move sinuosoidally on the x-axis, reset x position to 0 if it goes off screen
        self.rect.x += 2 * math.sin(self.rect.y / 64)
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 352 - 64:
            self.rect.x = 352 - 64
    
    


