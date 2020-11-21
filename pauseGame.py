import pygame
from pygame.locals import *

import sys
import globe

# ? Menu
import menu

class _pause(object):


    def __init__(self):
        self.resource = globe.resourceManager

        # ? Pause menu
        self.pause_ui = self.resource.pause_ui

        # ? What button you select {0:Start , 1:Setting, 2:Exit}
        self.x_cursor = 134; self.y_cursor = 196
        self.selIndex = 0

        # ? Clicked? or not
        self.clicked = False

        self.delay = 0

    def start(self):
        pass
    def stop(self):
        pass

    def update(self):
        if self.clicked == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F4 and event.mod == pygame.KMOD_LALT:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_ESCAPE or event.key == K_x:
                        globe.Game.back()
                    if event.key == K_UP:
                        self.selIndex -= 1
                        if self.selIndex < 0: self.selIndex = 0
                    elif event.key == K_DOWN:
                        self.selIndex += 1
                        if self.selIndex > 2: self.selIndex = 2
                    if self.selIndex == 0: self.x_cursor = 134; self.y_cursor = 196
                    elif self.selIndex == 1: self.x_cursor = 151; self.y_cursor = 221
                    elif self.selIndex == 2: self.x_cursor = 134; self.y_cursor = 247
                    if event.key == K_z:
                        self.clicked = True
        else:
            self.delay += 1
            if self.delay >= 15:
                if self.selIndex == 2:
                    globe.Game.gotoScene(menu._menu)
            elif self.delay >= 5:
                if self.selIndex == 0:
                    globe.Game.back()
                if self.selIndex == 1:
                    globe.ingame_now.__init__()
                    globe.ingame_now.update()
                    globe.Game.back()
                
                

    def draw(self, screen):
        #screen.fill((255,255,255))

        screen.blit(self.pause_ui["pause_menu.png"], (0, 0))
        screen.blit(self.pause_ui["cursor_menu.png"], (self.x_cursor, self.y_cursor))