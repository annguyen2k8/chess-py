import sys
import pygame as pg

from .mouse import *
from .keyboard import *
from ..types import *
from ..constant import *

# NOTE: Should I split class Input into KeyBoard and Mouse handler?
#       I don't know also I will update it on new update

class Input:
    events:List[Event]
    def __init__(self):
        self.mouse = Mouse(self)
    
    def check_input(self) -> None:
        self.events = pg.event.get()
        self.check_quit()
    
    def check_quit(self) -> None:
        for event in self.events:
            if event.type == QUIT:
                pg.quit()
                sys.exit()