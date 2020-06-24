
# pylint: disable=all


import unittest

from pykml.factory import KML_ElementMaker as KML

from kmldata import (
    Options,
    make_description,
    make_kml,
    make_kmls,
    make_placemark,
    styling,
)

from tests import make_data_sample


class TestTable2KMLFunctions(unittest.TestCase):

    def setUp(self):
        self.data_sample = make_data_sample()

    def test_make_description(self):
        description = make_description(
            row=self.data_sample.iloc[0],
            data_cols=["values0", "values1"],
        )
        self.assertIsInstance(description, KML.description().__class__)


class TestTable2KMLIntegration(unittest.TestCase):

    def setUp(self):
        self.data_sample = make_data_sample()
        self.opts = Options(
            lat="lat",
            lon="lon",
            data_cols=["values0", "values1"],
            folders=["Folder1", "Folder2", "Folder3"],
            name="name",
            files="Files",
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
        placemark = make_placemark(
            row=self.data_sample_with_digits.iloc[0],
            opt=self.opts,
        )
        self.assertIsInstance(placemark, KML.placemark().__class__)

    def test_make_kml(self):
        kml = make_kml(
            data=self.data_sample,
            opt=self.opts,
        )
        self.assertIsInstance(kml, KML.kml().__class__)

    def test_make_kmls(self):
        kmls_dict = make_kmls(
            data=self.data_sample,
            opt=self.opts,
        )
        self.assertIsInstance(kmls_dict, dict)


if __name__ == "__main__":
    unittest.main()
