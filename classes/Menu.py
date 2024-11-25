from pygame import surface

from .Font import *

class Menu:
    def __init__(self, screen:surface.Surface, font:Font) -> None:
        self.screen = screen
        