import pygame as pg
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from classes.graphics import Font

pg.init()
pg.font.init()
screen = pg.display.set_mode((500, 500))
clock = pg.time.Clock()
font = Font.get_font("./test/font/MinecraftRegular-Bmg3.otf", 30)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill("black")
    font.draw(screen, "Hello, World!", (0, 0), True, (255, 255, 255), (100, 255, 100))
    pg.display.update()
    clock.tick(60)