import unittest

import numpy as np

from table2kml import helper


class TestHelperFunctions(unittest.TestCase):

    def setUp(self):
        self.array = np.random.randint(0, 100, 10000)

    def test_get_digits(self):
        digits = helper.get_digits(array=self.array, n=5)
        self.assertIsInstance(digits, np.ndarray)

    def test_normalize(self):
        normalized = helper.normalize(self.array)
        self.assertLessEqual(np.max(normalized), 1)
        self.assertGreaterEqual(np.min(normalized), 0)


class TestHelperFunctionsPkgResources(unittest.TestCase):

    def test_load_icon_shapes(self):
        icon_shapes = helper.load_icon_shapes()
        self.assertIsInstance(icon_shapes, dict)


if __name__ == "__main__":
    unittest.main()
