import pygame
from Letter import *
from label import *
import random

class Game():

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Game")

        #bg
        self.bg = pygame.image.load("images/background.png")
        self.bg = pygame.transform.scale(self.bg, (800, 600))

        #letter
        self.letter_lst = []
        self.letter = pygame.image.load("images/letter.png")
        self.letter = pygame.transform.scale(self.letter, (150, 200))

        #label
        label_img = pygame.image.load("images/label.png")
        label_img = pygame.transform.scale(label_img, (250, 75))
        self.label1 =Label(label_img, 10, 0, self.window)
        self.label2 = Label(label_img, 10, 90, self.window)

        #text@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2\fgk
        self.score = 0
        self.time = 30
        self.start_time = pygame.time.get_ticks()
        self.update_chicken_time =  self.start_time
        self.font = pygame.font.Font("fonts/ROCK.TTF", 42)

        h = self.letter.get_height()
        y_center = (self.window.get_height() - h) // 2

        for x in self.letter_x_pos():      #x_list
            self.letter_lst.append(Letter(self.letter, x, y_center, self.window))

    def letter_x_pos(self):
        lst = []
        w = self.letter.get_width()
        h = self.letter.get_height()
        space = self.window.get_width() - (w * 4)
        gap = space // 5
        for i in range(0, 4):
            lst.append(gap + (w + gap)* i)
        return lst


    def run(self):
        running = True

        while running:

            self.window.blit(self.bg,  (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_score(event.pos)

            for letter in self.letter_lst:
                letter.draw()

            self.label1.draw()
            self.label2.draw()
            self.display_text()
            self.update_chicken()
            self.game_over()

            pygame.display.update()
        pygame.quit()

    def display_text(self):
        current_time = pygame.time.get_ticks() #ms
        elapsed_time = (current_time - self.start_time) // 1000
        self.label1.write(f"SCORE:{self.score}")
        self.label2.write(f"TIME:{self.time - elapsed_time}")

    def check_score(self, pos):
        for Letter in self.letter_lst:
            if Letter.letter_rect.collidepoint(pos):
                if Letter.is_chick == True:
                    self.score +=1
                    Letter.is_chick = False

    def update_chicken(self):
        current_time = pygame.time.get_ticks()
        elasped_time = (current_time - self.update_chicken_time) // 1000
        if elasped_time >= 2:
            for letter in self.letter_lst:
                letter.is_chick = False
            rand = random.randint(0,3)
            self.letter_lst[rand].is_chick = True
            self.update_chicken_time = current_time

    def game_over(self):
        current_time = pygame.time.get_ticks()
        if self.score >= 10:
            self.window.fill( (0, 255, 0))
            self.win = self.font.render("WIN!!!", True, (255, 255, 255))
            x_pos = (self.window.get_width() - self.win.get_width()) // 2
            y_pos = (self.window.get_height() - self.win.get_height()) // 2
            self.window.blit(self.win, (x_pos,y_pos))

        if current_time - self.start_time >= self.time * 1000:
            self.window.fill((255, 0, 0))
            self.lost = self.font.render("LOST!!!", True, (255, 255, 255))
            x_post1 = (self.window.get_width() - self.lost.get_width()) // 2
            y_post2 = (self.window.get_height() - self.lost.get_height()) // 2
            self.window.blit(self.lost, (x_post1,y_post2))

game = Game()
game.run()

