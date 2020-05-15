"""Transform an Excel file to a KML file
"""


import json
import os
import random

import pandas as pd
import pykml
from lxml import etree
from pykml.factory import KML_ElementMaker as KML


with open("icons.json", "r") as f:
    ICON_SHAPES = json.load(f)


class Options:
    def __init__(self, lat, lon, **kwargs):
        self.lat = lat
        self.lon = lon
        # List of column names that will be added in point's description
        self.data_cols = []
        # Point names by value in column `name_col`
        self.name = None
        # Separate points in folders by values in column `folder_col`
        self.folders = []
        # Color points by value in column `color_col`
        self.color = None
        # Altitude of points (relative to ground) by value in column `height_col`
        self.altitude = None
        self.shape = ICON_SHAPES["donut"]
        for key in kwargs:
            self.__setattr__(key, kwargs[key])


def make_description(row, data_cols):
    description = KML.description(
        "\n".join([f"{col}: {row[col]}" for col in data_cols])
    )
    return description


def make_point(row, opt):
    lat, lon = row[opt.lat], row[opt.lon]
    placemark = KML.Placemark()
    if opt.name:
        placemark.append(KML.name(row[opt.name]))
    # Point
    altitude = row[opt.altitude] if opt.altitude is not None else 0
    point = KML.Point(KML.coordinates(f"{lon},{lat},{altitude}"))
    alt_mode = KML.altitudeMode("relativeToGround")
    point.append(alt_mode)
    placemark.append(point)
    # Style
    if opt.color is not None:
        style_url = "#" + opt.color + "_" + str(row[opt.color])
        placemark.append(KML.styleUrl(style_url))
    description = make_description(row, opt.data_cols)
    placemark.append(description)
    return placemark


def make_folder(data, name, opt):
    folder = KML.Folder(KML.name(name))
    for i in range(data.shape[0]):
        row = data.iloc[i]
        point = make_point(row, opt)
        folder.append(point)
    return folder


def make_tree(parent, data, folders, opt):
    for l0 in data[folders[0]].unique():
        data0 = data[data[folders[0]] == l0]
        if len(folders) > 1:
            f0 = KML.Folder(KML.name(folders[0] + ": " + str(l0)))
            f0 = make_tree(
                parent=f0,
                data=data0,
                folders=folders[1:],
                opt=opt,
            )
        else:
            f0 = make_folder(
                data=data0,
                name=folders[0] + ": " + str(l0),
                opt=opt,
            )
        parent.append(f0)
    return parent


def make_style(style_name, icon_shape, icon_color, label_color):
    style = KML.Style()

    icon_style = KML.IconStyle(
        KML.scale(1),
        KML.Icon(
            KML.href(icon_shape)
        ),
        KML.color(icon_color)
    )
    label_style = KML.LabelStyle(
        KML.color(label_color)
    )

    style.append(icon_style)
    style.append(label_style)

    style.set("id", str(style_name))

    return style


def random_color():
    r = hex(random.randint(0, 255))[2:]
    g = hex(random.randint(0, 255))[2:]
    b = hex(random.randint(0, 255))[2:]
    a = "ff"
    return "".join((a, b, g, r)).upper()


def make_styles(data, icon_color_col, icon_shape, label_color="FFFFFFFF"):
    styles = []
    for name in data[icon_color_col].unique():
        icon_color = random_color()
        style = make_style(
            style_name=icon_color_col + "_" + str(name),
            icon_shape=icon_shape,
            icon_color=icon_color,
            label_color=label_color,
        )
        styles.append(style)
    return styles


def make_kml(data, opt, doc_name="Default"):
    kml = KML.kml()
    doc = KML.Document(KML.name(doc_name))
    kml.append(doc)

    if opt.color is not None:
        styles = make_styles(data, opt.color, icon_shape=opt.shape)
        for style in styles:
            doc.append(style)

    if opt.folders is not None:
        doc = make_tree(
            parent=doc,
            data=data,
            folders=opt.folders,
            opt=opt,
        )
        return kml

    for i in range(data.shape[0]):
        row = data.iloc[i]
        placemark = make_point(row, opt)
        doc.append(placemark)
    return kml


def save_kml(kml, filepath):
    with open(filepath, "wb") as f:
        f.write(etree.tostring(kml, pretty_print=True))
