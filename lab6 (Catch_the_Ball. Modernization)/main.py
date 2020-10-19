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


class Square:
    """
    Class of squares moving on screen
    """
    def __init__(self, x, y, a, color):
        self.x = x  # x-coordinate of square's center
        self.y = y  # y-coordinate of square's center
        self.a = a  # length of square's side
        self.color = color  # color of square


TIME = 30  # time of game in seconds

FPS = 24  # frames per second
WIDTH, HEIGHT = 1200, 800  # width and height of window
R_MIN, R_MAX = 20, 100  # minimal and maximal radius of ball
A_MIN, A_MAX = 70, 180  # minimal and maximal length of square's side

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


def new_ball(balls):
    """
    Create new ball
    :param balls: list of objects of the type Ball
    """
    x = randint(R_MAX, WIDTH - R_MAX)  # x-coordinate of ball's center
    y = randint(R_MAX, HEIGHT - R_MAX)  # y-coordinate of ball's center
    r = randint(R_MIN, R_MAX)  # radius of ball
    v_x = randint(-10, 10)  # projection of ball's velocity to x-axe
    v_y = randint(-10, 10)  # projection of ball's velocity to y-axe
    color = COLORS[randint(0, len(COLORS) - 1)]  # color of ball
    lifetime = randint(2, 5)  # lifetime of the ball
    balls.append(Ball(x, y, r, v_x, v_y, color, lifetime))
    circle(screen, color, (x, y), r)


def new_square(squares):
    """
    Create new square
    :param squares: list of objects of the type Square
    """
    x = randint(0, WIDTH - A_MAX)  # x-coordinate of square's left top vertex
    y = randint(0, HEIGHT - A_MAX)  # y-coordinate of square's left top vertex
    a = randint(A_MIN, A_MAX)  # length of square's side
    color = COLORS[randint(0, len(COLORS) - 1)]  # color of square
    squares.append(Square(x, y, a, color))
    rect(screen, color, (x, y, a, a))


def draw_ball(ball):
    """
    Draw ball on the screen
    :param ball: Ball object
    """
    surf = pygame.Surface((2 * ball.r, 2 * ball.r))
    surf.fill(BLACK)
    surf.set_colorkey(BLACK)
    circle(surf, ball.color, (ball.r, ball.r), ball.r)
    screen.blit(surf, (ball.x - ball.r, ball.y - ball.r))


def draw_square(square):
    """
    Draw square on the screen
    :param square: Square object
    """
    rect(screen, square.color, (square.x, square.y, square.a, square.a))


def click(ev):
    """
    Respond to click
    if position of click is in ball, score will increase by 1
    if position of click is in square, score will increase by 2
    :param ev: object from pygame.event.get()
    """
    global score
    for ball in balls:
        if (ev.pos[0] - ball.x) ** 2 + (ev.pos[1] - ball.y) ** 2 <= ball.r ** 2:
            score += 1
            balls.remove(ball)
    for square in squares:
        if square.x <= ev.pos[0] <= square.x + square.a and square.y <= ev.pos[1] <= square.y + square.a:
            score += 2
            squares.remove(square)


def time_to_text(time: int) -> str:
    """
    converts time to text
    :param time: time in seconds
    :return: time in text format
    """
    minutes, seconds = time // 60, time % 60
    if minutes < 10:
        minutes = '0' + str(minutes)
    else:
        minutes = str(minutes)
    if seconds < 10:
        seconds = '0' + str(seconds)
    else:
        seconds = str(seconds)
    return minutes + ':' + seconds


score = 0
FONT = pygame.font.Font(None, 40)

# label with score
score_text = FONT.render('Score: ' + str(score), 1, WHITE)
SCORE_TEXT_POSITION = (0, 0)
screen.blit(score_text, SCORE_TEXT_POSITION)

# label with time
time_text = FONT.render(time_to_text(TIME), 1, WHITE)
TIME_TEXT_POSITION = (WIDTH - 100, 0)
screen.blit(time_text, TIME_TEXT_POSITION)

clock = pygame.time.Clock()

input_box = pygame.Rect(500, 400, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
name_entered = False
finished = False
text = ''
NAME = ''
intro_text = 'Enter the name'
while not name_entered and not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            name_entered = True
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if the user clicked on the input_box rect
            if input_box.collidepoint(event.pos[0], event.pos[1]):
                # toggle the active variable.
                active = not active
            else:
                active = False
            # change the current color of the input box
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    name_entered = True
                    NAME = text
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
    screen.fill(BLACK)
    # render the current text
    txt_surface = FONT.render(text, True, color)
    # resize the box if the text is too long
    width = max(200, txt_surface.get_width() + 10)
    input_box.w = width
    # blit the text
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    # blit the input_box rect
    pygame.draw.rect(screen, color, input_box, 2)

    intro_text_surface = FONT.render(intro_text, True, WHITE)
    screen.blit(intro_text_surface, (input_box.x, input_box.y - 40))

    pygame.display.update()
    clock.tick(FPS)

if finished:
    pygame.quit()

balls = []
squares = []

while not finished:
    new_ball(balls)
    new_square(squares)
    for i in range(FPS):
        clock.tick(FPS)
        # handling of events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click(event)

        # changing position and parameters of objects
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

        for square in squares:
            square.a -= 2
            square.x += 1
            square.y += 1
            if square.a <= 0:
                squares.remove(square)
            else:
                draw_square(square)

        # changing number of scores on the screen
        score_text = FONT.render('Score: ' + str(score), 1, WHITE)
        screen.blit(score_text, SCORE_TEXT_POSITION)

        # changing time on the screen
        time_text = FONT.render(time_to_text(TIME), 1, WHITE)
        TIME_TEXT_POSITION = (WIDTH - 100, 0)
        screen.blit(time_text, TIME_TEXT_POSITION)

        pygame.display.update()
        screen.fill(BLACK)

    # changing lifetime of balls
    for ball in balls:
        ball.lifetime -= 1
        if ball.lifetime <= 0:
            balls.remove(ball)

    # changing time on the screen
    TIME -= 1
    if TIME <= 0:
        finished = True

pygame.quit()

list_of_the_best_players = []
# get names and scores of players
with open('the_best_players.txt', 'r') as outfile:
    for string in outfile:
        if len(string.split()) == 2 and string.split()[0] != '':
            player_name, player_score = string.split()
            player_score = int(player_score)
            list_of_the_best_players.append((player_name, player_score))

# append NAME and score of current player
list_of_the_best_players.append((NAME, score))
list_of_the_best_players.sort(key=lambda x: x[1], reverse=True)

# write names and scores to file
with open('the_best_players.txt', 'w') as outfile:
    for player in list_of_the_best_players:
        outfile.write(str(player[0]) + '\t' + str(player[1]) + '\n')
