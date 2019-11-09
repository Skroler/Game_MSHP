# здесь подключаются модули
import pygame
import sys
import random
from Snake import Point, Segment, Snake
# здесь определяются константы, классы и функции
FPS = 60

snake = Snake()
# здесь происходит инициация, создание объектов и др.
pygame.init()
surface = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
gameover = False
# если надо до цикла отобразить объекты на экране
pygame.display.update()

# главный цикл
f = 1
while not gameover:
    if f == 1:
        direction = 4
    f = 0
    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        if event.type == pygame.KEYDOWN:
            # 1 вверх 2 вниз 3 влево 4 вправо
            if event.key == pygame.K_RIGHT:
                direction = 4

            if event.key == pygame.K_DOWN:
                direction = 1

            if event.key == pygame.K_LEFT:
                direction = 3

            if event.key == pygame.K_UP:
                direction = 2

            if event.key == pygame.K_d:
                direction = 4

            if event.key == pygame.K_s:
                direction = 1

            if event.key == pygame.K_a:
                direction = 3

            if event.key == pygame.K_w:
                direction = 2
    surface.fill((0,0,0))
    snake.way = direction
    snake.move()
    snake.draw(surface)
    # --------
    # изменение объектов и многое др.
    # --------

    # обновление экранаdss
    pygame.display.update()
sys.exit()