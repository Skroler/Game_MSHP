# здесь подключаются модули
import pygame
from Snake import Point, Segment, Snake
# здесь определяются константы, классы и функции
FPS = 60

snake = Snake()
# здесь происходит инициация, создание объектов и др.
pygame.init()
surface = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# если надо до цикла отобразить объекты на экране
pygame.display.update()

# главный цикл
while True:

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    surface.fill((0,0,0))
    snake.move()
    snake.draw(surface)
    # --------
    # изменение объектов и многое др.
    # --------

    # обновление экрана
    pygame.display.update()