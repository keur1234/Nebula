import pygame
from pygame.locals import *

import sys
import globe
import ingame

class _loading(object):

    def __init__(self):
        self.resource = globe.resourceManager
        self.loading_ui = self.resource.loading_ui
        self.delay = 0



    def update(self):
        
        self.delay += 1
        if self.delay >= 205:
            globe.Game.gotoScene(ingame._ingame)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # ? Exit throught ALT + F4
                if event.key == pygame.K_F4 and event.mod == pygame.KMOD_LALT:
                    pygame.quit()
                    sys.exit()

        

    def draw(self, screen):
        # ? "Loading" background
        screen.blit(self.loading_ui["bg_loading.png"], (0, 0))

        # ? Load bar
        bar_rect = self.loading_ui["bar.png"].get_rect(bottomright = (105 + (self.delay * 2), 265) )
        screen.blit(self.loading_ui["bar.png"], bar_rect)#105 269
        
        # ? Load Overlay
        screen.blit(self.loading_ui["left_overlay.png"], (0, 0))
        screen.blit(self.loading_ui["right_overlay.png"], (517, 236))

        
