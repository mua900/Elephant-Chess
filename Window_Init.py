# Initialize window using pygame
from typing import Any

import pygame
import sys

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

window_start_size: tuple = (300, 300)
WINDOW = pygame.display.set_mode(window_start_size, pygame.RESIZABLE)
window_width, window_height = window_start_size
pygame.display.set_caption("Chess")


def draw_squares(win_width, win_height):
    sqr_width: float = win_width / 8
    sqr_height: float = win_height / 8

    # Draw vertical and horizontal lines

    """
    for i in range(8):
        # Vertical
        pygame.draw.line(WINDOW, BLACK, (sqr_width * i, 0), (sqr_width * i, win_height), 2)
        # Horizontal
        pygame.draw.line(WINDOW, BLACK, (0, sqr_height * i), (win_width, sqr_height * i), 2)
    """
    # Do it with squares instead

    sqr_positions: list = []

    for i in range (8):
        for j in range (8):
            sqr_color = WHITE if (i + j)%2 == 0 else BLACK
            pygame.draw.rect(WINDOW, sqr_color, (sqr_width * j, sqr_height * i, sqr_width, sqr_height))
            sqr_positions.append((sqr_width * (j + 1/2), sqr_height * (i + 1/2)))
    return sqr_positions

# We want the window to be square. If its shape is too far off from being a square we try to squish it.
###TODO###
def set_window_to_square():
    pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            WINDOW.fill(WHITE)
            window_width, window_height = WINDOW.get_width(), WINDOW.get_height()
            draw_squares(window_width, window_height)
            pygame.display.update()
