import unittest

from kmldata import color


class TestColor(unittest.TestCase):

    def test_Color(self):
        white = color.Color(1, 1, 1)
        black = color.Color(0, 0, 0)
        self.assertEqual(str(white), "#FFFFFFFF")
        self.assertEqual(str(black), "#FF000000")
        self.assertEqual(repr(white), "Color(1.0, 1.0, 1.0)")
        self.assertEqual(repr(black), "Color(0.0, 0.0, 0.0)")

    def test_ColorMap(self):
        cm = color.ColorMap(
            color_a=color.Color(0, 0, 0),
            color_b=color.Color(1, 1, 1),
            n_colors=5,
        )
        self.assertTrue(hasattr(cm, "mapping"))
        self.assertNotEqual(cm.mapping, {})
        self.assertEqual(cm.get_color(4), color.Color(1, 1, 1))
        self.assertEqual(cm[2], color.Color(0.5, 0.5, 0.5))
        self.assertRaises(ValueError, cm.get_color, 5)
        self.assertRaises(ValueError, cm.__getitem__, 5)

    def test_get_colormap_from_palette(self):
        cm = color.get_colormap_from_palette(palette_name="reds", n_colors=5)
        self.assertIsInstance(cm, color.ColorMap)
        self.assertEqual(cm.get_color(2), color.Color(1, 0.5, 0.5))

    def test_random_color(self):
        c = color.random_color()
        self.assertIsInstance(c, color.Color)

    def test_get_value(self):
        value = color.get_value(1, 5)
        self.assertIsInstance(value, float)
        self.assertEqual(value, 0.2)
        value = color.get_value(1, 5, inverse=True)
        self.assertIsInstance(value, float)
        self.assertEqual(value, 0.8)


if __name__ == "__main__":
    unittest.main()
