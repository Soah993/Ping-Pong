from pygame import *
from random import choice

mixer.init()
font.init()
fontMain = font.SysFont('Arial', 20)
fontEnd = font.SysFont('Arial', 40)

game = True
finish = False

yr = 25
yl = 25
wR = 0
wL = 0

xb = 335
yb = 235

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_im, sprite_speedx, sprite_speedy, sprite_x, sprite_y, numx, numy):
        super().__init__()
        self.image = transform.scale(image.load(sprite_im), (numx, numy))
        self.xspeed = sprite_speedx
        self.yspeed = sprite_speedy
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
    def reset(self):
        windy31.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def moveL(self, list):
        if list[K_UP] and self.rect.y > 25:
            self.rect.y -= self.yspeed
        if list[K_DOWN] and self.rect.y < 325:
            self.rect.y += self.yspeed
    def moveR(self, list):
        if list[K_w] and self.rect.y > 25:
            self.rect.y -= self.yspeed
        if list[K_s] and self.rect.y < 325:
            self.rect.y += self.yspeed

class Ball(GameSprite):
    def move(self):
        global wR
        global wL
        if self.rect.y <= 20 or self.rect.y >= 450:
            self.yspeed = -self.yspeed
        if sprite.collide_rect(ballPP, playerR) or sprite.collide_rect(ballPP, playerL):
            self.xspeed = -self.xspeed
        if self.rect.x <= 40 or self.rect.x >= 632:
            if self.rect.x <= 50:
                wR += 1
            if self.rect.x >= 632:
                wL += 1
            self.rect.y = 235
            self.rect.x = 335
            self.yspeed = choice([-2, 2])
            self.xspeed = choice([-2, 2])
        self.rect.y += self.yspeed
        self.rect.x += self.xspeed

windy31 = display.set_mode((700, 500))
display.set_caption('Ping Pong')
bg = transform.scale(image.load('table.jpg'), (700, 500))
clock = time.Clock()

playerR = Player('help.png', 3, 3, 20, yr, 25, 150)
playerL = Player('help.png', 3, 3, 655, yl, 25, 150)
ballPP = Ball('ppball.png', choice([-2, 2]), choice([-2, 2]), xb, yb, 30, 30)

winR = fontEnd.render('Игрок СПРАВА победил! !->!', True, (245, 135, 66))
winL = fontEnd.render('!<-! Игрок СЛЕВА победил!', True, (247, 0, 165))

# mixer.music.load('space.ogg')
# mixer.music.play()
# fire = mixer.Sound('fire.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        windy31.blit(bg, (0, 0))
        clock.tick(60)
        keys_pressed = key.get_pressed()

        roundR = fontMain.render('Счёт: '+str(wR), True, (245, 135, 66))
        roundL = fontMain.render('Счёт: '+str(wL), True, (247, 0, 165))
        windy31.blit(roundR, (620, 475))
        windy31.blit(roundL, (20, 0))

        ballPP.reset()
        ballPP.move()

        playerR.moveR(keys_pressed)
        playerR.reset()
        playerL.moveL(keys_pressed)
        playerL.reset()

        if wR == 7:
            windy31.blit(winR, (140, 220))
            finish = True
        if wL == 7:
            windy31.blit(winL, (160, 220))
            finish = True

        display.update()