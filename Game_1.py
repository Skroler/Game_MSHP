import pygame as pg
import sys
import random as rand
import time

#Инициализация методов
pygame.init()

# задаем размеры экрана
width  = 1290
height = 720

#Цвета
BLACK = (0  ,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0  , 255,   0)
BLUE  = (0  ,   0, 255)

pygame.display.set_mode((width, height))

while 1:
