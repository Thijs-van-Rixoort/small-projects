from cmath import cos, sin
from random import randint
import pygame
from my_libs import color
from math import ceil

pygame.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
window.fill("#222222")

pygame.mouse.set_visible(False)

exit_game = False

time = 1
sinus = sin(time/100).real
oldSinus = sinus
cosinus = cos(time/100).real
oldCosinus = cosinus

add_speed = 0
rotations = 0
magnification = 10
click_speed = 10
zoom = 0.001

# SPEED_DECREASE #
# speed_decrease = 0.001
speed_decrease = (click_speed * 0.00001025) * (zoom * 1000)

# RANDOMNESS #
randX = 0
randY = 0
amount_of_randomness = 0

# COLOR #
colorList = color.gradient(["00FF00", "FF00FF"], 255)

while not exit_game:

    oldRandX = randX
    oldRandY = randY

    if add_speed > 0:
        add_speed -= add_speed * speed_decrease
        add_speed -= speed_decrease
        rotations += add_speed * zoom

        randX = randint(randX-amount_of_randomness,randX+amount_of_randomness)
        randY = randint(randY-amount_of_randomness,randY+amount_of_randomness)
    else:
        add_speed = 0

    time += add_speed
    oldSinus = sinus
    sinus = sin(time/100).real
    oldCosinus = cosinus
    cosinus = cos(time/100).real

    pygame.draw.line(window, colorList[(len(colorList)-1) - ceil(add_speed * ((len(colorList)-1) / click_speed))], (window.get_width() / 2 + oldCosinus*magnification*rotations + oldRandX, window.get_height() / 2 + oldSinus*magnification*rotations + oldRandY), (window.get_width() / 2 + cosinus*magnification*rotations + randX, window.get_height() / 2 + sinus*magnification*rotations + randY))

    # CHECK KEY & MOUSE EVENTS#
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit_game = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if add_speed <= 0:
                    add_speed = click_speed
    
    pygame.display.update()