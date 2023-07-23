import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, unpressed_image_path, pressed_image_path):
        super().__init__()
        self.unpressed_image = pygame.image.load(unpressed_image_path)
        self.pressed_image = pygame.image.load(pressed_image_path)
        self.image = self.unpressed_image
        self.rect = self.image.get_rect(center=(x, y))
        self.is_button_pressed = False

    def is_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return pygame.mouse.get_pressed()[0]  # Check if the left mouse button is pressed
        return False

    def update(self):
        if self.is_button_pressed and not self.is_pressed():
            self.is_button_pressed = False

        if self.is_pressed() and not self.is_button_pressed:
            self.is_button_pressed = True
            self.image = self.pressed_image
        elif not self.is_pressed() and self.is_button_pressed:
            self.is_button_pressed = False
            self.image = self.unpressed_image
