import pygame
from pygame.locals import *
from src.Player import Player 
from src.Left_Enemy import LeftEnemy
from src.Right_Enemy import RightEnemy

pygame.init()

# Create the screen
screen = pygame.display.set_mode((352, 640))
clock = pygame.time.Clock()
running = True
game_over = False

#background
background = pygame.image.load('data/assets/background.png')

#scoreboard
scoreboard = pygame.image.load('data/assets/scoreboard.png')
score = -1 

#spawn timer
spawn_timer = 0

# Title and Icon
pygame.display.set_caption("Blob's Revenge")
icon = pygame.image.load('data/assets/blob_icon.png')
pygame.display.set_icon(icon)

P1 = Player(176, 320)
LE = LeftEnemy(0, -64)
RE = RightEnemy(0, -400)

def check_collision():
    global score, running, game_over
    if pygame.sprite.collide_rect(P1, LE) or pygame.sprite.collide_rect(P1, RE):
        running = False
        game_over = True

def game_over_screen():
    font_large = pygame.font.Font('data/assets/04B_25__.TTF', 48)
    font_small = pygame.font.Font('data/assets/04B_25__.TTF', 32)

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    game_over_text = font_large.render("Game Over", True, (255, 255, 255))
    screen.blit(game_over_text, (80, 250))

    score_text = font_small.render(f"Final Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (110, 320))

    play_again_text = font_small.render("Press SPACE to Play Again", True, (255, 255, 255))
    screen.blit(play_again_text, (35, 400))

    pygame.display.flip()
    

#MAIN GAME LOOP
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    P1.update_position()

    if LE.rect.y == -64:
        score += 1
    if RE.rect.y == -64:
        score += 1

    #fill screen with black
    screen.fill((0, 0, 0))

    #draw sprite from Player.py
    screen.blit(background, (0, 0))
    screen.blit(P1.image, P1.rect)
    
    #draw one instance of Left_Enemy.py
    screen.blit(LE.image, LE.rect)
    LE.update_position()

    screen.blit(RE.image, RE.rect)
    RE.update_position()

    screen.blit(scoreboard, (93, 25))

    font = pygame.font.Font('data/assets/04B_25__.TTF', 32)
    text = font.render(str(score), True, (255, 255, 255))
    screen.blit(text, (180, 30))

    check_collision()

    pygame.display.flip()
    clock.tick(60)

while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Press SPACE to play again
                game_over = False
                running = True
                P1.rect.x = 176
                P1.rect.y = 320
                score = -1

    game_over_screen()
    clock.tick(60)

pygame.quit()
    


