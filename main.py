import sys

import output
from cli_commands import parse_command, Command
from colors import read_colors, read_color


if __name__ == '__main__':
    (cmd, args) = parse_command(sys.argv)
    match cmd:
        case Command.LIST_COLORS:
            colors = read_colors()
            output.colors_list(colors)
        case Command.GET_COLOR:
            name = args.get('name', '')
            color = read_color(name)
            if color:
                output.color_desc(color)
            else:
                output.print_error_msg(f'No color with name "{name}" found', output.Offset(1, 1, 1, 1))
        case _:
            print('soon...')


