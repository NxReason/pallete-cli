import sys
from cli_commands import parse_command, Command
from colors import read_colors
from output import colors_list


if __name__ == '__main__':
    (cmd, args) = parse_command(sys.argv)
    match cmd:
        case Command.LIST_COLORS:
            colors = read_colors()
            colors_list(colors)
        case _:
            print('soon...')


