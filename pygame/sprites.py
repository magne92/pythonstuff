# Sprite classes for platform game
import pygame as pg
import random
from settings import *
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.life = PLAYER_LIFE

    def update(self):
        self.acc = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if keys[pg.K_UP]:
            self.acc.y = -PLAYER_ACC
        if keys[pg.K_DOWN]:
            self.acc.y = PLAYER_ACC

        # apply friction
        self.acc += self.vel * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.center = self.pos


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        # self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direction = DIRECTIONS[random.randint(0, 3)]
        self.speed = random.randint(ENEMY_MINSPEED,ENEMY_MAXSPEED)
        self.offscreen = True
        if self.direction == "left":
            self.vel.x = -self.speed
            self.pos = vec(WIDTH + 50, random.randint(50, HEIGHT - 50))
        if self.direction == "right":
            self.vel.x = self.speed
            self.pos = vec(-50, random.randint(50, HEIGHT - 50))
        if self.direction == "up":
            self.vel.y = -self.speed
            self.pos = vec(random.randint(50, WIDTH - 50), HEIGHT + 50)
        if self.direction == "down":
            self.vel.y = self.speed
            self.pos = vec(random.randint(50, WIDTH - 50), -50)

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        if self.pos.x < -100 or self.pos.x > WIDTH + 100 or self.pos.y < -100 or self.pos.y > HEIGHT + 100:
            self.kill()
            print("enemy deleted")


class Gear(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((40, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        #self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.pos = vec(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        pass
