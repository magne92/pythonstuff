import pygame as pg
vec = pg.math.Vector2

WIDTH = 1200
HEIGHT = 800
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
FPS = 60
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_LIFE = 200
SCROLLING = 10

pg.init()  # start pygame modul, gjør ved starten av programmet
clock = pg.time.Clock()

myfont = pg.font.SysFont('Comic Sans MS', 30)  # gjør klart en tekst font
screen = pg.display.set_mode((WIDTH, HEIGHT))  # oppretter spillvinduet

# laster klart bildefiler, legg til flere for å ha flere bilder klare til å vises
image = pg.image.load('img/celle.jpg')
image = pg.transform.scale(image, (800, 400))

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite__init__(self)
        self.image = pg.Surface((30, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.pos = vec()
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, 0)
        keys = pg.key.get_pressed()

        if keys[pg.K_UP]:
            self.acc.y = -PLAYER_ACC



Player()
running = True
while running:  # game loop
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:  # sjekker om en knapp er trykket
            if event.key == pg.K_ESCAPE:  # om escape trykkes avsluttes spillet
                running = False


    screen.fill(BLACK)  # overskriver hele vinduet med svart farge

    choice = 0
    pg.display.update()





