import pygame

pygame.init()

# Create the screen
screen = pygame.display.set_mode((352, 640))
clock = pygame.time.Clock()
running = True

# Title and Icon
pygame.display.set_caption("Blob's Revenge")
icon = pygame.image.load('blob_icon.png')
pygame.display.set_icon(icon)

#Quits the game when the X button is pressed
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #fill screen with black
    screen.fill((0, 0, 0))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
    


