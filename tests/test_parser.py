import os
import unittest

import pandas as pd
from pykml.factory import KML_ElementMaker as KML

import kmldata
from kmldata import parser


class TestParser(unittest.TestCase):

    def setUp(self):
        self.kml = KML.kml(
            KML.Document(
                KML.Folder(
                    KML.name("Folder0"),
                    KML.Placemark(
                        KML.name("Placemark0"),
                        KML.Point(KML.coordinates("0,0,0")),
                        KML.altitudeMode("relativeToGround"),
                        KML.styleUrl("#style_test"),
                        KML.description("Description: test placemark 0"),
                        KML.ExtendedData(
                            KML.SchemaData(
                                KML.SimpleData("TEST0").set("name", "test0"),
                            ),
                        ),
                    ),
                    KML.Placemark(
                        KML.name("Placemark1"),
                        KML.Point(KML.coordinates("0,0,0")),
                        KML.altitudeMode("relativeToGround"),
                        KML.styleUrl("#style_test"),
                        KML.description("Description: test placemark 1"),
                        KML.ExtendedData(
                            KML.SchemaData(
                                KML.SimpleData("TEST1").set("name", "test1"),
                            ),
                        ),
                    )
                ),
                KML.Folder(
                    KML.name("Folder1"),
                    KML.Placemark(
                        KML.name("Placemark0"),
                        KML.Point(KML.coordinates("0,0,0")),
                        KML.altitudeMode("relativeToGround"),
                        KML.styleUrl("#style_test"),
                        KML.description("Description: test placemark 0"),
                        KML.ExtendedData(
                            KML.SchemaData(
                                KML.SimpleData("TEST0").set("name", "test0"),
                            ),
                        ),
                    ),
                    KML.Placemark(
                        KML.name("Placemark1"),
                        KML.Point(KML.coordinates("0,0,0")),
                        KML.altitudeMode("relativeToGround"),
                        KML.styleUrl("#style_test"),
                        KML.description("Description: test placemark 1"),
                        KML.ExtendedData(
                            KML.SchemaData(
                                KML.SimpleData("TEST1").set("name", "test1"),
                            ),
                        ),
                    )
                )
            )
        )
        kmldata.save_kml(self.kml, "Default.kml")

    def test_read_kml(self):
        parser.read_kml

    def test_get_doc(self):
        parser.get_doc(self.kml)

    def test_get_folders(self):
        doc = parser.get_doc(self.kml)
        folders = parser.get_folders(doc)
        for folder in folders:
            self.assertIsInstance(folder, KML.Folder().__class__)

    def test_get_tree(self):
        doc = parser.get_doc(self.kml)
        tree = parser.get_tree(doc)
        self.assertIsInstance(tree, dict)

    def test_get_placemarks(self):
        doc = parser.get_doc(self.kml)
        for folder in parser.get_folders(doc):
            placemarks = parser.get_placemarks(folder)
            for placemark in placemarks:
                self.assertIsInstance(
                    placemark,
                    KML.Placemark().__class__,
                )

    def test_get_data(self):
        doc = parser.get_doc(self.kml)
        tree = parser.get_tree(doc)
        data = parser.get_data(tree)
        for row in data:
            self.assertIsInstance(row, dict)

    def test_get_dataframe_from_tree(self):
        doc = parser.get_doc(self.kml)
        tree = parser.get_tree(doc)
        df = parser.get_dataframe_from_tree(tree)
        self.assertIsInstance(df, pd.core.frame.DataFrame)

    def test_read_kml_data(self):
        df = parser.read_kml_data("Default.kml")
        self.assertIsInstance(df, pd.core.frame.DataFrame)

    def tearDown(self):
        os.remove("Default.kml")


class TestParserIntegration(unittest.TestCase):

    def setUp(self):
        self.placemark = KML.Placemark(
            KML.name("Test Placemark"),
            KML.Point(KML.coordinates("0,0,0")),
            KML.altitudeMode("relativeToGround"),
            KML.styleUrl("#style_test"),
            KML.description("Description: test placemark"),
            KML.ExtendedData(
                KML.SchemaData(
                    KML.SimpleData("TEST").set("name", "test"),
                ),
            ),
        )

    def test_get_SimpleData(self):
        sd = parser.get_SimpleData(self.placemark)
        self.assertIsInstance(sd, dict)

    def test_get_description(self):
        description = parser.get_description(self.placemark)
        self.assertIsInstance(description, str)

    def test_get_coordinates(self):
        coordinates = parser.get_coordinates(self.placemark)
        self.assertIsInstance(coordinates, dict)

    def test_get_placemarks_data(self):
        data = parser.get_placemarks_data([self.placemark, self.placemark])
        for i in data:
            self.assertIsInstance(i, dict)


if __name__ == "__main__":
    unittest.main()
