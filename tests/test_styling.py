import unittest

from pykml.factory import KML_ElementMaker as KML

from kmldata import color, styling

from tests import make_data_sample


class TestStylingIntegrationFuntionsWithData(unittest.TestCase):

    def setUp(self):
        self.data = make_data_sample()
        self.opts = styling.StyleOptions(
            icon_color_palette="blues",
            icon_color="Color",
            icon_n_colors=5,
            icon_inverse_colors=False,
            icon_shape="http://maps.google.com/mapfiles/kml/shapes/donut.png",
            label_color_palette="reds",
            label_color="Color",
            label_n_colors=5,
            label_inverse_colors=True,
        )

    def test_add_color_digit_column(self):
        new_data = styling.add_color_digit_column(df=self.data, opts=self.opts)
        self.assertTrue("IconColorDigit" in new_data.columns)
        self.assertTrue("LabelColorDigit" in new_data.columns)

    def test_make_styles(self):
        styling.make_styles(
            data=styling.add_color_digit_column(
                df=self.data,
                opts=self.opts,
            ),
            opts=self.opts,
        )


class TestStylingStyleOptionsClass(unittest.TestCase):

    def test_StyleOptions(self):
        styling.StyleOptions(
            icon_fmt_name="blues",
            icon_color="values0",
            icon_n_colors=5,
            icon_inverse_colors=False,
            icon_shape="donut",
        )


class TestStylingFunctions(unittest.TestCase):

    def test_random_color(self):
        c = color.random_color()
        self.assertIsInstance(c, color.Color)

    def test_make_style(self):
        ns = "{http://www.opengis.net/kml/2.2}"
        style_name = "style1"
        icon_shape = "http://maps.google.com/mapfiles/kml/shapes/donut.png"
        icon_color_hex = "FFFFFF00"
        label_color_hex = "FFFF000000"
        style = styling.make_style(
            style_name=style_name,
            icon_shape=icon_shape,
            icon_color_hex=icon_color_hex,
            label_color_hex=label_color_hex,
        )
        self.assertIsInstance(style, type(KML.Style()))
        self.assertEqual(style.tag, ns + "Style")
        iconstyle = style.find(ns + "IconStyle")
        self.assertEqual(
            iconstyle.find(ns + "scale"), 1)
        icon = iconstyle.find(ns + "Icon")
        self.assertEqual(
            icon.find(ns + "href"), icon_shape)
        self.assertEqual(
            iconstyle.find(ns + "color"), icon_color_hex)


if __name__ == "__main__":
    unittest.main()
