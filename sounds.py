import pygame
import settings
import random
import pygame.freetype as pf

pygame.init()


class Soing:
    def __init__(self, dlit_not, namenote):
        self.dlitnot = dlit_not
        self.namenote = namenote
        self.nomernot = 0
        self.nt_nomernot = 0
        self.time = 0
        self.time_not = 0
        self.list = []

    def update(self):
        if self.time - self.time_not >= 500 and len(self.namenote) != self.nomernot:
            sadnote = Noti(self.namenote[self.nomernot], self.dlitnot[self.nomernot], self.nomernot)
            self.draw_text = pf.Font("shrift.ttf", 50)
            self.render = self.draw_text.render(str(self.namenote[self.nomernot]))
            self.nomernot += 1
            self.list.append(sadnote)
            self.time_not = pygame.time.get_ticks()
        for i in self.list:
            i.update()
        self.time = pygame.time.get_ticks()

    def draw(self, window):
        for i in self.list:
            draw_text = pf.Font("shrift.ttf", 50)
            t_pic1 = self.render[0]
            rect1 = self.render[1]
            rect1.center = [350, 550]
            window.blit(t_pic1, rect1)
            i.draw(window)

    def praverka_oshibok(self, number):
        true = True
        for i in range(self.nt_nomernot, number):
            if not self.list[i].nazhta:
                true = False
        return true

    def kolvo_nazhtbix(self):
        counter = 0
        for i in self.list:
            if i.nazhta:
                counter += 1
        return counter


class Noti:
    kartinki1 = pygame.image.load("long_tile.png")
    kartinki1 = pygame.transform.scale(kartinki1, [settings.SHIRINA, 300])
    kartinki2 = pygame.image.load("long_tile_pressed.png")
    kartinki2 = pygame.transform.scale(kartinki2, [settings.SHIRINA, 300])
    kartinki3 = pygame.image.load("short_tile.png")
    kartinki3 = pygame.transform.scale(kartinki3, [settings.SHIRINA, 200])
    kartinki4 = pygame.image.load("short_tile_pressed.png")
    kartinki4 = pygame.transform.scale(kartinki4, [settings.SHIRINA, 200])

    def __init__(self, numis, oneortwo, numbirs_notesa):
        self.nazhta = False
        self.made_in_math = numbirs_notesa
        self.oneortwo = oneortwo
        self.nazvanie = numis
        self.zvuk = pygame.mixer.Sound(f"Sounds/{numis}.ogg")
        self.zvuk.set_volume(0.5)
        self.kartinka = Noti.kartinki3 if oneortwo == 1 else Noti.kartinki1
        self.random = random.randrange(0, settings.STOLBI)
        self.hitbox = pygame.rect.Rect([self.random * settings.SHIRINA, -self.kartinka.get_height()],
                                       self.kartinka.get_size())

    def draw(self, window):
        window.blit(self.kartinka, self.hitbox)
        draw_text = pf.Font("shrift.ttf", 50)
        render = draw_text.render(str(self.nazvanie))
        t_pic = render[0]
        rect = render[1]
        rect.center = self.hitbox.center
        window.blit(t_pic, rect)

    def update(self):
        self.hitbox.y += 10

    def cliki(self):
        if self.oneortwo == 1:
            self.kartinka = Noti.kartinki4
        else:
            self.kartinka = Noti.kartinki2
        channel = pygame.mixer.find_channel()
        if channel == None:
            pygame.mixer.stop()
        else:
            channel.queue(self.zvuk)
        self.nazhta = True
        self.zvuk.play()
