from pygame import image
from pygame import transform
from pygame import surface
from pygame import rect

from typing import Tuple
from typing import List

from .Maths import Vector2

class Sprite:
    def __init__(self, image:surface.Surface) -> None:
        self.image = image
        self.rect = image.get_rect()
    
    @staticmethod
    def load(path:str) -> surface.Surface:
        return Sprite(image.load(path))
    
    @staticmethod
    def scale(surface:surface.Surface, size:Tuple[int, int]) -> surface.Surface:
        return transform.scale(surface, size)
    
    def draw(self, surface:surface.Surface, pos:Vector2, size: Tuple[int, int]) -> None:
        if not size:
            surface.blit(self.img, pos)
        else:
            surface.blit(self.scale(self.img, size), pos)
    
    def collidepoint(self, pos:Vector2) -> bool:
        return self.rect.collidepoint(pos)
    
    def colliderect(self, rect:rect.Rect) -> bool:
        return self.rect.colliderect(rect)
    
    def collidelist(self, rects:List[rect.Rect]) -> bool:
        return self.rect.collidelist(rects)
    
    def collidelistall(self, rects:List[rect.Rect]) -> List[bool]:
        return self.rect.collidelistall(rects)