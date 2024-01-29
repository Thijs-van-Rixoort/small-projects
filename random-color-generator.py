import pygame
from my_libs import color
import pyperclip

pygame.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

font = pygame.font.SysFont('arial', 30)

exit_game = False

color_list = ["#333333"]
current_color_index = 0

control = False
copied_message_frames = 0

while not exit_game:

    window.fill(color_list[current_color_index])

    text_color = color.convert_string_to_int(color.get_color_negative(color_list[current_color_index]))

    text = font.render(f"Hex: {color_list[current_color_index]}", True, text_color)
    window.blit(text, (5, 0))
    text = font.render(f"Current Color: {current_color_index + 1}", True, text_color)
    window.blit(text, (5, 30))
    text = font.render(f"Colors Generated: {len(color_list)}", True, text_color)
    window.blit(text, (5, 60))

    if copied_message_frames > 0:
        text = font.render("Copied!", True, text_color)
        text_rect = text.get_rect()
        text_rect.center = (window.get_width()/2, window.get_height()/2)
        window.blit(text, text_rect)
        copied_message_frames -= 1

    # CHECK KEY & MOUSE EVENTS #
    for event in pygame.event.get():

        # KEYDOWN EVENTS #
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit_game = True
            if event.key == pygame.K_LEFT and current_color_index > 0:
                current_color_index -= 1
            if event.key == pygame.K_RIGHT and current_color_index < len(color_list) - 1:
                current_color_index += 1
            if event.key == pygame.K_LCTRL:
                control = True
            if event.key == pygame.K_c and control:
                pyperclip.copy(color_list[current_color_index])
                copied_message_frames = 600

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LCTRL:
                control = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                color_list.append(color.create_random_color())
                current_color_index = len(color_list) - 1

    pygame.display.update()