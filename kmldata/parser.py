import lxml.etree as ET
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
