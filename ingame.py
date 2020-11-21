import pygame
from pygame.locals import *

import sys
import globe

import pauseGame
import background
import player

class _ingame(object):






    def __init__(self):
        # ? Set ingame_now to on globe
        globe.ingame_now = self
        self.resource = globe.resourceManager

        
        # ? Game border
        globe.gameBorder = Rect(32 , 16 , 384 , 448)

        self.player = player._player()
        self.background = background._background()

        # ? Score
        self.score = 0
        
        # ? Is Pause?
        self.pause = False
    

        # ? Boss yet?
        globe.BOSSING = False

    def stop(self):
        self.pause = True
    def start(self):
        self.pause = False

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # ? Exit throught ALT + F4
                if event.key == pygame.K_F4 and event.mod == pygame.KMOD_LALT:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_ESCAPE:
                    globe.Game.callScene(pauseGame._pause)
        '''
        if self.pause != True:
            self.background.update()
            self.player.update()
            self.item.update()
            self.bullet.update()
            self.enemy.update()

        '''
        if self.pause != True:
            self.background.update()
            self.player.update()



    def draw(self, screen):
        screen.fill((255,255,255))
        
        
        self.background.draw(screen)
        self.player.draw(screen)

