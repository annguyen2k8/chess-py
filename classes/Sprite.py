import pygame as pg
from .Maths import Vec2

class Sprite:
    def __init__(self, image:pg.Surface) -> None:
        self.image = image
        self.rect = image.get_rect()
    
    @staticmethod
    def load(path:str) -> pg.Surface:
        return Sprite(pg.image.load(path))
    
    @staticmethod
    def scale(surface:pg.Surface, size:tuple[int, int]) -> pg.Surface:
        return pg.transform.scale(surface, size)
    
    def draw(self, surface:pg.Surface, pos:Vec2, size: tuple[int, int]) -> None:
        if not size:
            surface.blit(self.img, pos)
        else:
            surface.blit(self.scale(self.img, size), pos)