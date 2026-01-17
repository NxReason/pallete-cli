class Color:
    def __init__(self, name: str, hex_: str = '000000', rgb: tuple[int, int, int] | None = None):
        self.name = name
        # if neither provided -> set to default (000000)
        # if only one provided -> set other accordingly
        # if both provided -> prefer RGB
        if rgb is None:
            self.set_hex(hex_)
        else:
            self.set_rgb(rgb)

    def get_hex(self):
        return self._hex

    def get_rgb(self):
        return self._rgb

    def set_hex(self, value: str):
        self._hex = value
        self._rgb = _hex_to_rgb(value)

    def set_rgb(self, value: tuple[int, int, int]):
        self._rgb = value
        self._hex = _rgb_to_hex(value)

def _hex_to_rgb(hex_value: str) -> tuple[int, int, int]:
    r = int(hex_value[0:2], base=16)
    g = int(hex_value[2:4], base=16)
    b = int(hex_value[4:6], base=16)
    return (r, g, b)

def _rgb_to_hex(rgb_value: tuple[int, int, int]):
    (r, g, b) = rgb_value
    r = f'0{r:x}' if r < 10 else f'{r:x}'
    g = f'0{g:x}' if g < 10 else f'{g:x}'
    b = f'0{b:x}' if b < 10 else f'{b:x}'
    return f'{r}{g}{b}'

def read_colors() -> list[Color]:
    result = []
    with open('colors.txt', 'r', encoding='utf-8') as file:
        for line in file:
            name, hex_value = line.split(' ')
            hex_ = hex_value[:6]
            result.append(Color(name, hex_))
    return result

def read_color(name: str) -> Color | None:
    colors = read_colors()
    color = None
    for c in colors:
        if c.name == name:
            color = c
            break
    return color

def save_color(name: str, value: str):
    new_color = Color(name, value)
    colors = read_colors()
    updated = False
    for i, c in enumerate(colors):
        if c.name == name:
            colors[i] = new_color
            updated = True
            break
    if not updated:
        colors.append(new_color)

    with open('colors.txt', 'w', encoding='utf-8') as file:
        for color in colors:
            file.write(f'{color.name} {color.get_hex().upper()}\n')


# TESTING
import unittest

class TestColors(unittest.TestCase):
    def test_read_colors(self):
        result = read_colors()
        self.assertTrue(len(result) > 0)

    def test_color_cls_new(self):
        color = Color('test_color', '3434ff')
        self.assertEqual(color.name, 'test_color')
        self.assertEqual(color.get_hex().lower(), '3434ff')
        self.assertEqual(color.get_rgb(), (52, 52, 255))

        color = Color('test_color2', hex_='bada55')
        self.assertEqual(color.get_hex().lower(), 'bada55')
        self.assertEqual(color.get_rgb(), (186, 218, 85))

        color = Color('test_color3', rgb=(255, 255, 255))
        self.assertEqual(color.get_hex().lower(), 'ffffff')
        self.assertEqual(color.get_rgb(), (255, 255, 255))

        color = Color('test_color4', '001500', rgb=(186, 218, 85))
        self.assertEqual(color.get_hex().lower(), 'bada55')
        self.assertEqual(color.get_rgb(), (186, 218, 85))

    def test_convert_to_hex(self):
        result = _rgb_to_hex((52, 52, 255))
        self.assertEqual(result, '3434ff')

        # test padding for < 10 values
        result = _rgb_to_hex((0, 5, 2))
        self.assertEqual(result, '000502')

    def test_convert_to_rgb(self):
        result = _hex_to_rgb('3434ff')
        self.assertEqual(result, (52, 52, 255))

    def test_setting_one_changes_other(self):
        color = Color('test_color')
        self.assertEqual(color.name, 'test_color')
        self.assertEqual(color.get_hex(), '000000')

    def test_reading_from_file(self):
        colors = read_colors()
        self.assertTrue(len(colors) > 0)
        self.assertListEqual(
                [colors[0].name, colors[1].name, colors[2].name],
                ['skin', 'red', 'blue']
                )
        self.assertEqual(colors[0].get_hex().lower(), 'bada55')

    def test_get_color(self):
        result = read_color('skin')
        self.assertIsNotNone(result)
        if result is None: return
        self.assertEqual(result.name, 'skin')
        self.assertEqual(result.get_hex().lower(), 'bada55')

    def test_get_color_none(self):
        result = read_color('non-existent-name')
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
