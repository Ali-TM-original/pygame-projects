
import sys

import pygame
from pygame import Rect
from pygame.math import Vector2
from random import randint
from pygame import mixer

"""
Mixer imported for Sound  

1>. Creating a Grid by making small squares/rects will cause issues in separate file
2>. Creating Food for the snake using a dot class
"""

class Dots:
    def __init__(self):
        """
        Causing Issue sometime the dot spawns half outside the screen
        """
        self.x = randint(0, 48)
        self.y = randint(0, 20)
        self.pos = Vector2(self.x, self.y)

    def draw(self):
        dot_rect = Rect(int(self.pos.x * 48), int(self.pos.y * 48), 48, 48)
        pygame.draw.rect(screen, (126, 166, 114), dot_rect)
        
        
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill((175, 215, 70))
    pygame.display.update()
    clock.tick(60)
