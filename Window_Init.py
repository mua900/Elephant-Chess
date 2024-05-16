# Initialize window using pygame

import pygame
import sys
import os
import MathUtils
import cairosvg
from io import BytesIO

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

window_start_size: tuple[int, int] = (300, 300)
WINDOW = pygame.display.set_mode(window_start_size, pygame.RESIZABLE)
window_width, window_height = window_start_size
pygame.display.set_caption("Chess")


def draw_squares(win_width, win_height):
    sqr_width: float = win_width / 8
    sqr_height: float = win_height / 8

    sqr_positions: list = []

    for i in range(8):
        for j in range(8):
            sqr_color = WHITE if (i + j) % 2 == 0 else BLACK
            pygame.draw.rect(WINDOW, sqr_color, (sqr_width * j, sqr_height * i, sqr_width, sqr_height))
            sqr_positions.append((sqr_width * (j + 1 / 2), sqr_height * (i + 1 / 2)))
    return sqr_positions


# We want the window to be close to a square. If its shape is too far off, we try to squish or widen it. I have yet to
# decide on either one.
def set_window_to_square(win_width, win_height, event_w, event_h):
    if not MathUtils.ratio_close_to_desired(win_width, win_height, 1, 1 / 10):
        bigger_one = max(event_h, event_w)
        pygame.display.set_mode((bigger_one, bigger_one), pygame.RESIZABLE)

    if pygame.key.get_pressed():
        load_pieces("kiwen-suwi", 0)


def load_pieces(piece_set: str, sqr_positions):
    # Load images // Files will be organized better later
    # We use images we got from lichess so every single image file we have is .svg. // We are now also using cairosvg
    images = []
    piece_sets_dir = os.path.join(os.path.curdir, "Assets", "Piece_Sets")
    if not os.path.exists(piece_sets_dir):
        raise FileNotFoundError("AAFMCAAMvşkdmvk")
    piece_set_path = os.path.join(piece_sets_dir, piece_set)
    if not os.path.exists(piece_set_path):
        raise FileNotFoundError(f"{piece_set} was not found in the {piece_sets_dir}")

    for image in os.listdir(piece_set_path):
        image_path = os.path.join(piece_set_path, image)
        try:
            images.append(svg_to_surface(image_path))
        except pygame.error as pg:
            print(f"Error loading image {image}: {pg}")

    return images
    # Draw the pieces we loaded in


def svg_to_surface(svg_file):  # Necessary for the draw_pieces()
    png_data = cairosvg.svg2png(url=svg_file)
    image = pygame.image.load(BytesIO(png_data))
    return image


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            if not event.type == pygame.FULLSCREEN:  # This check doesn't help anything ## TODO Fix this ##
                set_window_to_square(window_width, window_height, event.w, event.h)  # This is broken if you extend
                # the window too much especially in fullscreen
        else:
            WINDOW.fill(WHITE)
            window_width, window_height = WINDOW.get_width(), WINDOW.get_height()
            draw_squares(window_width, window_height)
            pygame.display.update()
