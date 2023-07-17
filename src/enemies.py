import pygame
from pygame.locals import *
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.left_image = pygame.image.load("data/assets/left_obs.png")
        self.right_image = pygame.image.load("data/assets/right_obs.png")
        self.image = self.left_image
        self.rect = self.image.get_rect()
        self.rect.y = y

        if x == 0:
            self.rect.x = 0  # Spawn on the left side of the screen
        else:
            self.rect.x = 352 - self.rect.width  # Spawn on the right side of the screen

        self.speed = 5

    def update(self):
        self.rect.y += self.speed

        if self.rect.y > 640:
            self.rect.y = random.randint(-200, -50)

            if self.rect.x == 0:
                self.rect.x = 352 - self.rect.width
            else:
                self.rect.x = 0

        if random.random() < 0.01:
            if self.rect.x == 0:
                self.image = self.right_image
            else:
                self.image = self.left_image
