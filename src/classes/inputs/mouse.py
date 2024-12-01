import pygame as pg

from ..types import *
from ..constants import *

class Mouse:
    def __init__(self, input_):
        self.input = input_
    
    def get_buttondown(self, button:int) -> bool:
        for event in self.input.events:
            if (event.type == MOUSEBUTTONDOWN and event.button == button):
                return True
        return False
    
    def get_buttonup(self, button:int) -> bool:
        for event in self.input.events:
            if (event.type == MOUSEBUTTONUP and event.button == button):
                return True
        return False

    @property
    def x(self) -> int:
        return self.get_pos().x
    
    @property
    def y(self) -> int:
        return self.get_pos().y
    
    def get_pos(self) -> Coordinate:
        return Vector2(pg.mouse.get_pos())