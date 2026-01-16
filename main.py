import sys
from cli_commands import parse_command, Command
from colors import print_color, read_colors

if __name__ == '__main__':
    (cmd, args) = parse_command(sys.argv)
    match cmd:
        case Command.LIST_COLORS:
            colors = read_colors()
            print(colors)
        case _:
            print('soon...')


