import pygame as pg
from pygame.locals import *

from ..type import *

# NOTE: Should I split class Input into KeyBoard and Mouse handler?
#       I don't know also I will update it on new update.

class MouseButtonsState:
    def __init__(self, left:bool, middle:bool, right:bool, back:bool, forward:bool):
        self.left = left
        self.middle = middle
        self.right = right
        self.back = back
        self.forward = forward

class MouseButton:
    @staticmethod
    def get_buttons_pressed() -> MouseButtonsState:
        return MouseButtonsState(*pg.mouse.get_pressed(5))
    
    @property
    def isLeftPressed(self) -> bool:
        return self.get_buttons_pressed().left
    
    @property
    def isMiddlePressed(self) -> bool:
        return self.get_buttons_pressed().middle
    
    @property
    def isRightPressed(self) -> bool:
        return self.get_buttons_pressed().right
    
    @property
    def isBackPressed(self) -> bool:
        return self.get_buttons_pressed().back
    
    @property
    def isForwardPressed(self) -> bool:
        return self.get_buttons_pressed().forward

class MousePos:
    @property
    def x(self) -> int:
        return self.get_pos().x
    
    @property
    def y(self) -> int:
        return self.get_pos().y
    
    @staticmethod
    def get_pos() -> Coordinate:
        return Vector2(pg.mouse.get_pos())

class Mouse(MouseButton, MousePos):
    def __init__(self):
        super().__init__()

class Input:
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