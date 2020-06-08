
# pylint: disable=all

import string
import unittest

import pandas as pd
import numpy as np

import table2kml
from table2kml import styling

from tests import make_data_sample


class TestTable2KMLFunctions(unittest.TestCase):

    def setUp(self):
        self.data_sample = make_data_sample()

    def test_make_description(self):
        description = table2kml.make_description(
            row=self.data_sample.iloc[0],
            data_cols=["values0", "values1"],
        )


class TestTable2KMLIntegration(unittest.TestCase):

    def setUp(self):
        self.data_sample = make_data_sample()
        self.opts = table2kml.Options(
            lat="lat",
            lon="lon",
            data_cols=["values0", "values1"],
            folders=["Folder1", "Folder2", "Folder3"],
            name="name",
            style={
                "icon_color": "Color",
                "icon_color_palette": "blues",
                "icon_n_colors": 5,
                "label_color": "Color",
                "label_color_palette": "reds",
                "label_n_colors": 5,
                "label_inverse_colors": True,
            },
            altitude="Altitude",
        )
        self.data_sample_with_digits = styling.add_color_digit_column(
            df=self.data_sample,
            opts=self.opts.style,
        )

    def test_make_placemark(self):
        placemark = table2kml.make_placemark(
            row=self.data_sample_with_digits.iloc[0],
            opt=self.opts,
        )

    def test_make_kml(self):
        kml = table2kml.make_kml(
            data=self.data_sample,
            opt=self.opts,
        )


if __name__ == "__main__":
    unittest.main()
