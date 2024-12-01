import sys
import pygame as pg

pg.init()
pg.display.set_mode((500, 500))
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    print(pg.key.get_pressed()[pg.K_RETURN])
    pg.display.update()
    clock.tick(60)