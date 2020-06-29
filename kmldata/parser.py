from typing import Dict, Sequence, Union

import numpy as np
import pandas as pd
from pykml import parser
from pykml.factory import KML_ElementMaker as KML


NS = {"t": "http://www.opengis.net/kml/2.2"}


def read_kml(filepath: str) -> KML.kml:
    with open(filepath, "rb") as f:
        root = parser.parse(f).getroot()
    return root


def get_doc(root: KML.kml) -> KML.Document:
    doc = root.xpath("./t:Document", namespaces=NS)[0]
    return doc


def get_folders(doc: KML.Document) -> KML.Folder:
    for folder in doc.xpath("./t:Folder", namespaces=NS):
        yield folder


def get_tree(doc: KML.Document) -> dict:
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
    for folder in doc.xpath("./t:Placemark", namespaces=NS):
        yield folder


def get_SimpleData(placemark: KML.Placemark) -> Dict[str, str]:
    data = {
        simpledata.attrib.get("name"): simpledata.text
        for simpledata in placemark.xpath(".//t:SimpleData", namespaces=NS)
    }
    return data


def get_description(placemark: KML.Placemark) -> str:
    description = placemark.xpath(".//t:description", namespaces=NS)
    return "\n---\n".join(str(d) for d in description)


def get_coordinates(
        placemark: KML.Placemark
) -> Dict[str, float]:
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
    for placemark in placemarks:
        yield dict(
            description=get_description(placemark),
            **get_coordinates(placemark),
            **get_SimpleData(placemark),
        )


def get_data(
        tree: KML,
        folders: Sequence = None
) -> Dict[str, Union[str, float]]:
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


def get_dataframe_from_tree(tree: dict) -> pd.DataFrame:
    data = get_data(tree)
    df = pd.DataFrame.from_records(data)
    return df


def get_dataframe_from_kml(filepath: str) -> pd.DataFrame:
    root = read_kml(filepath)
    doc = get_doc(root)
    tree = get_tree(doc)
    df = get_dataframe_from_tree(tree)
    return df
