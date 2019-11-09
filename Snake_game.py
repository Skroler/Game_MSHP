import pygame as pg
import sys
import random as rand
import math
import random
from Snake import Counter

size = width, height = 1290, 850
black = 0, 0, 0
red = 255, 0, 0
yellow = 255, 211, 0
blue = 0, 0 , 255


def change_movement(x1, y1, movement):
    vX = 0
    vY = 0
    if (movement == "RIGHT"):
        vX = 30
        vY = 0
    if (movement == "DOWN"):
        vX = 0
        vY = 30
    if (movement == "LEFT"):
        vX = -30
        vY = 0
    if (movement == "UP"):
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
            if event.key == pg.K_RIGHT and movement != "LEFT":
                movement = "RIGHT"

            if event.key == pg.K_DOWN and movement != "UP":
                movement = "DOWN"

            if event.key == pg.K_LEFT and movement != "RIGHT":
                movement = "LEFT"

            if event.key == pg.K_UP and movement != "DOWN":
                movement = "UP"

            if event.key == pg.K_d:
                movement = "RIGHT"

            if event.key == pg.K_s:
                movement = "DOWN"

            if event.key == pg.K_a:
                movement = "LEFT"

            if event.key == pg.K_w:
                movement =  "UP"

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
    screen.blit(ts, (320, 300))

def add_food(food, x_food, y_food, screen, snake_x1, snake_y1, add_point):
    if food == 0:
        koef = 15
        x_food = random.uniform(15, 1275)
        x_food = int(x_food // koef * koef)
        if x_food % 30 == 0:
            x_food += 15
        y_food = random.uniform(15,705)
        y_food = int(y_food // koef* koef)
        if y_food % 30 == 0:
            y_food += 15
        position = [x_food, y_food]
        add_point = True
        food = 1
    else:
        position = [x_food, y_food]
        pg.draw.circle(screen, yellow, position, 15)

    return food, x_food, y_food, add_point

def eat_food(x_food, y_food, snake_x1, snake_y1, score, food, size_x2, size_y2):
    if x_food == snake_x1 + 15 and y_food == snake_y1 + 15:
        food = 0
        score = score + 8


    return score, food, size_x2, size_y2


def main():
    pg.init()
    screen = pg.display.set_mode(size)
    gameover = False

    snake_x1 = 0  # нач координаты левого угла
    snake_y1 = 0  # --

    score = 0

    add_point = False

    size_x2 = 30  # Размеры
    size_y2 = 30  # --

    points = []

    vX = 30  # нач скорость по X
    vY = 0  # по Y

    food = 0
    x_food = 0
    y_food = 0
    movement = "RIGHT"  # направление движения значение от 1 до 4 : право, низ, лево, верх

    end = 0

    # Счетчики
    counter1 = Counter (0)
    # --------

    while not gameover:

            screen.fill(black)

            movement, gameover = handler_of_buttons(movement) # обработка нажатия клавиш управления и кнопки выхода

            score, food, size_x2, size_y2 = eat_food(x_food, y_food, snake_x1, snake_y1, score, food, size_x2, size_y2)
            food, x_food, y_food, add_point = add_food(food, x_food, y_food, screen, snake_x1, snake_y1, add_point)

            counter1.print_text(10, 750, (0, 255, 0), screen) #счетчик

            if add_point == True:
                point = [snake_x1, snake_y1]
                points.insert(0, point)
                counter1.total += 1
            else:
                point = [snake_x1, snake_y1]

            add_point = False

            print("before= ", points)

            for i in range (len(points)-1,0,-1):
                points[i] = points[i-1]

            points[0] = point

            print("after= ", points)

            for i in range (len(points)):
                s = points[i][0]
                s1 = points[i][1]
                pg.draw.rect(screen, red, (s, s1, size_x2, size_y2), 0)

            if not end: #пока никуда не врезалась змея
                pg.draw.rect(screen, red, (snake_x1, snake_y1, size_x2, size_y2), 0)  # отрисовка головы змейки.

            if end: #при проигрыше будет отрисовыватся эта надпись
                end_of_the_game_menu(screen)
                gameover = True



            snake_x1, snake_y1 = change_movement(snake_x1, snake_y1, movement) #Функция смены направления движения

            end = check_on_end(snake_x1, snake_y1) #проверка колизий

            for i in range(len(points) - 2, 0, -1):
                if(points[i][0] == snake_x1 and points[i][1] == snake_y1):
                    end = 1

            pg.draw.rect(screen, blue, (0, 750, 1290, 10), 0)  # отрисовка нижней границы



            pg.display.flip()
            pg.time.wait(100)
            #print (x_food, y_food)
            #print (points)
    sys.exit()

if __name__ == '__main__':
    main()