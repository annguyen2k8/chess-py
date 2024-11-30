from pygame import Surface

from .Font import *

class Menu:
    def __init__(self, screen:Surface, font:Font) -> None:
        self.screen = screen
        self.font = font
        