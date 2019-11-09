import pygame
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move (self, direction, pixels = 10):
        if direction == 1:
            self.y += pixels
        if direction == 2:
            self.y -= pixels
        if direction == 3:
            self.x -= pixels
        if direction == 4:
            self.x += pixels
    def __str__(self):
        return("point x = " + str(self.x) + " y = " + str(self.y))

class Segment:
    def __init__(self, pnt, width = 10, height = 10, color = (255,0,0)):
        self.point = Point(pnt.x, pnt.y)
        self.width = width
        self.height = height
        self.color = color

    def move (self, direction, pixels = 10):
        if direction == 1:
            self.y += pixels
        if direction == 2:
            self.y -= pixels
        if direction == 3:
            self.x -= pixels
        if direction == 4:
            self.x += pixels

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.point.x, self.point.y, self.width, self.height))

class Snake:
    segments = []
    way = 1 #1 вверх 2 вниз 3 влево 4 вправо
    def __init__(self):
        self.segments.append(Segment(Point(50,50)))

    def draw(self, surface):
        for i in self.segments:
            i.draw(surface)

    def move(self, eating = False):
        new_segment = Segment(self.segments[0].point)
        new_segment.point.move(self.way)
        self.segments = [new_segment] + self.segments

        if not eating:
            self.segments = self.segments[:-1]
