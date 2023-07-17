import pygame
from src.Player import Player

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
    


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
    


