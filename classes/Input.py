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
    
    @property
    def isLeftMousePressed(self) -> bool:
        return self.check_mouse_pressed(LEFT)
    
    @property
    def isMiddleMousePressed(self) -> bool:
        return self.check_mouse_pressed(MIDDLE)
    
    @property
    def isRightMousePressed(self) -> bool:
        return self.check_mouse_pressed(RIGHT)
    
    def __init__(self, game) -> None:
        self.game = game
    
    def check_input(self) -> None:
        self.events = pg.event.get()
        self.check_keyboard()
        self.check_mouse()
        self.check_quit_or_restart()
    
    def check_keyboard(self) -> None:
        keys = pg.key.get_pressed()
    
    def check_mouse(self) -> None:
        self.mouseXY = pg.mouse.get_pos()
    
    def check_quit_or_restart(self) -> None:
        for event in self.events:
            if event.type == QUIT:
                self.game.quit()
            if event.type == KEYDOWN:
                if event.key == K_F1:    
                    self.game.restart()
    
    def check_mouse_pressed(self, button:Literal[1,2,3]) -> bool:
        for event in self.events:
            if event.type == MOUSEBUTTONDOWN and event.button == button:
                return True
        return False