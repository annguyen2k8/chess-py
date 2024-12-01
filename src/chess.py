import pygame as pg

from .classes.inputs.input import *
from .classes.graphics import *

class Game:
    window_size:dict[int, int] = 600, 600
    
    def __init__(self,):
        pg.init()
        pg.font.init()
        pg.mixer.pre_init(44100, -16, 2, 4096)
        pg.display.set_caption("chess-py")
        pg.display.set_icon(Sprite.load("./assets/icon.png"))
        self.screen = pg.display.set_mode(self.window_size)
        self.clock = pg.time.Clock()
        self.input = Input()
    
    def start(self) -> None:
        while True:
            self.input.check_input()
            self.screen.fill("#000000")
            pg.display.update()
            self.clock.tick(60)