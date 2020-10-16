# Б02-010 Русских Иван

import pygame
from pygame.draw import *
from random import randint
pygame.init()


class Ball:
    """
    Class of balls moving on screen
    """
    def __init__(self, x, y, r, v_x, v_y, color, lifetime):
        self.x = x  # x-coordinate of ball's center
        self.y = y  # y-coordinate of ball's center
        self.r = r  # radius of ball
        self.v_x = v_x  # projection of ball's velocity to x-axe
        self.v_y = v_y  # projection of ball's velocity to y-axe
        self.color = color  # color of ball
        self.lifetime = lifetime  # lifetime of ball


FPS = 24  # frames per second
WIDTH, HEIGHT = 1200, 800  # width and height of window
R_MIN, R_MAX = 20, 100  # minimal and maximal radius of ball

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# colors
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
# label with score
FONT = pygame.font.Font(None, 36)
text = FONT.render('Score: ' + str(score), 1, WHITE)
TEXT_POSITION = (0, 0)
screen.blit(text, TEXT_POSITION)


def new_ball(balls):
    """Create new ball"""
    x = randint(R_MAX, WIDTH - R_MAX)  # x-coordinate of ball's center
    y = randint(R_MAX, HEIGHT - R_MAX)  # y-coordinate of ball's center
    r = randint(R_MIN, R_MAX)  # radius of ball
    v_x = randint(-10, 10)  # projection of ball's velocity to x-axe
    v_y = randint(-10, 10)  # projection of ball's velocity to y-axe
    color = COLORS[randint(0, len(COLORS) - 1)]  # color of ball
    lifetime = randint(2, 5)  # lifetime of the ball
    balls.append(Ball(x, y, r, v_x, v_y, color, lifetime))
    circle(screen, color, (x, y), r)


def draw_ball(ball):
    """Draw ball on the screen"""
    surf = pygame.Surface((2 * ball.r, 2 * ball.r))
    surf.fill(BLACK)
    surf.set_colorkey(BLACK)
    circle(surf, ball.color, (ball.r, ball.r), ball.r)
    screen.blit(surf, (ball.x - ball.r, ball.y - ball.r))


def click(ev):
    """
    Respond to click
    if position of click is in ball, score will increase by one
    :param ev: object from pygame.event.get()
    """
    global score
    for ball in balls:
        if (ev.pos[0] - ball.x) ** 2 + (ev.pos[1] - ball.y) ** 2 <= ball.r ** 2:
            score += 1
            balls.remove(ball)


balls = []
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    new_ball(balls)
    for i in range(FPS // 2):
        clock.tick(FPS)
        # handling of events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click(event)

        # changing position of events
        for ball in balls:
            if ball.x <= ball.r:
                ball.v_x = randint(1, 10)
                ball.v_y = randint(-10, 10)
            elif ball.x >= WIDTH - ball.r:
                ball.v_x = randint(-10, -4)
                ball.v_y = randint(-10, 10)
            if ball.y <= ball.r:
                ball.v_y = randint(4, 12)
                ball.v_x = randint(-10, 10)
            elif ball.y >= HEIGHT - ball.r:
                ball.v_y = randint(-12, -4)
                ball.v_x = randint(-10, 10)
            ball.x += ball.v_x
            ball.y += ball.v_y
            draw_ball(ball)

        # changing number of scores on the screen
        text = FONT.render('Score: ' + str(score), 1, WHITE)
        screen.blit(text, TEXT_POSITION)

        pygame.display.update()
        screen.fill(BLACK)

    # changing lifetime of balls
    for ball in balls:
        ball.lifetime -= 1
        if ball.lifetime <= 0:
            balls.remove(ball)

pygame.quit()
