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
    rect(screen, white, (x, y, width, height))
    rect(screen, light_blue, (x + width * 0.025, y + height * 0.025, 0.45 * width, 0.45 * height))
    rect(screen, light_blue, (x + width * 0.025, y + height * 0.525, 0.45 * width, 0.45 * height))
    rect(screen, light_blue, (x + width * 0.525, y + height * 0.025, 0.45 * width, 0.45 * height))
    rect(screen, light_blue, (x + width * 0.525, y + height * 0.525, 0.45 * width, 0.45 * height))


def draw_cat(surface, x, y, width, height, body_color, eyes_color, orientation):
    # cat surface
    cat = pygame.Surface((width, 1.5 * height))
    cat.fill(sepia)
    cat.set_colorkey(sepia)

    # tail surface
    tail = pygame.Surface((width / 3, height / 3))
    tail.fill(sepia)
    tail.set_colorkey(sepia)
    pygame.draw.ellipse(tail, body_color, (0, 0, width / 3, height / 3))
    pygame.draw.ellipse(tail, black, (0, 0, width / 3, height / 3), 1)
    cat.blit(pygame.transform.rotate(tail, -10), (width / 2, 0.44 * height))  # tail

    ellipse(cat, body_color, [width / 8, height / 30 + 0.2 * height, width / 2, 0.9 * height])  # body
    ellipse(cat, black, [width / 8, height / 30 + 0.2 * height, width / 2, 0.9 * height], 1)  # body line

    ellipse(cat, body_color, [width / 15, 0.63 * height, width / 12, height / 2.4])  # back paw
    ellipse(cat, black, [width / 15, 0.63 * height, width / 12, height / 2.4], 1)  # back paw line

    ellipse(cat, body_color, [width / 7, 0.9 * height, width / 7, height / 3.6])  # front paw
    ellipse(cat, black, [width / 7, 0.9 * height, width / 7, height / 3.6], 1)  # front paw line

    ellipse(cat, body_color, [0, 0.2 * height, width / 4.2, height / 1.35])  # head
    ellipse(cat, black, [0, 0.2 * height, width / 4.2, height / 1.35], 1)  # headline

    ellipse(cat, body_color, [width / 2.1, 0.67 * height, width / 5.5, height / 1.75])  # leg base
    ellipse(cat, black, [width / 2.1, 0.67 * height, width / 5.5, height / 1.75], 1)  # leg base line

    ellipse(cat, body_color, [width / 1.59, height, width / 15, height / 2])  # leg
    ellipse(cat, black, [width / 1.59, height, width / 15, height / 2], 1)  # leg line

    polygon(cat, black, [(width / 4.3, 0.1 * height), (width / 4.8, 0.4 * height),
                            (width / 6.3, 0.25 * height),
                            (width / 4.3, 0.1 * height)])  # right ear line
    polygon(cat, body_color,
            [(width / 4.3 - 1, 0.1 * height + 1), (width / 4.8 - 1, 0.4 * height - 1),
             (width / 6.3 + 1, 0.25 * height), (width / 4.3 - 1, 0.1 * height + 1)])  # right ear
    polygon(cat, light_orange, [(width / 4.44, 0.125 * height), (width / 4.95, 0.335 * height),
                                      (width / 5.75, 0.25 * height),
                                      (width / 4.44, 0.125 * height)])  # right ear interior

    polygon(cat, black,
            [(0, 0.1 * height), (width / 45, 0.4 * height), (width / 13, 0.25 * height),
             (0, 0.1 * height)])  # left ear line
    polygon(cat, body_color, [(1, 0.1 * height + 1), (width / 45 + 1, 0.4 * height - 1),
                                   (width / 13 - 1, 0.25 * height), (1, 0.1 * height + 1)])  # left ear
    polygon(cat, light_orange, [(0.012 * width, 0.15 * height), (width / 38, 0.335 * height),
                                      (width / 15.6, 0.25 * height),
                                      (0.012 * width, 0.15 * height)])  # left ear interior

    ellipse(cat, black, [width / 28 - 1, 1 + height / 4 + 0.2 * height, width / 14.5 + 2, height / 4.2 + 2],
            1)  # left eye line
    ellipse(cat, eyes_color, [width / 28, height / 4 + 0.2 * height, width / 14.5, height / 4.2])  # left eye
    ellipse(cat, black,
            [width / 28 + width / 29, height / 3.9 + 0.2 * height, width / 80, height / 4.6])  # left eyelid
    ellipse(cat, light_grey,
            [width / 28 + width / 100, height / 3.7 + 0.2 * height, width / 35, height / 10])  # left eye shine

    ellipse(cat, eyes_color, [width / 7.2, height / 4 + 0.2 * height, width / 14.5, height / 4.2])  # right eye
    ellipse(cat, black,
            [width / 7.2 + width / 29, height / 3.9 + 0.2 * height, width / 80, height / 4.6])  # right eyelid
    ellipse(cat, light_grey,
            [width / 7.2 + width / 100, height / 3.7 + 0.2 * height, width / 35, height / 10])  # left eye shine

    polygon(cat, black, [(width / 8.4 - width / 80 - 1, 0.7 * height - 1),
                         (width / 8.4 + width / 80 + 1, 0.7 * height - 1),
                         (width / 8.4, height / 1.8 + 1 + 0.2 * height),
                         (width / 8.4 - width / 80 - 1, 0.7 * height - 1)])  # nose
    polygon(cat, pink,
            [(width / 8.4 - width / 80, 0.7 * height), (width / 8.4 + width / 80, 0.7 * height),
             (width / 8.4, height / 1.8 + 0.2 * height), (width / 8.4 - width / 80, 0.7 * height)])  # nose

    line(cat, black, (width / 8.4, height / 1.8 + 0.2 * height), (width / 8.4, height / 1.6 + 0.2 * height),
         1)  # line from nose to mouth
    arc(cat, black, [width / 8.4, height / 1.75 + 0.2 * height, width / 40, height / 12], 3.8, 6.28,
        1)  # right mouth wing
    arc(cat, black, [width / 8.4 - width / 44, height / 1.75 + 0.2 * height, width / 40, height / 12], 3.14, 6.28,
        1)  # left mouth wing

    # whiskers
    # right
    arc(cat, black, [width / 8.4 - width / 6.5, 0.725 * height, width / 1.8, height * 2], 1.25,
        1.95, 1)
    arc(cat, black,
        [width / 8.4 - width / 6.5 + width / 40, 0.665 * height, width / 1.8, height * 2], 1.35, 2.03, 1)
    arc(cat, black,
        [width / 8.4 - width / 6.5 - width / 40, 0.775 * height, width / 1.8, height * 2], 1.15, 1.85, 1)

    # left
    arc(cat, black, [width / 8.4 - width / 2.5, 0.725 * height, width / 1.8, height * 2], 1.25,
        1.95, 1)
    arc(cat, black,
        [width / 8.4 - width / 2.5 - width / 40, 0.665 * height, width / 1.8, height * 2], 1.15, 1.85, 1)
    arc(cat, black,
        [width / 8.4 - width / 2.5 + width / 40, 0.775 * height, width / 1.8, height * 2], 1.35, 2.05, 1)

    if orientation == 'right':
        cat = pygame.transform.flip(cat, True, False)
        surface.blit(cat, (x - 0.8 * width, y))
    else:
        surface.blit(cat, (x, y))


def ball_of_thread(surface, x, y, r, orientation):
    ball = pygame.Surface((3 * r, 2 * r))
    ball.set_colorkey(sepia)
    ball.fill(sepia)

    circle(ball, grey, (r, r), r)
    circle(ball, black, (r, r), r, 1)

    arc(ball, black, [0.17 * r, 0.25 * r, 1.9 * r, 1.9 * r], 1.66, 3.14, 1)
    arc(ball, black, [0.35 * r, 0.35 * r, 2 * r, 2 * r], 1.66, 3.14, 1)
    arc(ball, black, [0.45 * r, 0.45 * r, 2 * r, 2 * r], 1.66, 3.14, 1)
    arc(ball, black, [-0.25 * r, 0.5 * r, 2 * r, 2 * r], 0.15, 1.15, 1)
    arc(ball, black, [-0.41 * r, 0.65 * r, 2.1 * r, 2.1 * r], 0.15, 1.15, 1)
    arc(ball, black, [-0.65 * r, 0.85 * r, 2 * r, 2 * r], 0.15, 1.15, 1)

    # thread tail
    arc(ball, grey, [r + 0.33 * r, r + 0.225 * r, 0.7 * r, 0.7 * r], 4.1888, 5.236, 1)
    arc(ball, grey, [r + 0.33 * r + 0.35 * r, r + 0.225 * r + 0.606 * r, 0.7 * r, 0.7 * r], 1.0472, 2.11, 1)
    arc(ball, grey, [r + 0.33 * r + 0.7 * r, r + 0.225 * r, 0.7 * r, 0.7 * r], 4.1888, 5.236, 1)
    arc(ball, grey, [r + 0.33 * r + 1.05 * r, r + 0.225 * r + 0.606 * r, 0.7 * r, 0.7 * r], 1.0472, 2.11, 1)
    arc(ball, grey, [r + 0.33 * r + 1.4 * r, r + 0.225 * r, 0.7 * r, 0.7 * r], 4.1888, 5.236, 1)
    arc(ball, grey, [r + 0.33 * r + 1.75 * r, r + 0.225 * r + 0.606 * r, 0.7 * r, 0.7 * r], 1.0472, 2.11, 1)
    if orientation == 'right':
        ball = pygame.transform.flip(ball, True, False)

    surface.blit(ball, (x - r, y - r))


rect(screen, sepia, (0, 400, 600, 400))
rect(screen, dark_brown, (0, 0, 600, 400))

draw_window(400, 35, 250, 330)

draw_window(130, 35, 250, 330)

draw_window(-140, 35, 250, 330)

draw_cat(screen, 60, 400, 400, 120, body_color=brown, eyes_color=green, orientation='left')
draw_cat(screen, 300, 440, 300, 90, body_color=dark_grey, eyes_color=yellow, orientation='left')
draw_cat(screen, 300, 530, 400, 120, body_color=dark_grey, eyes_color=yellow, orientation='right')
draw_cat(screen, 300, 230, 240, 72, body_color=dark_grey, eyes_color=yellow, orientation='right')
draw_cat(screen, 220, 700, 300, 90, body_color=brown, eyes_color=green, orientation='left')
draw_cat(screen, 520, 700, 300, 90, body_color=brown, eyes_color=green, orientation='right')

ball_of_thread(screen, 400, 660, 60, orientation='left')
ball_of_thread(screen, 200, 560, 40, orientation='right')
ball_of_thread(screen, 300, 60, 100, orientation='left')
ball_of_thread(screen, 100, 760, 50, orientation='left')

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
