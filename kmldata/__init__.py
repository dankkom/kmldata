"""Transform an Excel file to a KML file

Group the placemarks by folders, color & shapes based on values in the table

"""


# pylint: disable=invalid-name


import pandas as pd
from lxml import etree
from pykml.factory import KML_ElementMaker as KML
from . import styling


__author__ = "Daniel K. Komesu"
__author_email__ = "danielkomesu@gmail.com"
__version__ = "0.3.0"


class Options:
    """An object to store options passed to the functions in this module

    Required parameters
    -------------------
    lat, lon : float
        The column names of a Pandas DataFrame coordinates (latitude, longitude)
    """

    def __init__(self, lat, lon, **kwargs):
        self.style = styling.StyleOptions()
        self.lat = lat
        self.lon = lon
        # List of column names that will be added in point's description
        self.data_cols = []
        # Point names by value in column
        self.name = None
        # Separate points in folders by values in column
        self.folders = []
        # Altitude of points (relative to ground) by value in column
        self.altitude = None
        # Create separate KML files for different values in a column
        self.files = None
        for key in kwargs:
            if key == "style":
                for style_key in kwargs[key]:
                    self.style.__setattr__(style_key, kwargs[key][style_key])
            else:
                self.__setattr__(key, kwargs[key])

    def json(self):
        j = {
            k: v for k, v in self.__dict__.items()
            if not k.startswith("_") and not k.isupper() and isinstance(k, str)
        }
        j.update({"style": self.style.json()})
        return j

    def __str__(self):
        return "{} object".format(self.__class__.__name__)

    def __repr__(self):
        return "{} object".format(self.__class__.__name__)


def make_description(row: pd.core.series.Series, data_cols) -> KML.description:
    """Create a description KML object with the data in row[data_cols]

    Parameters
    ----------
    row : pd.core.series.Series
        A row of dataframe with the information to use in the description text
    data_cols : list
        A list of columns in the row

    Returns
    -------
    KML.description
        The KML description object
    """
    description = KML.description(
        "\n".join([f"{col}: {row[col]}" for col in data_cols])
    )
    return description


def make_placemark(row: pd.core.series.Series, opt: Options) -> KML.Placemark:
    """Create a placemark KML object with data in `row` and configuration in opt

    Parameters
    ----------
    row : pd.core.series.Series, dict, namedtuple
        An iterable with values accessible by a key
    opt : Options
        The options to use as parameters

    Returns
    -------
    KML.Placemark
        A KML placemark object
    """
    lat, lon = row[opt.lat], row[opt.lon]
    placemark = KML.Placemark()
    if opt.name:
        placemark.append(KML.name(row[opt.name]))
    # Point
    altitude = row[opt.altitude] if opt.altitude else 0
    point = KML.Point(KML.coordinates(f"{lon},{lat},{altitude}"))
    alt_mode = KML.altitudeMode("relativeToGround")
    point.append(alt_mode)
    placemark.append(point)
    # Style
    style_url = styling.get_style_url_from_row(row)
    placemark.append(KML.styleUrl(style_url))
    description = make_description(row, opt.data_cols)
    placemark.append(description)
    return placemark


def get_folder(element: KML.Folder, folder_path: list) -> KML.Folder:
    name = folder_path[0]
    folder_name = element.xpath(
        f"./t:Folder/*[text()='{name}']",
        namespaces={"t": "http://www.opengis.net/kml/2.2"},
    )
    if len(folder_name) == 0:
        folder = KML.Folder(KML.name(name))
        element.append(folder)
    else:
        folder = folder_name[0].getparent()
    if len(folder_path) > 1:
        folder = get_folder(folder, folder_path[1:])
    return folder


def make_kml(data: pd.core.frame.DataFrame, opt: Options,
             doc_name: str = "Default") -> KML.kml:
    """Create a KML object with data and opt configuration

    Parameters
    ----------
    data : pd.core.frame.DataFrame
        A Pandas DataFrame with the data to use as input
    opt : Options
        An Options instance with the configuration to output the KML
    doc_name : str, optional
        The document name of KML object, by default "Default"

    Returns
    -------
    pykml.KML
        The resulting KML object
    """
    kml = KML.kml()
    doc = KML.Document(KML.name(doc_name))
    kml.append(doc)

    data = styling.add_color_digit_column(df=data, opts=opt.style)
    styles = styling.make_styles(data=data, opts=opt.style)
    for style in styles:
        doc.append(style)

    for i in range(data.shape[0]):
        row = data.iloc[i]
        placemark = make_placemark(row, opt)
        if opt.folders:
            folder = get_folder(doc, row[opt.folders])
            folder.append(placemark)
        else:
            doc.append(placemark)
    return kml


def make_kmls(data: pd.core.frame.DataFrame, opt: Options) -> dict:
    """Create multiple KML with the column name given in opt

    Parameters
    ----------
    data : pd.core.frame.DataFrame
        A Pandas DataFrame with the data to use as input
    opt : Options
        An Options instance with the configuration to output the KML

    Returns
    -------
    dict
        A dict qith the resulting KMLs objects, with columns' values as keys
    """
    kml_dict = {}
    if opt.files:
        for i in data[opt.files].unique():
            dd = data.loc[data[opt.files] == i]
            kml = make_kml(dd, opt, doc_name=i)
            kml_dict[i] = kml
    else:
        kml = make_kml(data, opt)
        kml_dict["Default"] = kml
    return kml_dict


def save_kml(kml: KML.kml, filepath: str):
    """Save a KML object to a file

    Parameters
    ----------
    kml : KML.kml
        The object to save
    filepath : str
        Path to save the file
    """
    # pylint: disable=c-extension-no-member
    with open(filepath, "wb") as f:
        f.write(b"""<?xml version="1.0" encoding="UTF-8"?>\n""")
        f.write(etree.tostring(kml, pretty_print=True))
