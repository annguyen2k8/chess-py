import pygame as pg

# Constant
LEFT = 1
RIGHT = 3

class Input():
    __mouseX:int = 0
    __mouseY:int = 0
    __mouseXY:tuple[int ,int] = (0, 0)
    
    @property
    def mouseX(self) -> int:
        return self.__mouseXY[0]
    
    @property
    def mouseY(self) -> int:
        return self.__mouseXY[1]
    
    @property
    def mouseXY(self) -> tuple[int, int]:
        return self.__mouseXY
    
    @mouseXY.setter
    def mouseXY(self, value:tuple[int, int]) -> int:
        self.__mouseXY = value
    
    def __init__(self, game) -> None:
        self.game = game
    
    def checkInput(self) -> None:
        events = pg.event.get()
        self.checkKeyboardInput(events)
        self.checkMouseInput(events)
        self.checkQuitOrRestart(events)
    
    def checkKeyboardInput(self, events:pg.event.Event) -> None:
        keys = pg.key.get_pressed()
    
    def checkMouseInput(self, events:pg.event.Event) -> None:
        self.mouseXY = pg.mouse.get_pos()
    
    def checkQuitOrRestart(self, events:pg.event.Event) -> None:
        for event in events:
            if event.type == pg.QUIT:
                self.game.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F1:    
                    self.game.restart()
    
    def isLeftMouseButtonPressed(self, events:pg.event.Event) -> bool:
        return self.checkMousePressed(events, LEFT)
    
    def isRightMouseButtonPressed(self, events:pg.event.Event) -> bool:
        return self.checkMousePressed(events, RIGHT)
    
    def checkMousePressed(self, events:pg.event.Event, button:int) -> bool:
        for event in events:
            if event.type == pg.MOUSEBUTTONUP and event.button == button:
                return True
        return False