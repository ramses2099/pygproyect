import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, color, width, height):
   
       pg.sprite.Sprite.__init__(self)

       self.image = pg.Surface([width, height])
       self.image.fill(color)

       self.rect = self.image.get_rect()