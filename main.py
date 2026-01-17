import sys

import output
from cli_commands import parse_command, Command
from colors import read_colors, read_color, save_color


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
                output.print_error_msg(f'No color with name "{name}" found', output.unit_offset)
        case Command.PUT_COLOR:
            name = args.get('name', None)
            value = args.get('value', None)
            if not name or not value: raise Exception('Should not be here, name/value must be checked before')
            save_color(name, value)
        case Command.ERROR:
            error_msg = args.get('msg', 'Something went wrong...')
            output.print_error_msg(error_msg, output.unit_offset)
        case _:
            print('soon...')


