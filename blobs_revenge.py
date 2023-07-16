import pygame

pygame.init()

# Create the screen
screen = pygame.display.set_mode((352, 640))

# Title and Icon
pygame.display.set_caption("Blob's Revenge")
icon = pygame.image.load('blob_icon.png')
pygame.display.set_icon(icon)

#Quits the game when the X button is pressed
while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()


