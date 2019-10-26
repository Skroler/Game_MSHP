import pygame as pg
import sys
import random
import math

size = width, height = 1024, 768
black = 0, 0, 0


def main():
    pg.init()
    screen = pg.display.set_mode(size)
    gameover = False
    alpha  = 0
    x = 10
    y = 10
    kek = 0

    while not gameover:

            for event in pg.event.get():
                    if event.type == pg.QUIT:
                        gameover = True

                    if(kek == 0):
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_LEFT:
                                x -= 30

                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_RIGHT:
                                x += 30

                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_DOWN:
                                y += 30

                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_UP:
                                y -= 30
            if y > 600 :
                kek = 1


            screen.fill(black)
            plane = pg.image.load("plane.png")
            plane = pg.transform.scale(plane, (width//5, height//5))
            planerect = plane.get_rect()
            planerect.x = x
            planerect.y = y
            #alpha -= 0.05
            screen.blit(plane, planerect)
            if kek == 1:
                font = pg.font.SysFont('Comic Sans MS', 105, True)
                data = '11.09.2001'
                ts = font.render(data, False, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
                screen.blit(ts, (250, 300))

            pg.display.flip()

            pg.time.wait(10)
    sys.exit()

if __name__ == '__main__':
    main()