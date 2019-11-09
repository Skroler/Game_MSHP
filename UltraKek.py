import pygame as pg
import sys
import random as rand
import math

size = width, height = 1290, 720
black = 0, 0, 0
red = 255, 0, 0


def main():
    pg.init()
    screen = pg.display.set_mode(size)
    gameover = False
    x1 = 0 #нач координаты левого угла
    y1 = 0 #--

    x2 = 30 #Размеры
    y2 = 30 #--

    vX = 30 #нач скорость по X
    vY = 0  #по Y
    while not gameover:
            screen.fill(black)
            for event in pg.event.get():
                    if event.type == pg.QUIT:
                        gameover = True

            pg.draw.rect(screen, red, (x1, y1, x2, y2), 0) #отрисовка головы змейки

            x1 += vX
            y1 += vY


            pg.display.flip()
            pg.time.wait(1000)
    sys.exit()

if __name__ == '__main__':
    main()