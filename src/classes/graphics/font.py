from __future__ import annotations

import pygame as pg
from pygame import font
from pygame import Surface

from ..type import *
from ..maths.vector import Vector2

class Font(font.Font):
    @staticmethod
    def get_font(name:str, size:int) -> Font:
        return Font(name, size)
    
    def draw(
            self, 
            surface:Surface,
            text:str|bytes|None,
            pos:Coordinate,
            antialias:bool|Literal[0,1],
            color:Optional[ColorValue],
            background:Optional[ColorValue],
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