from typing import NamedTuple
import functools
from colors import Color

def colors_list(colors: list[Color]):
    for c in colors:
        color_desc(c)

def color_desc(color: Color):
    (r, g, b) = color.get_rgb()
    info = [
            color.name,
            f'hex: {color.get_hex().upper()}',
            f'rgb: {r} / {g} / {b}'
            ]
    layout = RectLayout(7, 3, Offset(1, 1, 1, 1))
    draw_rect(color, layout, info)

def draw_rect(color: Color, layout: RectLayout, info: list[str] | None = None):
    (r, g, b) = color.get_rgb()
    for _ in range(layout.offset.top): print()
    for i in range(layout.height):
        for _ in range(layout.offset.left): print(' ', end='')
        draw_line(layout.width, r, g, b)
        for _ in range(layout.offset.right): print(' ', end='')
        try_print_info(i, info)
        print('')
    for _ in range(layout.offset.bottom): print()

def try_print_info(index: int, info: list[str] | None = None):
    if info is None: return

    if index < len(info):
        print(info[index], end='')

def draw_line(w, r, g, b):
    fg = f'\033[38;2;{r};{g};{b}m'
    reset = '\033[0m'
    # box_line = fg + '█' * w + reset
    line = fg + chr(9608) * w + reset
    print(line, end='')

class RectLayout(NamedTuple):
    width: int
    height: int
    offset: Offset

class Offset(NamedTuple):
    right: int
    left: int
    top: int
    bottom: int
