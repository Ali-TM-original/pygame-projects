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
        self.x = randint(0, 15)
        self.y = randint(0, 15)
        self.pos = Vector2(self.x, self.y)

    def draw_dot(self):
        dot_rect = Rect(int(self.pos.x * 48), int(self.pos.y * 48), cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114), dot_rect)

    def random_DOT(self):
        self.x = randint(0, 15)
        self.y = randint(0, 15)
        self.pos = Vector2(self.x, self.y)


class Body:
    """
    For Movement add Direction vector to all the vectors in self.body
    """

    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10)]
        self.direction = Vector2(1, 0)

    def draw_(self):
        for blocks in self.body:
            x_pos = int(blocks.x * 48)
            y_pos = int(blocks.y * 48)
            blk = Rect(x_pos, y_pos, 48, 48)
            pygame.draw.rect(screen, (255, 100, 0), blk)

    def move(self):
        body = self.body[:-1]
        body.insert(0, body[0] + self.direction)
        self.body = body[:]

    def add_part(self):
        body = self.body[:]
        body.insert(0, body[0] + self.direction)
        self.body = body[:]


class Core:
    def __init__(self):
        self.snake = Body()
        self.dots = Dots()

    def pls_move_snake(self):
        self.snake.move()
        self.check_collison_dots_snake()
        self.check_collision_body()
        self.check_collision_wall()

    def pls_draw_snake(self):
        self.snake.draw_()

    def pls_draw_dots(self):
        self.dots.draw_dot()

    def check_collison_dots_snake(self):
        if self.dots.pos == self.snake.body[0]:
            self.dots.random_DOT()
            self.snake.add_part()

    def check_collision_body(self):
        for parts in self.snake.body[1:]:
            if parts == self.snake.body[0]:
                print("COLLISION")

    def check_collision_wall(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            print("WALL")


pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()


core = Core()

Custom_event = pygame.USEREVENT
pygame.time.set_timer(Custom_event, 120)

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if events.type == Custom_event:
            core.pls_move_snake()

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_UP and core.snake.direction != Vector2(0, 1):
                core.snake.direction = Vector2(0, -1)

            if events.key == pygame.K_DOWN and core.snake.direction != Vector2(0, -1):
                core.snake.direction = Vector2(0, 1)

            if events.key == pygame.K_RIGHT and core.snake.direction != (-1, 0):
                core.snake.direction = Vector2(1, 0)

            if events.key == pygame.K_LEFT and core.snake.direction != Vector2(1, 0):
                core.snake.direction = Vector2(-1, 0)

    screen.fill((0, 0, 0))
    core.pls_draw_snake()
    core.pls_draw_dots()
    pygame.display.update()
    clock.tick(60)
