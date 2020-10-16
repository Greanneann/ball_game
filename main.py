from random import randint
import pygame
from pygame.draw import *

pygame.init()

FPS = 0.3
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def prover_circ(event_x, event_y, x_y_circ, radius):
    """по теореме Пифагора проверяет попал ли игрок в шарик
    event_x, event_y - координаты нажатия мыши,
    x_y_circ - список координат шариков
    radius - список радиусов шариков"""
    for i in range(len(radius)):
        a = (x_y_circ[0][i] - event_x)**2
        b = (x_y_circ[1][i] - event_y)**2
        c = (a + b)**0.5
        if c <= radius[i]:
            return True
    return False


def prover_ellip(event_x, event_y, x_y_ell, par_ell):
    """проверка попадания в эллипс
    par_ell - параметры эллипсы, его большая и малая полуоси
    x_y_ell - координаты эллипса"""
    for i in range(len(x_y_ell[0])):
        a = (x_y_ell[0][i] + par_ell[0][i]/2 - event_x)**2
        b = (x_y_ell[1][i] + par_ell[1][i]/2 - event_y)**2
        c = (a + b)**0.5
        if c <= par_ell[0][i]/2 and c <= par_ell[1][i]/2:
            return True
    return False


def new_balls(number, x_y_circ, radius):
    """рисует новые шарики"""
    for i in range(number):
        color = COLORS[randint(0, 5)]
        circle(screen, color,
               (x_y_circ[0][i], x_y_circ[1][i]), radius[i])


def location_of_ball(number):
    """определяет координаты и радиусы будущих шариков"""
    x_y_circ = [[0 for _ in range(number)], [0 for _ in range(number)]]
    radius = [0 for _ in range(number)]
    for i in range(number):
        x = randint(100, 1100)
        x_y_circ[0][i] = x
        y = randint(100, 900)
        x_y_circ[1][i] = y
        r = randint(10, 100)
        radius[i] = r
    return [x_y_circ, radius]


def new_ellipse(number2, x_y_ell, par_ell):
    """рисует новый эллипс"""
    for i in range(number2):
        color = COLORS[randint(0, 5)]
        ellipse(screen, color,
                (x_y_ell[0][i], x_y_ell[1][i], par_ell[0][i], par_ell[1][i]))


def location_of_ellipse(number2):
    """определяет координаты и параметры эллипса"""
    x_y_ell = [[0 for _ in range(number2)], [0 for _ in range(number2)]]
    par_ell = [[0 for _ in range(number2)], [0 for _ in range(number2)]]
    for i in range(number2):
        x = randint(100, 1100)
        x_y_ell[0][i] = x
        y = randint(100, 900)
        x_y_ell[1][i] = y
        parx = randint(100, 200)
        par_ell[0][i] = parx
        pary = randint(80, 150)
        par_ell[1][i] = pary
    return [x_y_ell, par_ell]


def move_balls(number, x_y_circ, radius):
    for j in range(100):
        for i in range(number):
            x = x_y_circ[0][i] + j
            y = x_y_circ[0][i] + j
            x_y_circ[0].append(x)
            x_y_circ[1].append(y)


clock = pygame.time.Clock()
finished = False
score1 = 0
score2 = 0
number = 0
number2 = 4

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            result1 = prover_circ(event.pos[0], event.pos[1],
                                  x_y_circ, radius)
            result12 = prover_ellip(event.pos[0], event.pos[1],
                                  x_y_ell, par_ell)
            if result1:
                score1 += 1
            if result12:
                score2 += 3

    values = location_of_ball(number)
    x_y_circ = values[0]
    radius = values[1]
    values2 = location_of_ellipse(number2)
    x_y_ell = values2[0]
    par_ell = values2[1]
    new_balls(number, x_y_circ, radius)
    new_ellipse(number2, x_y_ell, par_ell)
    pygame.display.update()
    screen.fill(BLACK)


print('Счёт за круги:', score1, 'Счёт за эллипсы:', score2)
print('Сумма', score1 + score2)

pygame.quit()
