from pygame import key
from pygame import mouse
from pygame import event
from pygame.locals import *

from typing import Tuple

LEFT = 1
RIGHT = 3
MIDDLE = 2

class Input():
    __mouseXY:Tuple[int ,int] = (0, 0)
    
    @property
    def mouseX(self) -> int:
        return self.__mouseXY[0]
    
    @property
    def mouseY(self) -> int:
        return self.__mouseXY[1]
    
    @property
    def mouseXY(self) -> Tuple[int, int]:
        return self.__mouseXY
    
    @mouseXY.setter
    def mouseXY(self, value:Tuple[int, int]) -> int:
        self.__mouseXY = value
    
    @property
    def isLeftMouseButtonPressed(self) -> bool:
        self.check_mouse_pressed(LEFT)
    
    @property
    def isRightMouseButtonPressed(self) -> bool:
        return self.check_mouse_pressed(RIGHT)
    
    @property
    def isMiddleMouseButtonPressed(self) -> bool:
        return self.check_mouse_pressed(MIDDLE)
    
    def __init__(self, game) -> None:
        self.game = game
    
    def check_input(self) -> None:
        self.events = event.get()
        self.check_keyboard()
        self.check_mouse()
        self.check_quit_or_restart()
    
    def check_keyboard(self) -> None:
        keys = key.get_pressed()
    
    def check_mouse(self) -> None:
        self.mouseXY = mouse.get_pos()
    
    def check_quit_or_restart(self) -> None:
        for event in self.events:
            if event.type == QUIT:
                self.game.quit()
            if event.type == KEYDOWN:
                if event.key == K_F1:    
                    self.game.restart()
    
    def check_mouse_pressed(self, button:int) -> bool:
        for event in self.events:
            if event.type == MOUSEBUTTONUP and event.button == button:
                return True
        return False