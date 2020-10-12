import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
WIDTH, HEIGHT = 1200, 800
R_MIN, R_MAX = 20, 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

score = 0
FONT = pygame.font.Font(None, 36)
text = FONT.render('Score: ' + str(score), 1, WHITE)
TEXT_POSITION = (0, 0)
screen.blit(text, TEXT_POSITION)


def new_ball():
    """Draw new ball"""
    global x, y, r, v_x, v_y, color
    x = randint(R_MAX, WIDTH - R_MAX)  # x-coordinate of ball's center
    y = randint(R_MAX, HEIGHT - R_MAX)  # y-coordinate of ball's center
    r = randint(R_MIN, R_MAX)  # radius of ball
    v_x = randint(-10, 10)  # projection of ball's velocity to x-axe
    v_y = randint(-10, 10)  # projection of ball's velocity to y-axe
    color = COLORS[randint(0, len(COLORS) - 1)]  # color of ball
    circle(screen, color, (x, y), r)


def click(ev):
    """
    Respond to click
    if position of click is in ball, score will increase by one
    :param ev: object from pygame.event.get()
    """
    global score
    if (ev.pos[0] - x) ** 2 + (ev.pos[1] - y) ** 2 <= r ** 2:
        score += 1


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    new_ball()
    for i in range(15):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click(event)
        if x <= r or x >= WIDTH - r:
            v_x = -v_x
        if y <= r or y >= HEIGHT - r:
            v_y = -v_y
        x += v_x
        y += v_y
        circle(screen, color, (x, y), r)
        text = FONT.render('Score: ' + str(score), 1, WHITE)
        screen.blit(text, TEXT_POSITION)
        pygame.display.update()
        screen.fill(BLACK)

pygame.quit()
