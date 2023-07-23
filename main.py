import pygame
import math
from pygame.locals import *
from src.Player import Player 
from src.Left_Enemy import LeftEnemy
from src.Right_Enemy import RightEnemy
from src.Button import Button

pygame.init()

#create screen
screen = pygame.display.set_mode((352, 640))
clock = pygame.time.Clock()
running = True
game_over = False
closing_game = False
in_menu = True


#sine movement for menu
sinusoidal_speed = 0.1  
sinusoidal_amplitude = 10  
sinusoidal_offset = 0  


#background
background = pygame.image.load('data/assets/background.png')


#scoreboard
scoreboard = pygame.image.load('data/assets/scoreboard.png')
score = -1
high_score = 0 


#spawn timer
spawn_timer = 0


#title and icon
pygame.display.set_caption("Blob's Revenge")
icon = pygame.image.load('data/assets/blob_icon.png')
pygame.display.set_icon(icon)


#player and enemy objects
P1 = Player(176, 320)
LE = LeftEnemy(0, -64)
RE = RightEnemy(0, -400)


#collision detection
def check_collision():
    global score, running, game_over
    if pygame.sprite.collide_rect(P1, LE) or pygame.sprite.collide_rect(P1, RE):
        running = False
        game_over = True


#game over screen
def game_over_screen():
    global sinusoidal_offset
    font_small = pygame.font.Font('data/assets/04B_25__.TTF', 32)

    screen.fill((0, 0, 0))
    
    
    game_over_text = pygame.image.load('data/assets/gameover.png')
    score_img = pygame.image.load('data/assets/score.png')
    high_score_img = pygame.image.load('data/assets/highscore.png')
    play_again_text = pygame.image.load('data/assets/pressspace.png')
    score_text = font_small.render(f"{score}", True, (255, 255, 255))
    high_score_text = font_small.render(f"{high_score}", True, (255, 255, 255))

    sinusoidal_offset += sinusoidal_speed
    y_offset_menu = int(sinusoidal_amplitude * math.sin(sinusoidal_offset))

    game_over_text_rect = game_over_text.get_rect(center=(screen.get_width() // 2, 140 + y_offset_menu))
    play_again_text_rect = play_again_text.get_rect(center=(screen.get_width() // 2, 450 + y_offset_menu))


    screen.blit(game_over_text, game_over_text_rect)
    screen.blit(score_img, (110-5, 300-30))
    screen.blit(score_text, (230-5, 292-30))
    screen.blit(high_score_img, (75-5, 336-30))
    screen.blit(high_score_text, (275-5, 340-30))
    screen.blit(play_again_text, play_again_text_rect)

    pygame.display.flip()


#main menu screen
def menu_screen():
    global in_menu, sinusoidal_offset
    font_large = pygame.font.Font('data/assets/04B_25__.TTF', 48)

    #load menu image
    menu_text = pygame.image.load('data/menu/blobsrevenge_logo.png')
    menu_text_rect = menu_text.get_rect(center=(screen.get_width() // 2, 250))

    #start button
    start_button = Button(screen.get_width() // 2, 400, 'data/menu/play_button.png', 'data/menu/play_button_pressed.png')

    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        sinusoidal_offset += sinusoidal_speed
        # Apply sinusoidal movement to the logo and start button
        button_y_offset = int(sinusoidal_amplitude * math.sin(sinusoidal_offset))
        menu_text_rect.y = 250 + button_y_offset
        start_button.rect.y = 400 + button_y_offset

        start_button.update()

        if start_button.is_pressed():
            in_menu = False

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        # Render menu text and button
        screen.blit(menu_text, menu_text_rect)
        screen.blit(start_button.image, start_button.rect)
        

        pygame.display.flip()
        clock.tick(60)


#iris wipe transition
def iris_wipe_transition(screen):
    max_radius = int((screen.get_width() ** 2 + screen.get_height() ** 2) ** 0.5)
    for radius in range(0, max_radius, 10):
        pygame.draw.circle(screen, (0, 0, 0), (screen.get_width() // 2, screen.get_height() // 2), radius)
        pygame.display.flip()
        pygame.time.delay(30)  # Add a delay of 30 milliseconds between each frame (adjust as needed)


#reset game to og state
def reset_game():
    global score
    P1.rect.x = 176
    P1.rect.y = 320
    P1.acc = 0.5
    P1.maxVel = 5
    LE.rect.x = 0
    LE.rect.y = -64
    LE.speed = 5
    RE.rect.x = 0
    RE.rect.y = -400
    RE.speed = 5
    score = -1


#main loop - menu part
while in_menu:
    menu_screen()
    if not in_menu:
        break

#main loop - game part
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            closing_game = True

    P1.update_position()

    if LE.rect.y == -64:
        score += 1
    if RE.rect.y == -64:
        score += 1
    if score == 15:
        P1.acc = 0.6
        P1.maxVel = 6
        LE.speed = 6
        RE.speed = 6
    if score == 30:
        P1.acc = 0.7
        P1.maxVel = 7
        LE.speed = 7
        RE.speed = 7
    if score == 45:
        P1.acc = 0.8
        P1.maxVel = 8
        LE.speed = 8
        RE.speed = 8
    if score == 60:
        P1.acc = 0.9
        P1.maxVel = 9
        LE.speed = 9
        RE.speed = 9

    if score > high_score:
        high_score = score
    else:
        high_score = high_score


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

    font = pygame.font.Font('data/assets/04B_25__.TTF', 48)
    text = font.render(str(score), True, (255, 255, 255))
    scoreboard_x = 98
    scoreboard_y = 22
    scoreboard_width = scoreboard.get_width()
    scoreboard_height = scoreboard.get_height()

    text_x = scoreboard_x + (scoreboard_width - text.get_width()) // 2
    text_y = scoreboard_y + (scoreboard_height - text.get_height()) // 2

    screen.blit(text, (text_x, text_y))

    check_collision()

    pygame.display.flip()
    clock.tick(60)

    # Check if the game should end
    if not running and not closing_game:
        iris_wipe_transition(screen)
        game_over = True

    # Game Over Screen Loop
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                closing_game = True
                game_over = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Press SPACE to play again
                    game_over = False
                    running = True
                    reset_game()  # Reset the game state
        if game_over and not closing_game:
            game_over_screen()

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
