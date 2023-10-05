
from pygame import *
from random import *


w_w = 1200
w_h = 900


#
window = display.set_mode((w_w,w_h))
display.set_caption("Пинг-понг")
clock = time.Clock()
fps = 60
bacgroop = transform.scale(image.load("fon.jpg"), (w_w,w_h))








class Gamespite(sprite.Sprite):
    def __init__(self, p_im, p_x,p_y, p_s,s_x, s_y):
        super().__init__()
        self.image = transform.scale(image.load(p_im),(s_x, s_y))
        self.speed = p_s
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
        self.direction = "left"
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(Gamespite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < w_h - 130:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < w_h - 130:
            self.rect.y += self.speed    



Playerok1 = Player("igrok.png",50,300,20, 30,150)

Playerok2 = Player("igrok.png",1100,300,20, 30,150)

mich = Gamespite("bals.png", 600, 450, 20,80,80 )



game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        

    if finish != True:
        window.blit(bacgroop,(0,0))
        Playerok1.reset()
        Playerok1.update1()
        Playerok2.reset()
        Playerok2.update2()
        mich.reset()



        display.update()
        clock.tick(fps)