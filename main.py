import pygame
from pygame.locals import *
from Player import Player
from enemies import Enemy
import random

pygame.init()

# Create the screen
screen = pygame.display.set_mode((352, 640))
clock = pygame.time.Clock()
running = True

#background
background = pygame.image.load('data/assets/background.png')

#scoreboard
scoreboard = pygame.image.load('data/assets/scoreboard.png')

# Title and Icon
pygame.display.set_caption("Blob's Revenge")
icon = pygame.image.load('data/assets/blob_icon.png')
pygame.display.set_icon(icon)

P1 = Player(176, 320)
enemies = pygame.sprite.Group()

#Quits the game when the X button is pressed
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    P1.update_position()

    #fill screen with black
    screen.fill((0, 0, 0))

    #draw sprite from Player.py
    screen.blit(background, (0, 0))
    screen.blit(P1.image, P1.rect)
    screen.blit(scoreboard, (93, 25))

    #draw sprite from Enemies.py
    enemies.update()
    enemies.draw(screen)
    
    spawn_timer += clock.get_rawtime()
    if spawn_timer >= 2:
        spawn_x = random.randint(0, 352 - 50)  # Adjust the range for x position
        new_enemy = Enemy(spawn_x, -50)  # Create a new enemy instance
        enemies.add(new_enemy)  # Add the enemy to the sprite group
        spawn_timer = 0

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
    


