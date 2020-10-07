# Б02-010 Садыков Даниил
# refactoring by Б02-010 Русских Иван

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))

# colors
white = (230, 230, 255)
light_blue = (64, 234, 255)
black = (0, 0, 0)
light_grey = (234, 245, 234)
light_orange = (255, 157, 122)
grey = (154, 154, 154)
brown = (165, 96, 23)
dark_grey = (50, 50, 50)
green = (156, 208, 19)
yellow = (255, 208, 19)
sepia = (105, 66, 12)
dark_brown = (84, 54, 5)
pink = (255, 157, 155)


def draw_window(x, y, width, height):
    """
    Function that draws window
    :param x: x-coordinate of the left top corner
    :param y: y-coordinate of the left top corner
    :param width: width of window
    :param height: height of window
    """
    rect(screen, white, (x, y, width, height))
    rect(screen, light_blue, (x + width * 0.025, y + height * 0.025, 0.45 * width, 0.45 * height))
    rect(screen, light_blue, (x + width * 0.025, y + height * 0.525, 0.45 * width, 0.45 * height))
    rect(screen, light_blue, (x + width * 0.525, y + height * 0.025, 0.45 * width, 0.45 * height))
    rect(screen, light_blue, (x + width * 0.525, y + height * 0.525, 0.45 * width, 0.45 * height))


def draw_cat(surface, x, y, width, height, body_color, eyes_color, orientation):
    """
    Function that draws a cat
    :param surface: object pygame.Surface
    :param x: x-coordinate of the left top corner
    :param y: y-coordinate of the left top corner
    :param width: width of cat
    :param height: height of cat
    :param body_color: RGB-color of body
    :param eyes_color: RGB-color of eyes
    :param orientation: 'right' or 'left'
    """
    # cat surface
    cat = pygame.Surface((1.2 * width, 1.5 * height))
    cat.fill(sepia)
    cat.set_colorkey(sepia)

    # tail surface
    tail = pygame.Surface((int(0.33 * width), int(0.33 * height)))
    tail.fill(sepia)
    tail.set_colorkey(sepia)
    pygame.draw.ellipse(tail, body_color, (0, 0, int(0.33 * width), int(0.33 * height)))
    pygame.draw.ellipse(tail, black, (0, 0, int(0.33 * width), int(0.33 * height)), 1)
    cat.blit(pygame.transform.rotate(tail, -10), (int(0.7 * width), int(0.44 * height)))  # tail

    ellipse(cat, body_color, (0.33 * width, 0.23 * height, 0.5 * width, 0.9 * height))  # body
    ellipse(cat, black, (0.33 * width, 0.23 * height, 0.5 * width, 0.9 * height), 1)  # body line

    ellipse(cat, body_color, (0.27 * width, 0.63 * height, 0.08 * width, 0.42 * height))  # back paw
    ellipse(cat, black, (0.27 * width, 0.63 * height, 0.08 * width, 0.42 * height), 1)  # back paw line

    ellipse(cat, body_color, (0.34 * width, 0.9 * height, 0.14 * width, 0.27 * height))  # front paw
    ellipse(cat, black, (0.34 * width, 0.9 * height, 0.14 * width, 0.27 * height), 1)  # front paw line

    ellipse(cat, body_color, (0.2 * width, 0.2 * height, 0.24 * width, 0.74 * height))  # head
    ellipse(cat, black, (0.2 * width, 0.2 * height, 0.24 * width, 0.74 * height), 1)  # headline

    ellipse(cat, body_color, (0.68 * width, 0.67 * height, 0.18 * width, 0.57 * height))  # leg base
    ellipse(cat, black, (0.68 * width, 0.67 * height, 0.18 * width, 0.57 * height), 1)  # leg base line

    ellipse(cat, body_color, (0.83 * width, height, 0.07 * width, 0.5 * height))  # leg
    ellipse(cat, black, (0.83 * width, height, 0.07 * width, 0.5 * height), 1)  # leg line

    polygon(cat, body_color, ((0.43 * width, 0.1 * height), (0.41 * width, 0.4 * height),
                              (0.36 * width, 0.25 * height), (0.43 * width, 0.1 * height)))  # right ear
    polygon(cat, black, ((0.43 * width, 0.1 * height), (0.41 * width, 0.4 * height),
                         (0.36 * width, 0.25 * height), (0.43 * width, 0.1 * height)), 1)  # right ear line
    polygon(cat, light_orange,
            ((0.422 * width, 0.145 * height), (0.4 * width, 0.335 * height),
             (0.375 * width, 0.25 * height), (0.422 * width, 0.145 * height)))  # right ear interior

    polygon(cat, body_color, ((0.2 * width, 0.1 * height), (0.22 * width, 0.4 * height),
                              (0.28 * width, 0.25 * height),
                              (0.2 * width, 0.1 * height)))  # left ear
    polygon(cat, black, ((0.2 * width, 0.1 * height), (0.22 * width, 0.4 * height),
                         (0.28 * width, 0.25 * height), (0.2 * width, 0.1 * height)), 1)  # left ear line
    polygon(cat, light_orange,
            ((0.212 * width, 0.15 * height), (0.23 * width, 0.335 * height),
             (0.26 * width, 0.25 * height), (0.212 * width, 0.15 * height)))  # left ear interior

    ellipse(cat, eyes_color,
            (0.24 * width, 0.45 * height, 0.07 * width, 0.24 * height))  # left eye
    ellipse(cat, black,
            (0.27 * width, 0.46 * height, 0.0125 * width, 0.22 * height))  # left eyelid
    ellipse(cat, light_grey,
            (0.246 * width, 0.47 * height, 0.028 * width, 0.1 * height))  # left eye shine

    ellipse(cat, eyes_color,
            (0.34 * width, 0.45 * height, 0.069 * width, 0.24 * height))  # right eye
    ellipse(cat, black,
            (0.373 * width, 0.46 * height, 0.0125 * width, 0.217 * height))  # right eyelid
    ellipse(cat, light_grey,
            (0.35 * width, 0.47 * height, 0.029 * width, 0.1 * height))  # left eye shine

    polygon(cat, pink, ((int(0.306 * width), int(0.7 * height)), (int(0.33 * width), int(0.7 * height)),
                        (int(0.319 * width), int(0.76 * height)), (int(0.306 * width), int(0.7 * height))))  # nose
    aalines(cat, black, True, ((int(0.306 * width - 1), int(0.7 * height)), (int(0.33 * width + 1), int(0.7 * height)),
                               (int(0.319 * width), int(0.76 * height + 1))))  # nose line

    line(cat, black, (int(0.319 * width), int(0.76 * height)),
         (int(0.319 * width), int(0.825 * height)), 1)  # line from nose to mouth
    arc(cat, black, (int(0.319 * width), int(0.77 * height), int(0.023 * width), int(0.08 * height)),
        3.2, 6.28, 1)  # right mouth wing
    arc(cat, black, (int(0.3 * width), int(0.77 * height), int(0.023 * width), int(0.08 * height)),
        3.2, 6.28, 1)  # left mouth wing

    # whiskers
    # right
    arc(cat, black, (0.165 * width, 0.725 * height, 0.56 * width, 2 * height), 1.25, 1.95, 1)
    arc(cat, black, (0.19 * width, 0.665 * height, 0.56 * width, 2 * height), 1.35, 2.03, 1)
    arc(cat, black, (0.14 * width, 0.775 * height, 0.56 * width, 2 * height), 1.15, 1.85, 1)

    # left
    arc(cat, black, (-0.08 * width, 0.725 * height, 0.56 * width, 2 * height), 1.25, 1.95, 1)
    arc(cat, black, (-0.106 * width, 0.665 * height, 0.56 * width, 2 * height), 1.15, 1.85, 1)
    arc(cat, black, (-0.056 * width, 0.775 * height, 0.56 * width, 2 * height), 1.35, 2.05, 1)

    if orientation == 'right':
        cat = pygame.transform.flip(cat, True, False)
    surface.blit(cat, (x, y))


def ball_of_thread(surface, x, y, r, orientation):
    """
    Function that draws ball of threads
    :param surface: object pygame.Surface
    :param x: x-coordinate of the left top corner
    :param y: y-coordinate of the left top corner
    :param r: radius of the ball
    :param orientation: 'right' or 'left'
    """
    ball = pygame.Surface((3 * r, 2 * r))
    ball.set_colorkey(sepia)
    ball.fill(sepia)

    circle(ball, grey, (r, r), r)
    circle(ball, black, (r, r), r, 1)

    arc(ball, black, (0.17 * r, 0.25 * r, 1.9 * r, 1.9 * r), 1.66, 3.14, 1)
    arc(ball, black, (0.35 * r, 0.35 * r, 2 * r, 2 * r), 1.66, 3.14, 1)
    arc(ball, black, (0.45 * r, 0.45 * r, 2 * r, 2 * r), 1.66, 3.14, 1)
    arc(ball, black, (-0.25 * r, 0.5 * r, 2 * r, 2 * r), 0.15, 1.15, 1)
    arc(ball, black, (-0.41 * r, 0.65 * r, 2.1 * r, 2.1 * r), 0.15, 1.15, 1)
    arc(ball, black, (-0.65 * r, 0.85 * r, 2 * r, 2 * r), 0.15, 1.15, 1)

    # thread tail
    arc(ball, grey, (1.33 * r, 1.225 * r, 0.7 * r, 0.7 * r), 4.1888, 5.236, 1)
    arc(ball, grey, (1.68 * r, 1.831 * r, 0.7 * r, 0.7 * r), 1.0472, 2.11, 1)
    arc(ball, grey, (2.03 * r, 1.225 * r, 0.7 * r, 0.7 * r), 4.1888, 5.236, 1)
    arc(ball, grey, (2.38 * r, 1.831 * r, 0.7 * r, 0.7 * r), 1.0472, 2.11, 1)
    arc(ball, grey, (2.73 * r, 1.225 * r, 0.7 * r, 0.7 * r), 4.1888, 5.236, 1)
    arc(ball, grey, (3.08 * r, 1.831 * r, 0.7 * r, 0.7 * r), 1.0472, 2.11, 1)

    if orientation == 'right':
        ball = pygame.transform.flip(ball, True, False)
    surface.blit(ball, (x - r, y - r))


rect(screen, sepia, (0, 400, 600, 400))
rect(screen, dark_brown, (0, 0, 600, 400))

draw_window(400, 35, 250, 330)

draw_window(130, 35, 250, 330)

draw_window(-140, 35, 250, 330)

draw_cat(screen, -30, 400, 400, 120, body_color=brown, eyes_color=green, orientation='left')
draw_cat(screen, 330, 440, 300, 90, body_color=dark_grey, eyes_color=yellow, orientation='left')
draw_cat(screen, 0, 530, 400, 120, body_color=dark_grey, eyes_color=yellow, orientation='right')
draw_cat(screen, 230, 350, 240, 72, body_color=dark_grey, eyes_color=yellow, orientation='right')
draw_cat(screen, 100, 700, 300, 90, body_color=brown, eyes_color=green, orientation='left')
draw_cat(screen, 250, 700, 300, 90, body_color=brown, eyes_color=green, orientation='right')

ball_of_thread(screen, 450, 650, 60, orientation='left')
ball_of_thread(screen, 50, 560, 40, orientation='right')
ball_of_thread(screen, 510, 400, 40, orientation='left')
ball_of_thread(screen, 60, 750, 50, orientation='left')

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
