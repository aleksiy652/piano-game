import pygame as pg
import pygame.event
import pygame.freetype as pf
import settings
import settings as st
import sounds
import menu

pg.init()
pg.mixer.init(channels=4)


class Game:
    def __init__(self):
        self.window = pg.display.set_mode(st.SIZE)
        self.a = True
        self.song = sounds.Soing(settings.CHRISTMAS_TREE_DURATION, settings.CHRISTMAS_TREE_NOTES)
        self.chasbI = pygame.time.Clock()
        self.counter = 0
        self.win_or_lose = ""
        self.counter_nazhatix = 0
        self.draw_text = pf.Font("shrift.ttf", 50)
        self.ostalosb = 28
        self.menu = menu.Menu(self)
        self.ponyatborneponyatb = 2
        self.vremya_konca = 0
        self.clik_count = 0

    def draw(self):
        self.window.fill([255, 255, 255])
        self.linii()
        self.song.draw(self.window)
        render = self.draw_text.render(f"{self.counter}/{self.song.kolvo_nazhtbix()}/{self.ostalosb}")
        t_pic = render[0]
        rect = render[1]
        rect.center = [100, 50]
        self.window.blit(t_pic, rect)

        if self.win_or_lose != "" and self.song.list[-1].hitbox.y > 600:
            render = self.draw_text.render(str(self.win_or_lose))
            t_pic = render[0]
            rect = render[1]
            rect.center = [200, 300]
            self.window.blit(t_pic, rect)

    def linii(self):
        for i in range(1, st.STOLBI):
            pygame.draw.line(self.window, [0, 0, 0], [st.SHIRINA * i, st.SIZE[1]], [st.SHIRINA * i, 0])

    def update(self):
        self.song.update()
        if len(self.song.namenote) == self.song.nomernot and self.song.list[-1].hitbox.y >= st.SIZE[
            1] and len(self.song.namenote) - self.song.kolvo_nazhtbix() <= 3 and self.win_or_lose == "":
            self.win_or_lose = "Win"
            self.vremya_konca = pygame.time.get_ticks()
        elif len(self.song.namenote) == self.song.nomernot and self.song.list[-1].hitbox.y >= st.SIZE[1] \
                and self.counter >= 3 and self.win_or_lose == "":
            self.win_or_lose = "Lose"
            self.vremya_konca = pygame.time.get_ticks()
        if self.win_or_lose != "" and pg.time.get_ticks() - self.vremya_konca >= 5000:
            self.ponyatborneponyatb = 2

    def events(self):
        event = pygame.event.get()
        for i in event:
            if i.type == pygame.QUIT:
                self.a = False
            if i.type == pygame.MOUSEBUTTONDOWN:
                for j in self.song.list:
                    self.clik_count += 1
                    if j.hitbox.collidepoint(i.pos) and j.nazhta == False:
                        j.cliki()

                        self.clik_count += 1
                        if self.song.praverka_oshibok(j.made_in_math) is True:
                            self.ostalosb -= 1
                        else:
                            self.ostalosb -= 1
                            self.counter += 1
                            self.song.nt_nomernot = j.made_in_math

    def game_while(self):
        while self.a:
            if self.ponyatborneponyatb == 1:
                self.draw()
                self.update()
                self.events()
            else:
                self.menu.draw()
                self.menu.update()
                self.menu.event()
            pygame.display.update()
            self.chasbI.tick(60)


zvuki = Game()
zvuki.game_while()
