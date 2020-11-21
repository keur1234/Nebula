import pygame
from pygame.locals import *

import sys

# ? Global variable [Can access from anywhere]
import globe

# ? Menu
import menu

# ? Resource
import data.resource

class main(object):
    
    def __init__(self):
        # ? System Screen / Resolution
        self.resolution = (640 , 480)
        self.screen = pygame.display.set_mode(self.resolution)
        
        # ? System Clock
        self.clock = pygame.time.Clock()
        self.fps = 144

        # ? System Font 
        self.myFont = pygame.font.SysFont(None , 20)

        # ? System Resource
        globe.resourceManager = data.resource._resource()

        # ? Scene Stack
        self.stackScene = []

        # ? Initialize first scene [Menu, of course.]
        self.gotoScene(menu._menu)

        # ? Does game run?
        globe.RUNNING = True

    def gotoScene(self, sc): # ? Go to next scene without saving previous one
        self.scene = sc()
        self.scene.update()

    def callScene(self, sc): # ? Up scene and pause the current scene
        self.scene.stop()
        self.stackScene.append(self.scene)
        self.scene = sc()

    def back(self): # ? Back to previous scene
        self.scene = self.stackScene.pop()
        self.scene.start()

    def run(self):
        # ? Game Loop
        while globe.RUNNING:
            
            # ? Update Scene / Draw Scene
            self.scene.update()
            self.scene.draw(self.screen)
            
            # ? FPS meter
            img = self.myFont.render("fps:" + str((int)(self.clock.get_fps() * 100) * 1.0 / 100), True , (255, 255, 255))
            rc = img.get_rect()
            rc.bottomright = self.resolution

            # ? Flip screen
            pygame.display.flip()

            # ? Set Frame per second
            self.clock.tick(self.fps)

if __name__ == "__main__":
    pygame.init()

    globe.Game = main()
    globe.Game.run()

    pygame.exit()
    sys.exit()