import pygame
from pygame.locals import *

import globe

class _background(object):


    def __init__(self):
        # ? Set ingame_now to on globe
        globe.ingame_now = self
        self.resource = globe.resourceManager

        # ? Background Stage
        self.bg_stage = self.resource.bgStage["bg_stage.png"]
        self.bg_rect = self.bg_stage.get_rect(topleft = (32 , 16))
        self.x_stage = 32;  self.y_stage = 16
        self.stageSpeed = 0.225


    def update(self):
        self.y_stage += self.stageSpeed
        if self.y_stage >= 0:
            self.y_stage = -890

    def draw(self, screen):
        # ? Background / Overlay
        screen.blit(self.bg_stage, (self.x_stage , self.y_stage))
        screen.blit(self.resource.overlay["overlay.png"], (0, 0)) # ? This one overlay
