from __future__ import annotations

from pygame import font
from pygame import surface
from pygame.draw import rect

from .Maths import Vector2

class Font(font.Font):
    @staticmethod
    def get_font(name:str, size:int) -> Font:
        return Font(name, size)
    
    def draw(
        self, 
        surface:surface.Surface,
        text:str,
        pos:Vector2,
        antialias:bool,
        color:tuple[int, int, int],
        background:tuple[int, int, int],
        ) -> None:
        ...