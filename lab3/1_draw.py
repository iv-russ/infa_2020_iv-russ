import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

grey = (200, 200, 200)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)

screen.fill(grey)

circle(screen, yellow, (200, 200), 100)
circle(screen, black, (200, 200), 100, 1)

circle(screen, red, (150, 170), 25)
circle(screen, black, (150, 170), 25, 1)
circle(screen, black, (150, 170), 10)

circle(screen, red, (250, 170), 20)
circle(screen, black, (250, 170), 20, 1)
circle(screen, black, (250, 170), 8)

polygon(screen, black, [(91, 100), (191, 150), (186, 160), (86, 110), (91, 100)])
polygon(screen, black, [(220, 155), (300, 115), (304, 123), (224, 163), (220, 155)])

rect(screen, black, (150, 250, 100, 15))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()