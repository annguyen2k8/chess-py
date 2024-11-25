from __future__ import annotations

from pygame import font
from pygame import surface

from typing import Tuple

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
        color:Tuple[int, int, int],
        background:Tuple[int, int, int],
        ) -> None:
        surface.blit(
            self.render(
                text,
                antialias,
                color,
                background
            ),
            pos
        )