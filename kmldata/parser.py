import numpy as np
from pykml import parser


NS = {"t": "http://www.opengis.net/kml/2.2"}


def read_kml(filepath):
    with open(filepath, "rb") as f:
        root = parser.parse(f).getroot()
    return root


def get_doc(root):
    doc = root.xpath("./t:Document", namespaces=NS)[0]
    return doc


def get_folders(doc):
    for folder in doc.xpath("./t:Folder", namespaces=NS):
        yield folder


def get_tree(doc):
    folders = {folder.name: folder for folder in get_folders(doc)}
    for folder_name in folders:
        subfolders = get_tree(folders[folder_name])
        if len(subfolders) > 0:
            folders[folder_name] = subfolders
    placemarks = list(get_placemarks(doc))
    if placemarks:
        folders["placemarks"] = placemarks
    return folders


def get_placemarks(doc):
    for folder in doc.xpath("./t:Placemark", namespaces=NS):
        yield folder


def get_SimpleData(placemark):
    data = {
        simpledata.attrib.get("name"): simpledata.text
        for simpledata in placemark.xpath(".//t:SimpleData", namespaces=NS)
    }
    return data


def get_description(placemark):
    description = placemark.xpath(".//t:description", namespaces=NS)
    return "\n---\n".join(str(d) for d in description)


def get_coordinates(placemark):
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


def get_placemarks_data(placemarks):
    for placemark in placemarks:
        yield dict(
            description=get_description(placemark),
            **get_SimpleData(placemark),
        )


def get_data(tree, folders=None):
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
