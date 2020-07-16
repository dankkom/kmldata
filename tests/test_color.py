import unittest

from kmldata import color


class TestColor(unittest.TestCase):

    def test_Color(self):
        white = color.Color(1, 1, 1)
        black = color.Color(0, 0, 0)
        self.assertEqual(str(white), "#FFFFFFFF")
        self.assertEqual(str(black), "#FF000000")


if __name__ == "__main__":
    unittest.main()
