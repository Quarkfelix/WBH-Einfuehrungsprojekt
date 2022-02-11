import pygame
import sys

from pygame.locals import *


BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)


def main():
    window_width = 300
    window_height = 250
    running = True
    window_resolution = (window_width, window_height)
    background_color = BLUE  # rgb defined color
    color_green = pygame.Color('green')
    # pygame defined color
    # define values for a rectangle, x, y, width and height
    rect_x = 10
    rect_y = 10
    rect_width = 20
    rect_height = 20
    # define a rect as touple of 4 values
    my_rect = (rect_x, rect_y, rect_width, rect_height)
    # init pygame, define display surface and set a title for the window
    pygame.init()
    display_surface = pygame.display.set_mode(window_resolution)
    pygame.display.set_caption('Fun with PyGame!')
    # infinity loop - stop running with escape key or by closing the window
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        display_surface.fill(background_color)
        pygame.draw.rect(display_surface, color_green, my_rect, 0)
        pygame.draw.circle(display_surface, RED, (80, 80), 30)
        pygame.draw.ellipse(display_surface, YELLOW, (100, 150, 50, 25), 0)
        pygame.draw.line(display_surface, WHITE, (220, 160), (160, 220))
        pygame.display.flip()

        if not running:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    main()
