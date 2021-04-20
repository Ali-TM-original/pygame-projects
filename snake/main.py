import sys
from random import randint
from random import randrange

import pygame
from pygame import Rect
from pygame.math import Vector2

"""
Mixer imported for Sound  

1>. Creating a Grid by making small squares/ ret will cause issues in separate file
2>. Creating Food for the snake using a dot class
3>. Trying to create Particles
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
        for index, blocks in enumerate(self.body):
            x_pos = int(blocks.x * 48)
            y_pos = int(blocks.y * 48)
            blk = Rect(x_pos, y_pos, 48, 48)
            if index == 0:
                pygame.draw.rect(screen, (255, 0, 0), blk)
            else:
                pygame.draw.rect(screen, (255, 100, 0), blk)

    def move(self):
        body = self.body[:-1]
        body.insert(0, body[0] + self.direction)
        self.body = body[:]

    def add_part(self):
        body = self.body[:]
        body.insert(0, body[0] + self.direction)
        self.body = body[:]

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(6, 10)]
        self.direction = Vector2(1, 0)


class Core:
    def __init__(self):
        self.snake = Body()
        self.dots = Dots()
        self.rain_list = []

    def pls_move_snake(self):
        self.snake.move()
        self.check_collision_dots_snake()
        self.check_collision_body()
        self.check_collision_wall()

    def pls_draw_snake(self):
        self.snake.draw_()

    def pls_draw_dots(self):
        self.dots.draw_dot()

    def check_collision_dots_snake(self):
        """play a sound here"""
        if self.dots.pos == self.snake.body[0]:
            self.dots.random_DOT()
            self.snake.add_part()

        for block in self.snake.body[1:]:
            if block == self.dots.pos:
                self.dots.random_DOT()

    def check_collision_body(self):
        """PLAY A SOUND HERE"""
        for parts in self.snake.body[1:]:
            if parts == self.snake.body[0]:
                self.game_over()

    def check_collision_wall(self):
        """CHANGE DIRECTION"""
        if not 0 <= self.snake.body[0].x < cell_number - 3:
            for index, blocks in enumerate(self.snake.body):
                x_pos = int(blocks.x * 48)
                if x_pos > 800:
                    blocks.x = 0
                if blocks.x < -1.0:
                    blocks.x = 17
            # self.game_over()
        if not 0 <= self.snake.body[0].y < cell_number:  # this is for Y
            for index, blocks in enumerate(self.snake.body):
                y_pos = int(blocks.y * 48)
                if y_pos > 800:
                    blocks.y = 0
                if blocks.y < -1.0:
                    blocks.y = 20

            # self.game_over()

    def game_over(self):
        self.snake.reset()


white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.Font("assets/LazenbyCompSmooth.ttf", 32)

text = font.render('GeeksForGeeks', True, white)
textRect = text.get_rect()

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

    test_score = str(len(core.snake.body) * 10)
    text_ = f"SCORE:{test_score}"
    text = font.render(text_, True, white)
    textRect = text.get_rect()
    # screen.fill((175, 215, 70))
    screen.fill((0, 0, 0))
    screen.blit(text, textRect)
    core.pls_draw_snake()
    core.pls_draw_dots()
    pygame.display.update()
    clock.tick(60)
