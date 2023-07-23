import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, unpressed_image_path, pressed_image_path):
        super().__init__()
        self.unpressed_image = pygame.image.load(unpressed_image_path)
        self.pressed_image = pygame.image.load(pressed_image_path)
        self.image = self.unpressed_image
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image = self.pressed_image
        else:
            self.image = self.unpressed_image

    def is_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return pygame.mouse.get_pressed()[0]  # Check if the left mouse button is pressed
        return False
