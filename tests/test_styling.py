import unittest

from pykml.factory import KML_ElementMaker as KML

from table2kml import styling

from . import make_data_sample


class TestStylingIntegrationFuntionsWithData(unittest.TestCase):

    def setUp(self):
        self.data = make_data_sample()

    def test_add_color_digit_column(self):
        new_data = styling.add_color_digit_column(
            df=self.data,
            column_name="values",
            n_colors=5,
        )
        self.assertTrue("ColorDigit" in new_data.columns)

    def test_make_styles(self):
        opts = styling.StyleOptions(
            icon_fmt_name="blues",
            icon_n_colors=5,
            icon_inverse_colors=False,
            icon_shape="http://maps.google.com/mapfiles/kml/shapes/donut.png",
            label_color="FFFFFFFF",
        )
        styling.make_styles(
            data=styling.add_color_digit_column(
                df=self.data,
                column_name="values",
                n_colors=5,
            ),
            opts=opts,
        )


class TestStylingIntegrationFuntions(unittest.TestCase):

    def test_get_color_hue_hex(self):
        value = styling.get_color_hue_hex(
            fmt_name="blues",
            digit=2,
            n=5,
            inverse=False,
        )
        self.assertIsInstance(value, str)
        self.assertEqual(value, "FF66FFFF")


class TestStylingStyleOptionsClass(unittest.TestCase):

    def test_StyleOptions(self):
        opts = styling.StyleOptions(
            icon_fmt_name="blues",
            icon_color="values",
            icon_n_colors=5,
            icon_inverse_colors=False,
            icon_shape="http://maps.google.com/mapfiles/kml/shapes/donut.png",
        )


class TestStylingFunctions(unittest.TestCase):

    def test_random_color(self):
        color = styling.random_color()
        self.assertIsInstance(color, str)
        self.assertTrue(len(color), 8)

    def test_make_style(self):
        ns = "{http://www.opengis.net/kml/2.2}"
        style_name = "style1"
        icon_shape = "http://maps.google.com/mapfiles/kml/shapes/donut.png"
        icon_color = "FFFFFF00"
        label_color = "FFFF000000"
        style = styling.make_style(
            style_name=style_name,
            icon_shape=icon_shape,
            icon_color=icon_color,
            label_color=label_color,
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
            iconstyle.find(ns + "color"), icon_color)

    def test_get_color_value(self):
        value = styling.get_color_value(digit=1, n=5, inverse=False)
        self.assertIsInstance(value, int)
        self.assertEqual(value, 51)

    def test_get_hex(self):
        value = styling.get_hex(51)
        self.assertIsInstance(value, str)
        self.assertEqual(value, "33")

    def test_get_string_format(self):
        string_fmt = styling.get_string_format("blues")
        self.assertIsInstance(string_fmt, str)
        self.assertEqual(string_fmt, "FF{0}FFFF")


if __name__ == "__main__":
    unittest.main()
