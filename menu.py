import pygame
from pygame.locals import *

import sys
import globe
import loading

class _menu(object):
    
    def __init__(self):
        self.resource = globe.resourceManager
        
        # ? For making background
        self.bg_frame = 0
        self.bg_name = self.resource.bg_name
        self.bg = self.resource.bg
        self.delay_background = pygame.time.get_ticks()
        
        # ? What button you select {0:Start , 1:Setting, 2:Exit}
        self.ui = self.resource.ui; self.x_ui = 383; self.y_ui = 256
        self.selIndex = 0

        # ? Clicked? or not
        self.clicked = False

        # ? Delay scene fading
        self.delay = 0

    def update(self):
        if self.clicked == False:
            now = pygame.time.get_ticks()
            if now - self.delay_background > 120:
                self.delay_background = now
                self.bg_frame += 1
                self.bg_frame = self.bg_frame % 4

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    # ? Exit throught ALT + F4
                    if event.key == pygame.K_F4 and event.mod == pygame.KMOD_LALT:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_UP:
                        self.selIndex -= 1
                        if self.selIndex < 0: self.selIndex = 0
                    elif event.key == K_DOWN:
                        self.selIndex += 1
                        if self.selIndex > 2: self.selIndex = 2
                    if self.selIndex == 0: self.x_ui = 383; self.y_ui = 256
                    elif self.selIndex == 1: self.x_ui = 383; self.y_ui = 337
                    elif self.selIndex == 2: self.x_ui = 545; self.y_ui = 420
                    
                    if event.key == K_z:
                        self.clicked = True
        else:
            self.delay += 1
            if self.delay >= 25 and self.delay < 30:
                if self.selIndex == 2:
                    pygame.quit()
                    sys.exit()
            elif self.delay >= 30:
                if self.selIndex == 0:  
                    globe.Game.gotoScene(loading._loading)
                if self.selIndex == 1:
                    pass


    def draw(self, screen):
        # ? Background
        screen.blit(self.bg[self.bg_name[self.bg_frame]] , (0, 0))
        
        # ? SHOW Start UI
        if self.selIndex == 0: screen.blit(self.ui["start_ui.png"], (430, 237)) # 433 237 Start button
        else : screen.blit(self.ui["start_ui_less.png"], (435, 237))
        
        # ? SHOW Setting UI
        if self.selIndex == 1: screen.blit(self.ui["setting_ui.png"], (427, 325))
        else: screen.blit(self.ui["setting_ui_less.png"], (427, 325))
        
        # ? SHOW Exit UI
        if self.selIndex == 2: screen.blit(self.ui["exit_ui_hover.png"], (590, 415))
        else: screen.blit(self.ui["exit_ui.png"], (590, 415))
        
        # ? SHOW Cursor UI
        screen.blit(self.ui["cursor_ui.png"], (self.x_ui, self.y_ui))
