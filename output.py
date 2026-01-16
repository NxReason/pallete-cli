import functools

def rgb_box(w, h, r, g, b):
    fg = f'\033[38;2;{r};{g};{b}m'
    reset = '\033[0m'
    # box_line = fg + '█' * w + reset
    box_line = fg + chr(9608) * w + reset
    for _ in range(h):
        print(box_line)

color_square = functools.partial(rgb_box, 7, 3)

