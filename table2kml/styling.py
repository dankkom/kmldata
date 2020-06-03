import random
from typing import List

import pandas as pd
import numpy as np
from pykml.factory import KML_ElementMaker as KML

from table2kml.helper import get_digits, load_icon_shapes, normalize


_STR_FMT = {
    "reds": "FFFFFF{0}",
    "greens": "FFFF{0}FF",
    "blues": "FF{0}FFFF",
    "yellows": "FFFF{0}{0}",
    "magentas": "FF{0}FF{0}",
    "cyans": "FF{0}{0}FF",
}


class StyleOptions:

    def __init__(self, **kwargs):
        self.ICON_SHAPES = load_icon_shapes()
        self.icon_fmt_name = None
        self.label_fmt_name = None
        self.icon_color = None
        self.label_color = None
        self.icon_n_colors = None
        self.label_n_colors = None
        self.icon_inverse_colors = False
        self.label_inverse_colors = False
        self.icon_shape = self.ICON_SHAPES["donut"]
        for key in kwargs:
            self.__setattr__(key, kwargs[key])

    def json(self):
        j = {
            k: v for k, v in self.__dict__.items()
            if not k.startswith("_") and not k.isupper() and isinstance(k, str)
        }
        return j

    def __str__(self):
        return "{} object".format(self.__class__.__name__)

    def __repr__(self):
        return "{} object".format(self.__class__.__name__)

        
def make_style(
        style_name: str,
        icon_shape: str,
        icon_color: str,
        label_color: str
    ) -> KML.Style:
    """Create a KML style object with the given parameters

    Parameters
    ----------
    style_name : str
        The name of style
    icon_shape : str
        URL of the image to use as icon
    icon_color : str
        Hex color code for the icon
    label_color : str
        Hex color code for the label

    Returns
    -------
    KML.Style
        The style with the specified settings
    """
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


def random_color(seed: int = 0) -> str:
    """Generate a random color value for a KML style

    Parameters
    ----------
    seed : int
        The seed to random generator for reproducible code

    Returns
    -------
    str
        Random color string value
    """
    random.seed(seed)
    r = hex(random.randint(0, 255))[2:]
    random.seed(seed+1)
    g = hex(random.randint(0, 255))[2:]
    random.seed(seed+2)
    b = hex(random.randint(0, 255))[2:]
    a = "ff"
    return "".join((a, b, g, r)).upper()


def make_styles(
        data: pd.core.frame.DataFrame,
        opts: StyleOptions,
    ) -> List[KML.Style]:
    """Create a list of styles accordingly the data and StyleOptions.

    data is expected to have a ColorDigit column, added by
    add_color_digit_column() function.

    Parameters
    ----------
    data : pd.core.frame.DataFrame
        The Pandas DataFrame to use as input for the styles
    opts : StyleOptions
        StyleOptions to make styles

    Returns
    -------
    list
        A list of styles to append to a KML document
    """
    styles = []
    for digit in data["ColorDigit"].unique():
        icon_color = get_color_hue_hex(
            fmt_name=opts.icon_fmt_name,
            digit=digit,
            n=opts.icon_n_colors,
            inverse=opts.icon_inverse_colors,
        )
        style = make_style(
            style_name= "color_" + str(digit),
            icon_shape=opts.icon_shape,
            icon_color=icon_color,
            label_color=opts.label_color,
        )
        styles.append(style)
    return styles


def add_color_digit_column(
        df: pd.DataFrame,
        column_name: str,
        n_colors: int,
    ) -> pd.DataFrame:
    normal_values = normalize(df[column_name])
    digits = get_digits(normal_values, n=n_colors)
    return df.assign(ColorDigit=digits)


def get_color_value(digit: int, n: int, inverse: bool = False) -> int:
    v = digit / n
    if inverse:
        v = 1 - v
    value = int(v * 255)
    return value


def get_hex(value: int) -> str:
    return hex(value)[2:].upper()


def get_color_hue_hex(
        fmt_name: str,
        digit: int,
        n: int,
        inverse: bool = False,
    ) -> str:
    return get_string_format(fmt_name).format(
        get_hex(get_color_value(digit, n, inverse=inverse))
    )


def get_string_format(fmt_name: str) -> str:
    return _STR_FMT[fmt_name]
