from os import path

import pygame as pg

from pygame import image
from pygame import transform
from pygame import Surface

from ..types import *
from ..constants import *
from ..maths.vector import Vector2

class Sprite:
    def __init__(self, file:AnyPath) -> None:
        try:
            self.image = self.load_image(file)
        except FileNotFoundError:
            raise Exception(f"Failed to load {file}")
        self.rect = image.get_rect()
    
    def load_image(self, file:FileArg) -> Surface:
        return Sprite(image.load(file))
    
    def scale(self, surface:Surface, size:Coordinate) -> Surface:
        return transform.scale(surface, size)
    
    def draw(self, surface:Surface, pos:Coordinate, size:Coordinate) -> None:
        if not size:
            surface.blit(self.img, pos)
        else:
            surface.blit(self.scale(self.img, size), pos)
    
    def collidepoint(self, pos:Coordinate) -> bool:
        return self.rect.collidepoint(pos)
    
    def colliderect(self, rect:pg.Rect) -> bool:
        return self.rect.colliderect(rect)
    
    def collidelist(self, rects:List[pg.Rect]) -> bool:
        return self.rect.collidelist(rects)
    
    def collidelistall(self, rects:List[pg.Rect]) -> List[bool]:
        return self.rect.collidelistall(rects)