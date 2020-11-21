import pygame
from pygame.locals import *

class _resource(object):

    def __init__(self):
        # ? Contain all file we need / Image / Background
        
        # ? Load Background 
        self.bg_name = [
            "bg_0.png",
            "bg_1.png",
            "bg_2.png",
            "bg_3.png"
        ]

        self.bg = {}
        for i in self.bg_name:
            self.bg[i] = pygame.image.load("data\\bck\\" + i).convert_alpha()

        # ? Load Background stage
        self.bgStage = {}
        self.bgStage["bg_stage.png"] = pygame.image.load("data\\bck\\bg_stage.png").convert_alpha()

        # ? Load Overlay
        self.overlay = {}
        self.overlay["overlay.png"] = pygame.image.load("data\\bck\\overlay.png").convert()
        self.overlay["overlay.png"].set_colorkey((0 ,255 ,0))

        # ? Load SuperSun
        self.superSun_name = [
            "super_sun1.png",
            "super_sun2.png",
            "super_sun3.png",
            "super_sun4.png"
        ]
        self.superSun = {}
        for i in self.superSun_name:
            self.superSun[i] = pygame.image.load("data\\img\\" + i).convert()
            self.superSun[i] = pygame.transform.scale(self.superSun[i], (41, 71))
            self.superSun[i].set_colorkey((255, 255, 255))

        # ? Load menu
        self.ui_name = [
            "cursor_ui.png",        # 0
            "exit_ui.png",          # 1
            "exit_ui_hover.png",    # 2
            "home_ui.png",          # 3
            "setting_ui.png",       # 4
            "setting_ui_less.png",  # 5
            "start_ui.png",         # 6
            "start_ui_less.png"     # 7
        ]
        self.ui = {}
        for i in self.ui_name:
            self.ui[i] = pygame.image.load("data\\menu\\" + i)

        self.ui["start_ui.png"] = pygame.transform.scale(self.ui["start_ui.png"], (191, 76))
        self.ui["start_ui_less.png"] = pygame.transform.scale(self.ui["start_ui_less.png"], (186, 71))
        self.ui["setting_ui.png"] = pygame.transform.scale(self.ui["setting_ui.png"], (200, 72)) # 190 72
        self.ui["setting_ui_less.png"] = pygame.transform.scale(self.ui["setting_ui_less.png"], (200, 72)) # 190 72
        self.ui["exit_ui.png"] = pygame.transform.scale(self.ui["exit_ui.png"], (26, 55)) # 190 72
        self.ui["exit_ui_hover.png"] = pygame.transform.scale(self.ui["exit_ui_hover.png"], (26, 65)) # 190 72
        self.ui["cursor_ui.png"] = pygame.transform.scale(self.ui["cursor_ui.png"], (50, 55)) # 190 72
        self.ui["cursor_ui.png"].set_colorkey((255, 255, 255))

        self.loading_name = [
            "bg_loading.png",
            "left_overlay.png",
            "right_overlay.png",
            "bar.png"
        ]

        self.loading_ui = {}
        for i in self.loading_name:
            self.loading_ui[i] = pygame.image.load("data\\loading\\" + i)

        self.pause_ui = {}
        self.pause_ui["pause_menu.png"] = pygame.image.load("data\\pause\\pause_menu.png").convert()
        self.pause_ui["pause_menu.png"].set_colorkey((255 ,255 ,255))

        self.pause_ui["cursor_menu.png"] = pygame.image.load("data\\pause\\cursor_menu.png").convert()
        self.pause_ui["cursor_menu.png"].set_colorkey((255 ,255 ,255))

        