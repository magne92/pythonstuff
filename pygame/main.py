import pygame as pg
import random
from settings import *
from sprites import *


class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.myfont = pg.font.SysFont('Comic Sans MS', 30)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))

        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.newgame = False

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player()
        self.enemy = Enemy()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.enemy)

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.spawn()
        # Game Loop - Update
        self.all_sprites.update()

        hits = pg.sprite.spritecollide(self.player, self.enemies, True)
        if hits:
            self.player.life -= 10

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
        if self.player.life == 0:
            self.playing = False

    def spawn(self):
        if len(self.enemies) < MAX_ENEMIES:
            self.enemy = Enemy()
            self.all_sprites.add(self.enemy)
            self.enemies.add(self.enemy)

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.lifetext = self.myfont.render(str(self.player.life), False, GREEN)
        self.screen.blit(self.lifetext, (WIDTH-50, 0))

        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        self.gameovertext = self.myfont.render("GAME OVER", False, GREEN)
        self.screen.blit(self.gameovertext, (WIDTH / 2-100, HEIGHT / 2))

        self.playagaintext = self.myfont.render("Press enter to play again", False, GREEN)
        self.screen.blit(self.playagaintext, (WIDTH / 2 - 100, HEIGHT / 2 + 100))
        pg.display.flip()

        pg.event.clear()
        gameover = True
        while gameover:
            for event in pg.event.get():
                # check for closing window
                if event.type == pg.QUIT:
                    if self.playing:
                        self.playing = False
                    self.running = False
                    gameover = False

                keys = pg.key.get_pressed()
                if keys[pg.K_RETURN] or keys[pg.K_KP_ENTER]:
                    self.newgame = True
                    gameover = False

        if self.newgame:
            g.new()


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.run()
    g.show_go_screen()

pg.quit()
