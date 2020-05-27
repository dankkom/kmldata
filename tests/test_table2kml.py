
# pylint: disable=all

import string
import unittest

import pandas as pd
import numpy as np

import table2kml
from table2kml import styling

from . import make_data_sample


class TestTable2KMLFunctions(unittest.TestCase):

    def setUp(self):
        self.data_sample = make_data_sample()

    def test_make_description(self):
        description = table2kml.make_description(
            row=self.data_sample.iloc[0],
            data_cols=["x", "y"],
        )


class TestTable2KMLIntegration(unittest.TestCase):

    def setUp(self):
        self.data_sample = make_data_sample()
        self.opt = table2kml.Options(
            lat="lat",
            lon="lon",
            data_cols=["x", "y"],
            folders=["AAA", "BBB", "CCC"],
            name="name",
            style={
                "icon_color": "values",
                "icon_fmt_name": "blues",
                "icon_n_colors": 5,
            },
            altitude="Altitude",
        )
        self.data_sample_with_digits = styling.add_color_digit_column(
            df=self.data_sample,
            column_name=self.opt.style.icon_color,
            n_colors=self.opt.style.icon_n_colors,
        )

    def test_make_placemark(self):
        placemark = table2kml.make_placemark(
            row=self.data_sample_with_digits.iloc[0],
            opt=self.opt,
        )

    def test_make_folder(self):
        folder = table2kml.make_folder(
            data=self.data_sample_with_digits,
            name="folder-test",
            opt=self.opt,
        )

    def test_make_kml(self):
        kml = table2kml.make_kml(
            data=self.data_sample,
            opt=self.opt,
        )


if __name__ == "__main__":
    unittest.main()
