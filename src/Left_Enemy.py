import pygame
from pygame.locals import *
import random
import math

class LeftEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('data/assets/left_obs.png')
        self.rect = self.image.get_rect()
        self.start_x = x  # Store initial x-position
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.amp = 10
        self.freq = 0.009

    def update_position(self):
        
        self.rect.y += self.speed
        if self.rect.y > 640:
            self.rect.y = -64
            self.rect.x = random.randint(0 - 180, 0 - 4)  # Select x-position within the range
            
