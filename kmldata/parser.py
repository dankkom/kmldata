"""Extract KML data into DataFrame."""


from typing import Dict, Sequence, Union

import numpy as np
import pandas as pd
from pykml import parser
from pykml.factory import KML_ElementMaker as KML


NS = {"t": "http://www.opengis.net/kml/2.2"}


def read_kml(filepath: str) -> KML.kml:
    """Read a KML file.

    Parameters
    ----------
    filepath : str
        Path to the file to read.

    Returns
    -------
    KML.kml
        Root of a KML document.
    """
    with open(filepath, "rb") as f:
        root = parser.parse(f).getroot()
    return root


def get_doc(root: KML.kml) -> KML.Document:
    """Get the document of a KML file.

    Parameters
    ----------
    root : KML.kml
        Root of a KML document.

    Returns
    -------
    KML.Document
        Document of a KML file.
    """
    doc = root.xpath("./t:Document", namespaces=NS)[0]
    return doc


def get_folders(doc: KML.Document) -> KML.Folder:
    """Yield folder object children in a KML node.

    Parameters
    ----------
    doc : KML.Document
        A KML node.

    Yields
    ------
    KML.Folder
        A KML Folder object.
    """
    for folder in doc.xpath("./t:Folder", namespaces=NS):
        yield folder


def get_tree(doc: KML.Document) -> dict:
    """Return a dictionary with the data of a KML.Document.

    Parameters
    ----------
    doc : KML.Document
        A KML node with data.

    Returns
    -------
    dict
        Data of a KML.Document.
    """
    folders = {folder.name: folder for folder in get_folders(doc)}
    for folder_name in folders:
        subfolders = get_tree(folders[folder_name])
        if len(subfolders) > 0:
            folders[folder_name] = subfolders
    placemarks = list(get_placemarks(doc))
    if placemarks:
        folders["placemarks"] = placemarks
    return folders


def get_placemarks(doc: KML.Document) -> KML.Placemark:
    """Yield placemark object children in a KML node.

    Parameters
    ----------
    doc : KML.Document
        A KML node.

    Yields
    ------
    KML.Placemark
        A KML Placemark object.
    """
    for placemark in doc.xpath("./t:Placemark", namespaces=NS):
        yield placemark


def get_points(placemark: KML.Placemark) -> KML.LineString:
    for point in placemark.xpath("./t:Point", namespaces=NS):
        yield point


def get_line_strings(placemark: KML.Placemark) -> KML.LineString:
    for line_string in placemark.xpath("./t:LineString", namespaces=NS):
        yield line_string


def get_polygons(placemark: KML.Placemark) -> KML.Polygon:
    for polygon in placemark.xpath("./t:Polygon", namespaces=NS):
        yield polygon


def get_geometry_coordinates(element: Union[KML.LineString, KML.LinearRing]):
    text = element.coordinates.text
    coord = [
        tuple(float(j) for j in i.strip().split(","))
        for i in text.split("\n")
    ]
    return coord


def get_SimpleData(placemark: KML.Placemark) -> Dict[str, str]:
    """Return data from SimpleData KML fields in a placemark.

    Parameters
    ----------
    placemark : KML.Placemark
        A Placemark object.

    Returns
    -------
    dict
        A dictionary with the data from placemark.
    """
    data = {
        simpledata.attrib.get("name"): simpledata.text
        for simpledata in placemark.xpath(".//t:SimpleData", namespaces=NS)
    }
    return data


def get_description(placemark: KML.Placemark) -> str:
    """Return string with description from a placemark.

    Parameters
    ----------
    placemark : KML.Placemark
        A Placemark object.

    Returns
    -------
    str
        String representing the Placemark description.
    """
    description = placemark.xpath(".//t:description", namespaces=NS)
    return "\n---\n".join(str(d) for d in description)


def get_coordinates(placemark: KML.Placemark) -> Dict[str, float]:
    """Return dict with coordinates of Placemark.

    Parameters
    ----------
    placemark : KML.Placemark
        A KML Placemark with coordinates to get.

    Returns
    -------
    Dict[str, float]
        A dictionary with the coordinates of the Placemark.
    """
    if hasattr(placemark, "Point"):
        if hasattr(placemark.Point, "coordinates"):
            lon, lat, alt = placemark.Point.coordinates.text.split(",")
            return {
                "Latitude": float(lat),
                "Longitude": float(lon),
                "Altitude": float(alt),
            }
    return {
        "Latitude": np.nan,
        "Longitude": np.nan,
        "Altitude": np.nan,
    }


def get_placemarks_data(
        placemarks: Sequence[KML.Placemark]
) -> Dict[str, Union[str, float]]:
    """Get data from a sequence of placemarks.

    Parameters
    ----------
    placemarks : Sequence[KML.Placemark]
        A list or tuple of placemarks to get its data.

    Yields
    ------
    dict
        A dict with the data of placemarks.
    """
    for placemark in placemarks:
        yield dict(
            description=get_description(placemark),
            **get_coordinates(placemark),
            **get_SimpleData(placemark),
        )


def get_data(
        tree: dict,
        folders: Sequence[str] = None
) -> Dict[str, Union[str, float]]:
    """Yield data for each placemark in a tree.

    Parameters
    ----------
    tree : dict
        A dictionary from get_tree().
    folders : Sequence
        A sequence with names of folders to include in the returned data.

    Yields
    ------
    Dict[str, Union[str, float]]
        A dictionary with all data for a placemark in the given tree.
    """
    if folders is None:
        folders = tuple()
    for node in tree:
        if node == "placemarks":
            for pdata in get_placemarks_data(tree[node]):
                yield dict(
                    **{f"Folder{i}": f for i, f in enumerate(folders)},
                    **pdata,
                )
        else:
            yield from get_data(
                tree=tree[node],
                folders=tuple([*folders, str(node)]),
            )


def get_dataframe_from_tree(tree: dict) -> pd.core.frame.DataFrame:
    """Get a dataframe from a tree dict of a KML document.

    Parameters
    ----------
    tree : dict
        Tree of a KML document, given by get_tree() function.

    Returns
    -------
    pd.core.frame.DataFrame
        A DataFrame with data from the tree.
    """
    data = get_data(tree)
    df = pd.DataFrame.from_records(data)
    return df


def read_kml_data(filepath: str) -> pd.core.frame.DataFrame:
    """Read a KML file, returning its data as a Pandas DataFrame.

    Parameters
    ----------
    filepath : str
        Path of the KML file to read and parse.

    Returns
    -------
    pd.core.frame.DataFrame
        A DataFrame with data from the KML file.
    """
    root = read_kml(filepath)
    doc = get_doc(root)
    tree = get_tree(doc)
    df = get_dataframe_from_tree(tree)
    return df
