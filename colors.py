from output import color_square

def read_colors() -> list[str]:
    result = []
    with open('colors.txt', 'r', encoding='utf-8') as file:
        result = file.readlines()
    return result

def print_color(r, g, b):
    print(f'#{r:X}{g:X}{b:X}')
    color_square(r, g, b)
    print()
