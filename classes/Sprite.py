from pygame import image
from pygame import transform

from pygame import Surface

from .Maths import Vector2

class Sprite:
    def __init__(self, image:Surface) -> None:
        self.image = image
        self.rect = image.get_rect()
    
    @staticmethod
    def load(path:str) -> Surface:
        return Sprite(image.load(path))
    
    @staticmethod
    def scale(surface:Surface, size:tuple[int, int]) -> Surface:
        return transform.scale(surface, size)
    
    def draw(self, surface:Surface, pos:Vector2, size: tuple[int, int]) -> None:
        if not size:
            surface.blit(self.img, pos)
        else:
            surface.blit(self.scale(self.img, size), pos)