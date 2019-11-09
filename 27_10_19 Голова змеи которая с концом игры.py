import pygame as pg
import sys
import random as rand
import math

size = width, height = 1290, 720
black = 0, 0, 0
red = 255, 0, 0


def change_movement(x1, y1, movement):
    vX = 0
    vY = 0
    if (movement == 1):
        vX = 30
        vY = 0
    if (movement == 2):
        vX = 0
        vY = 30
    if (movement == 3):
        vX = -30
        vY = 0
    if (movement == 4):
        vX = 0
        vY = -30

    x1 += vX
    y1 += vY
    return x1, y1

def handler_of_buttons(movement): # обработка нажатия клавиш управления и кнопки выхода
    gameover = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameover = True

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                movement = 1

            if event.key == pg.K_DOWN:
                movement = 2

            if event.key == pg.K_LEFT:
                movement = 3

            if event.key == pg.K_UP:
                movement = 4
    return movement, gameover

def check_on_end(x1, y1): #функция проверки на колизии
    if(x1>1260 or x1<0):
        return 1
    if (y1 > 690 or y1 < 0):
        return 1
    return 0

def end_of_the_game_menu(screen):
    font = pg.font.SysFont('Comic Sans MS', 105, True)
    data = 'GAME OVER'
    ts = font.render(data, False, (255, 0, 0))
    screen.blit(ts, (250, 300))

def main():
    pg.init()
    screen = pg.display.set_mode(size)
    gameover = False

    x1 = 0  # нач координаты левого угла
    y1 = 0  # --

    x2 = 30  # Размеры
    y2 = 30  # --

    vX = 30  # нач скорость по X
    vY = 0  # по Y

    movement = 1  # направление движения значение от 1 до 4 : право, низ, лево, верх

    end = 0
    while not gameover:
            screen.fill(black)

            movement, gameover = handler_of_buttons(movement) # обработка нажатия клавиш управления и кнопки выхода

            if not end: #пока никуда не врезалась змея
                pg.draw.rect(screen, red, (x1, y1, x2, y2), 0)  # отрисовка головы змейки.

            if end: #при проигрыше будет отрисовыватся эта надпись
                end_of_the_game_menu(screen)

            x1, y1 = change_movement(x1, y1, movement) #Функция смены направления движения

            end = check_on_end(x1, y1) #проверка колизий

            pg.display.flip()
            pg.time.wait(100)
    sys.exit()

if __name__ == '__main__':
    main()