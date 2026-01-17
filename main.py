import sys

import output
from cli_commands import parse_command, Command
from colors import read_colors, read_color, save_color, remove_color


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
                output.print_error_msg(f'Color "{name}" not found', output.unit_offset)
        case Command.PUT_COLOR:
            name = args.get('name', '')
            value = args.get('value', '')
            saved_color = save_color(name, value)
            output.print_success_msg(f'Color "{name}" saved', output.unit_offset)
        case Command.ERROR:
            error_msg = args.get('msg', 'Something went wrong...')
            output.print_error_msg(error_msg, output.unit_offset)
        case Command.LIST_COLOR_NAMES:
            colors = read_colors()
            output.color_names_list(colors, output.unit_offset)
        case Command.REMOVE_COLOR:
            name = args.get('name', '')
            removed = remove_color(name)
            match removed:
                case True: output.print_success_msg(f'Color "{name}" removed', output.unit_offset)
                case False: output.print_error_msg(f'Color "{name}" not found', output.unit_offset)
        case _:
            print('soon...')


