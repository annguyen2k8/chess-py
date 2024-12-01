import pygame as pg

from classes.Input import *

class Game:
    window_size:dict[int, int] = 600, 600
    max_fps:int = 60
    
    def __init__(self):
        pg.init()
        pg.font.init()
        pg.mixer.pre_init(44100, -16, 2, 4096)
        self.screen = pg.display.set_mode(self.window_size)
        self.clock = pg.time.Clock()
        self.input = Input(self)
        self.isRestart = True
        self.isExitLoop = False
    
    def loop(self) -> None:
        while not self.isExitLoop:
            self.input.check_input()
            self.screen.fill("#000000")
            pg.display.update()
            self.clock.tick(self.max_fps)
    
    def quit(self) -> None:
        self.isExitLoop = True
        self.isRestart = False
    
    def restart(self) -> None:
        self.isExitLoop = True
    
    def main(self) -> None:
        while self.isRestart:
            self.__init__()
            self.loop()

if __name__ == '__main__':
    game = Game()
    game.main()