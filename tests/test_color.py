import unittest

from kmldata import color


class TestColorInterpolation(unittest.TestCase):

    def test_get_interpolation(self):
        color_interpolation = color.get_interpolation("viridis")
        self.assertIsInstance(color_interpolation, color.ColorInterpolation)

    def test_get_value(self):
        v = color.get_value(5, 10, inverse=False)
        self.assertLessEqual(v, 1)
        self.assertGreaterEqual(v, 0)
        self.assertEqual(v, 0.5)
        self.assertIsInstance(v, float)

    def test_interpolation(self):
        color_start = color.RGB(1, 0, 1)
        color_end = color.RGB(0.25, 0.75, 0.5)
        interpolation = color.ColorInterpolation(color_start, color_end)
        result_point = interpolation.get_point(0.2)
        self.assertEqual(str(result_point), "#FFE526D8")
        self.assertIsInstance(result_point, color.RGB)


class TestRGB(unittest.TestCase):

    def test_RGB(self):
        white = color.RGB(1, 1, 1)
        black = color.RGB(0, 0, 0)
        self.assertEqual(str(white), "#FFFFFFFF")
        self.assertEqual(str(black), "#FF000000")


if __name__ == "__main__":
    unittest.main()
