import pygame as pg
from pygame.locals import *

from .Type import *

# NOTE: Should I split class Input into KeyBoard and Mouse handler?
#       I don't know also I will update it on new update.

LEFT = 1
MIDDLE = 2
RIGHT = 3

class Input:
    @property
    def mouseX(self) -> int:
        return self.mouseXY.x
    
    @property
    def mouseY(self) -> int:
        return self.mouseXY.y
    
    @property
    def mouseXY(self) -> Tuple[int, int]:
        return Vector2(pg.mouse.get_pos())
    
    @staticmethod
    def get_mouse_pressed(num_buttons:Literal[5, 3]=5) -> bool:
        return pg.mouse.get_pressed(num_buttons)
    
    @property
    def isLeftMousePressed(self) -> bool:
        return self.get_mouse_pressed()[0]
    
    @property
    def isMiddleMousePressed(self) -> bool:
        return self.get_mouse_pressed()[1]
    
    @property
    def isRightMousePressed(self) -> bool:
        return self.get_mouse_pressed()[2]
    
    @property
    def isBackMousePressed(self) -> bool:
        return self.get_mouse_pressed()[3]
    
    @property
    def isForwardMousePressed(self) -> bool:
        return self.get_mouse_pressed()[4]
    
    def __init__(self, game) -> None:
        self.game = game
    
    def check_input(self) -> None:
        self.check_keyboard()
        self.check_quit_or_restart()
    
    def check_keyboard(self) -> None:
        keys = pg.key.get_pressed()
    
    def check_quit_or_restart(self) -> None:
        for event in pg.event.get():
            if event.type == QUIT:
                self.game.quit()
            if event.type == KEYDOWN:
                if event.key == K_F1:    
                    self.game.restart()
    
