import sys

import pygame
from pygame import Rect
from pygame.math import Vector2
from random import randint

"""
Mixer imported for Sound  

1>. Creating a Grid by making small squares/rects will cause issues in separate file
2>. Creating Food for the snake using a dot class
"""

cell_size = 48
cell_number = 20


class Dots:
    def __init__(self):
        """
        Causing Issue sometime the dot spawns half outside the screen
        """
        self.x = randint(0, 18)
        self.y = randint(0, 18)
        self.pos = Vector2(self.x, self.y)

    def draw_dot(self):
        dot_rect = Rect(int(self.pos.x * 48), int(self.pos.y * 48), cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114), dot_rect)


class Body:
    """
    For Movement add Direction vector to all the vectors in self.body
    """

    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10)]

    def draw_(self):
        for blocks in self.body:
            blk = Rect(blocks.x*48, blocks.y*48, 48, 48)
            pygame.draw.rect(screen, (255, 100, 0), blk)

    def move(self, direction: Vector2):
        body = self.body[:-1]
        body.insert(0, body[0] + direction)
        self.body = body


pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

dots = Dots()
snake = Body()

Custom_event = pygame.USEREVENT
pygame.time.set_timer(Custom_event, 120)

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if events.type == Custom_event:
            snake.move(Vector2(0, 1))
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_UP:
                snake.move(Vector2(0, -1))
            if events.key == pygame.K_RIGHT:
                snake.move(Vector2(1, 0))
            if events.key == pygame.K_DOWN:
                snake.move(Vector2(0, 1))
            if events.key == pygame.K_LEFT:
                snake.move(Vector2(-1, 0))

    screen.fill((175, 215, 70))
    dots.draw_dot()
    snake.draw_()
    pygame.display.update()
    clock.tick(60)
