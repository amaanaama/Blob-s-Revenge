import pygame
from pygame.locals import *
import random


class LeftEnemy(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('data/assets/left_obs.png')
        self.rect = self.image.get_rect()
        self.start_x = x  # Store initial x-position
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update_position(self):
        self.rect.y += self.speed
        if self.rect.y > 640:
            self.rect.y = -64
            self.rect.x = random.randint(self.start_x - 180, self.start_x - 4)  # Select x-position within the range
            
