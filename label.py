import pygame

class Label():

    def __init__(self, image, x, y, window):
        self.label_image = image
        self.window = window
        self.label_rect = self.label_image.get_rect(x = x, y = y)
        self.font = pygame.font.Font("fonts/ROCK.TTF",24)
    def draw(self):
        self.window.blit(self.label_image,(self.label_rect.x, self.label_rect.y))

    def write(self, text):
        msg = self.font.render(text, True,(0, 0, 0))
        self.window.blit(msg, (self.label_rect.x+35, self.label_rect.y+15))