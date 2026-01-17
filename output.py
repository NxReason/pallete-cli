from typing import NamedTuple
import functools
from colors import Color

class RectLayout(NamedTuple):
    width: int
    height: int
    offset: Offset

class Offset(NamedTuple):
    right: int
    left: int
    top: int
    bottom: int

    def draw_top(self):
        for _ in range(self.top): print()

    def draw_bottom(self):
        for _ in range(self.bottom): print()

    def draw_left(self):
        print(' ' * self.left, end='')

    def draw_right(self):
        print(' ' * self.right, end='')

no_offset = Offset(0, 0, 0, 0)

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
    layout.offset.draw_top()
    for i in range(layout.height):
        layout.offset.draw_left()
        draw_line(layout.width, r, g, b)
        layout.offset.draw_right()
        try_print_info(i, info)
        print('')
    layout.offset.draw_bottom()

def try_print_info(index: int, info: list[str] | None = None):
    if info is None: return

    if index < len(info):
        print(info[index], end='')

def print_error_msg(msg: str, offset: Offset = no_offset):
    offset.draw_top()
    offset.draw_left()
    print(f' {msg}')
    offset.draw_bottom()

def draw_line(w, r, g, b):
    fg = f'\033[38;2;{r};{g};{b}m'
    reset = '\033[0m'
    # box_line = fg + '█' * w + reset
    line = fg + chr(9608) * w + reset
    print(line, end='')


