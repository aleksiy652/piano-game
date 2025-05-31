import pygame
import settings as st
import random as rnd
import pygame.freetype as pf
import sounds


class Menu:
    def __init__(self, game):
        self.kartinka = pygame.image.load("menu.png")
        self.kartinka = pygame.transform.scale(self.kartinka, st.SIZE)
        self.game = game
        self.draw_ne_text = pf.Font("shrift.ttf", 30)
        self.color = st.WHITE
        self.color2 = st.BLACK
        self.color3 = st.BLACK
        self.counter = 1

    def drawtext(self, color, text, xy):
        render = self.draw_ne_text.render(text, color)
        t_pic = render[0]
        rect = render[1]
        rect.center = xy
        self.game.window.blit(t_pic, rect)

    def draw(self):
        self.game.window.blit(self.kartinka, [0, 0])
        self.drawtext(self.color, "Christmas tree", [200, 150])
        self.drawtext(self.color2, "Birch", [200, 300])
        self.drawtext(self.color3, "Morning", [200, 450])

    def update(self):
        pass

    def event(self):
        event = pygame.event.get()
        for i in event:
            if i.type == pygame.QUIT:
                self.game.a = False
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_UP and self.counter == 1:
                    self.color = st.BLACK
                    self.color3 = st.WHITE
                    self.counter = 3
                elif i.key == pygame.K_UP and self.counter == 2:
                    self.color2 = st.BLACK
                    self.color = st.WHITE
                    self.counter = 1
                elif i.key == pygame.K_UP and self.counter == 3:
                    self.color3 = st.BLACK
                    self.color2 = st.WHITE
                    self.counter = 2
                elif i.key == pygame.K_DOWN and self.counter == 1:
                    self.color = st.BLACK
                    self.color2 = st.WHITE
                    self.counter = 2
                elif i.key == pygame.K_DOWN and self.counter == 2:
                    self.color2 = st.BLACK
                    self.color3 = st.WHITE
                    self.counter = 3
                elif i.key == pygame.K_DOWN and self.counter == 3:
                    self.color3 = st.BLACK
                    self.color = st.WHITE
                    self.counter = 1
                elif i.key == pygame.K_RETURN:
                    self.game.ponyatborneponyatb = 1
                    self.game.song.nomernot = 0
                    self.game.win_or_lose = ""
                    self.game.counter = 0
                    if self.counter == 1:
                        self.game.song = sounds.Soing(st.CHRISTMAS_TREE_DURATION, st.CHRISTMAS_TREE_NOTES)
                    elif self.counter == 2:
                        self.game.song = sounds.Soing(st.BIRCH_DURATION, st.BIRCH_NOTES)
                    else:
                        self.game.song = sounds.Soing(st.MORNING_DURATION, st.MORNING_NOTES)
                    self.game.ostalosb = len(self.game.song.namenote)
