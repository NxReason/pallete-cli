from enum import Enum

class Command(Enum):
    GET_COLOR = 'GET_COLOR'
    PUT_COLOR = 'PUT_COLOR'
    LIST_COLORS = 'LIST_COLORS'
    LIST_COLOR_NAMES = 'LIST_COLOR_NAMES'
    REMOVE_COLOR = 'REMOVE_COLOR'
    ERROR = 'ERROR'


def parse_command(argv: list[str]) -> tuple[Command, dict]:
    if len(argv) < 2:
        return (Command.ERROR, { "msg" : "Not enough arguments" })

    command = argv[1]
    match command:
        case 'get' | 'g':
            if len(argv) < 3: return (Command.ERROR, { "msg": "Specify color name to get" })
            return (Command.GET_COLOR, { "name": argv[2] })
        case 'put' | 'p':
            if len(argv) < 4: return (Command.ERROR, { "msg": "Specify name and color to save" })
            return (Command.PUT_COLOR, { "name": argv[2], "value": argv[3] })
        case 'list' | 'l':
            return (Command.LIST_COLORS, {})
        case 'list-names' | 'ln':
            return (Command.LIST_COLOR_NAMES, {})
        case 'remove' | 'r':
            if len(argv) < 3: return (Command.ERROR, { "msg": "Specify color name to remove" })
            return (Command.REMOVE_COLOR, { "name": argv[2] })
        case _:
            return (Command.ERROR, { "msg": f"Unknown command: {command}"})

# TESTING
import unittest

class TestCommands(unittest.TestCase):
    def test_not_enough_args(self):
        result = parse_command(['main.py'])
        self.assertEqual(result[0], Command.ERROR)
        self.assertEqual(result[1]['msg'], 'Not enough arguments')

    def test_valid_get_color(self):
        args = ['main.py', 'get', 'color_name']
        result = parse_command(args)
        self.assertEqual(result[0], Command.GET_COLOR)
        self.assertEqual(result[1]['name'], 'color_name')

    def test_valid_get_color_alias(self):
        args = ['main.py', 'g', 'color_name']
        result = parse_command(args)
        self.assertEqual(result[0], Command.GET_COLOR)
        self.assertEqual(result[1]['name'], 'color_name')

    def test_invalid_get_color(self):
        args = ['main.py', 'get']
        result = parse_command(args)
        self.assertEqual(result[0], Command.ERROR)
        self.assertEqual(result[1]['msg'], 'Specify color name to get')


if __name__ == '__main__':
    unittest.main()
