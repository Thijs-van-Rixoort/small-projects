from math import floor
import pygame
from random import randint
from my_libs import color

pygame.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

pygame.mouse.set_visible(False)

exit_game = False

# BALL PROPERTIES #
radius = 10
bounciness = 0.9

x_pos = window.get_width()/2
x_speed = 0
y_pos = window.get_height() - radius
y_speed = 0

max_speed = 5

# COLOR #
color_list = color.gradient(["00FF00", "FFFF00", "FF0000"], 255)

while not exit_game:

    window.fill("#333333")

    # DETERMINE COLOR #
    if abs(y_speed) > abs(x_speed):
        biggest_speed = abs(y_speed)
    else:
        biggest_speed = abs(x_speed)

    y_speed += 0.01

    if abs(x_speed) > 0.03:
        x_speed = x_speed / 1.0005
    else:
        x_speed = x_speed / 1.005

    # CALCULATE Y_POS & Y_SPEED #
    if y_pos > window.get_height() - radius:
        y_pos = window.get_height() - radius
        y_speed = -y_speed * bounciness + bounciness / 100
    elif y_pos < 0 + radius:
        y_pos = 0 + radius
        y_speed = -y_speed * bounciness + bounciness / 100
    else:
        y_pos += y_speed

    # CALCULATE X_POS & X_SPEED #
    if x_pos > window.get_width() - radius:
        x_pos = window.get_width() - radius
        x_speed = -x_speed * bounciness + bounciness / 100
    elif x_pos < 0 + radius:
        x_pos = 0 + radius
        x_speed = -x_speed * bounciness + bounciness / 100
    else:
        x_pos += x_speed

    # DRAW CIRCLE #
    pygame.draw.circle(window, color_list[floor(biggest_speed * (len(color_list)-1) / max_speed)], (x_pos, y_pos), radius)

    # CHECK KEY & MOUSE EVENTS#
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit_game = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if y_speed < 0.1 and y_pos > window.get_height() - radius - 1:
                    x_speed = randint(max_speed, max_speed)
                    y_speed = -(randint(max_speed, max_speed))
    
    pygame.display.update()