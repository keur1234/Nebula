import pygame
from pygame.locals import *

import globe

from math import *

class _player(object):
    def __init__(self):
        
        self.resource = globe.resourceManager

        # ? Game border
        self.border = globe.gameBorder
        
        # ? Stat
        self.life = 5;  self.speed = 4
        
        # ? Animation
        self.pl = self.resource.superSun
        self.pl_name = self.resource.superSun_name
        self.pl_frame = 0
        self.delay_pl = pygame.time.get_ticks()

        
        # ? Position
        self.rect = self.pl["super_sun1.png"].get_rect(center = (224 , 450))
        self.x_pl = 224; self.y_pl = 450

    def move(self):
        keys = self.keypressed
        if keys[pygame.K_z]:
            pass

        if keys[pygame.K_x]:
            pass

        if keys[pygame.K_LSHIFT]:
            self.speed = 0.75
        else : self.speed = 4

        if (keys[pygame.K_DOWN] or keys[pygame.K_UP]) and (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
            self.speed /= sqrt(2)

        if keys[pygame.K_UP]: self.y_pl -= self.speed
        if keys[pygame.K_DOWN]: self.y_pl += self.speed

        if keys[pygame.K_LEFT]: self.x_pl -= self.speed 
        if keys[pygame.K_RIGHT]: self.x_pl += self.speed

        self.rect.center = (int(self.x_pl),int(self.y_pl))

        if self.rect.centery < self.border.top:
            self.rect.centery = self.border.top
            self.y_pl = self.rect.centery
        elif self.rect.bottom > self.border.bottom:
            self.rect.bottom = self.border.bottom
            self.y_pl = self.rect.centery

        if self.rect.centerx < self.border.left:
            self.rect.centerx = self.border.left
            self.x_pl = self.rect.centerx
        elif self.rect.centerx > self.border.right:
            self.rect.centerx = self.border.right
            self.x_pl=self.rect.centerx

#        if self.rect.top<100:
#			globe.scgame.itmanager.getitem()

    def update(self):
        # ? Move check
        self.keypressed = pygame.key.get_pressed()
        self.move()

        # ? Game over
        if self.life < 0:
            pass
            #globe.Game.call(gameover._gameover)

        # ? Animation
        now = pygame.time.get_ticks()
        if now - self.delay_pl > 120:
            self.delay_pl = now
            self.pl_frame += 1
            self.pl_frame = self.pl_frame % 4


    def draw(self, screen):
        screen.blit(self.pl[self.pl_name[self.pl_frame]] , self.rect)



# 212 = 231 * 261





