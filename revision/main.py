import sys

import pygame
from pygame import mixer

pygame.init()
pygame.display.set_caption("TEST")

HEIGHT = 800
WIDTH = 600

speed = [1, 1]

screen = pygame.display.set_mode((HEIGHT, WIDTH))
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

mixer.music.load("8bit music cool.mp3")
mixer.music.play(-1)

music_paused = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and music_paused is False:
                music_paused = True
            elif event.key == pygame.K_SPACE and music_paused  is True:
                music_paused = False
        if music_paused:
            mixer.music.pause()
        if not music_paused:
            mixer.music.unpause()

    ballrect = ballrect.move(speed)
    if ballrect.left <= 0 or ballrect.right >= 800:
        speed[0] = -speed[0]

    if ballrect.top <= 0 or ballrect.bottom >= 600:
        speed[1] = -speed[1]

    screen.fill((20, 40, 60, 255))
    screen.blit(ball, ballrect)
    pygame.display.update()
