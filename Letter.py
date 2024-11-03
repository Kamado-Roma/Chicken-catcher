import pygame

class Letter():

    def __init__(self, image, x, y, window):
        self.image = image
        self.window = window
        self.letter_rect = self.image.get_rect(x = x,  y = y)
        self.chick_img = pygame.image.load("images/chicken.png")
        self.is_chick = False

    def draw(self):
        self.window.blit(self.image, (self.letter_rect.x, self.letter_rect.y))
        if self.is_chick == True:
            self.window.blit(self.chick_img, (self.letter_rect.x + (self.letter_rect.w - self.chick_img.get_width())//2, self.letter_rect.y + (self.letter_rect.h - self.chick_img.get_height()) //2))






