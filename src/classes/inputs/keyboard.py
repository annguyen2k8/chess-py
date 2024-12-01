import pygame as pg
from ..types import *
from ..constant import *

class Keyboard:
    def __init__(self, input_):
        self.input = input_
    
    def is_pressed(self, key:int) -> bool:
        return pg.key.get_pressed()[key]
    
    def is_keydown(self, key:int) -> bool:
        for event in self.input.events:
            if (event.type == KEYDOWN and event.button == key):
                return True
        return False
    
    def is_keyup(self, key:int) -> bool:
        for event in self.input.events:
            if (event.type == KEYUP and event.button == key):
                return True
        return False