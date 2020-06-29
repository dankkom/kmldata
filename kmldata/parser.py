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
    return folders


def get_placemarks(doc):
    for folder in doc.xpath("./t:Placemark", namespaces=NS):
        yield folder


def get_leafs(doc):
    folders = {folder.name: folder for folder in get_folders(doc)}
    for folder_name in folders:
        subfolders = get_leafs(folders[folder_name])
        if len(subfolders) > 0:
            folders[folder_name] = subfolders
    placemarks = list(get_placemarks(doc))
    if placemarks:
        folders["placemarks"] = placemarks
    return folders


def get_SimpleData(placemark):
    data = {
        simpledata.attrib.get("name"): simpledata.text
        for simpledata in placemark.xpath(".//t:SimpleData", namespaces=NS)
    }
    return data


def get_description(placemark):
    description = placemark.xpath(".//t:description", namespaces=NS)
    return description
