import unittest

from pykml.factory import KML_ElementMaker as KML

from kmldata import color, styling

from tests import make_data_sample


class TestStylingIntegrationFunctionsWithData(unittest.TestCase):

    def setUp(self):
        self.data = make_data_sample()
        self.opts = styling.StyleOptions(
            icon_colormap=color.ColorMap(
                color_a=color.Color(1, 1, 1),
                color_b=color.Color(1, 1, 1),
                n_colors=1,
            ),
            icon_color="Color",
            icon_shape="airports",
            label_colormap=color.ColorMap(
                color_a=color.Color(1, 1, 1),
                color_b=color.Color(1, 1, 1),
                n_colors=1,
            ),
            label_color="Color",
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

    def setUp(self):
        self.style = styling.StyleOptions(
            icon_colormap=color.ColorMap(
                color_a=color.Color(0, 0, 0),
                color_b=color.Color(1, 1, 1),
                n_colors=4,
            ),
            icon_color="values0",
            icon_shape="airports",
            label_colormap=color.ColorMap(
                color_a=color.Color(0, 0, 0),
                color_b=color.Color(1, 1, 1),
                n_colors=4,
            ),
            label_color="values1",
        )

    def test_icon_colormap(self):
        self.assertIsInstance(self.style.icon_colormap, color.ColorMap)

    def test_icon_color(self):
        self.assertEqual(self.style.icon_color, "values0")
        self.assertIsInstance(self.style.icon_color, str)

    def test_icon_shape(self):
        self.assertEqual(self.style.icon_shape, "airports")

    def test_label_color(self):
        self.assertIsInstance(self.style.label_color, str)

    def test_label_colormap(self):
        self.assertIsInstance(self.style.label_colormap, color.ColorMap)

    def test_json(self):
        j = self.style.json()
        self.assertIsInstance(j, dict)
        self.assertSetEqual(
            set(j.keys()),
            set(
                [
                    "icon_colormap",
                    "icon_color",
                    "icon_shape",
                    "label_colormap",
                    "label_color",
                ],
            )
        )


class TestStylingFunctions(unittest.TestCase):

    def test_random_color(self):
        c = color.random_color()
        self.assertIsInstance(c, color.Color)

    def test_make_style(self):
        ns = "{http://www.opengis.net/kml/2.2}"
        style_name = "style1"
        icon_shape_url = "http://maps.google.com/mapfiles/kml/shapes/airports.png"
        icon_color_hex = "FFFFFF00"
        label_color_hex = "FFFF000000"
        style = styling.make_style(
            style_name=style_name,
            icon_shape="airports",
            icon_color_hex=icon_color_hex,
            label_color_hex=label_color_hex,
        )
        self.assertIsInstance(style, type(KML.Style()))
        self.assertEqual(style.tag, ns + "Style")
        iconstyle = style.find(ns + "IconStyle")
        self.assertEqual(iconstyle.find(ns + "scale"), 1)
        icon = iconstyle.find(ns + "Icon")
        self.assertEqual(icon.find(ns + "href"), icon_shape_url)
        self.assertEqual(iconstyle.find(ns + "color"), icon_color_hex)


if __name__ == "__main__":
    unittest.main()
