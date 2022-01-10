import pygame as pg


# vi må laste inn flere bi
STANDING = pg.image.load('standing.png')
STANDING2 = pg.image.load('standing2.png')
STANDING3 = pg.image.load('standing3.png')

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.current_frame = 0   # lag denne variabelen for player spriten
        self.last_update = 0    # denne og

        self.standing = True   # vi må ha varabler som vet om vi springer, står stille, eller hopper feks.
        self.running = False
        self.jumping = False

        # lager en liste over alle bilder som skal vises når vi står stille
        self.standing_frames = [STANDING, STANDING2, STANDING3]


def update(self):
        self.animate()   # kjør animasjon funksjon i starten av update, 
                         # dette sørger for at vi animerer player for hver frame i game loopen
                                                
        # move rect to pos
        self.rect.center = self.pos

        self.standing = True   # denne spriten vil alltid ha True på self.standing, lag kode som endrer denne til false hvis den beveger seg og sett self.running til True


def animate(self):
        now = pg.time.get_ticks()   # på starten av animate henter vi hvilken "tick" eller frame vi er på 1 tick er 1 FPS

        if self.standing:   # vis vi står stille,          
            if now - self.last_update > 350:   # her sørger vi for at vi bytte bilde kun hver 350 tick, lavere tall animerer fortere
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()
           

