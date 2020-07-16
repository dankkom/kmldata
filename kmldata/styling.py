"""Styling KML Placemarks.

This module contains classes and functions to add styles to Placemarks in a KML
file based on the data from a Pandas DataFrame.

The styles options are set and passed to the functions with the `StyleOptions`
container class.
"""


from typing import List

import pandas as pd
from pykml.factory import KML_ElementMaker as KML

from .helper import get_digits, load_icon_shapes
from . import color


ICON_SHAPES = load_icon_shapes()
ICON_DIGIT = "IconColorDigit"
LABEL_DIGIT = "LabelColorDigit"
DEFAULT_ICON_SHAPE_URL = "http://maps.google.com/mapfiles/kml/shapes/donut.png"


class StyleOptions:
    """Options to pass style to KML maker functions."""

    def __init__(self, **kwargs):
        self.icon_color_palette = "viridis"
        self.icon_color = None  # Column name for color
        self.icon_n_colors = 1
        self.icon_inverse_colors = False
        self.icon_shape = "donut"
        self.label_color_palette = "viridis"
        self.label_color = None  # Column name for color
        self.label_n_colors = 1
        self.label_inverse_colors = False
        for key in kwargs:
            self.__setattr__(key, kwargs[key])

    def json(self) -> dict:
        """Get options as a (JSON-like) dictionary."""
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
        icon_color_hex: str,
        label_color_hex: str,
) -> KML.Style:
    """Create a KML style object with the given parameters.

    Parameters
    ----------
    style_name : str
        The name of style.
    icon_shape : str
        Name of the image to use as icon.
    icon_color_hex : str
        Hex color code for the icon.
    label_color_hex : str
        Hex color code for the label.

    Returns
    -------
    KML.Style
        The style with the specified settings.
    """
    style = KML.Style()

    icon_style = KML.IconStyle(
        KML.scale(1),
        KML.Icon(
            KML.href(
                ICON_SHAPES.get(
                    icon_shape,
                    DEFAULT_ICON_SHAPE_URL
                )
            )
        ),
        KML.color(icon_color_hex)
    )
    label_style = KML.LabelStyle(
        KML.color(label_color_hex)
    )

    style.append(icon_style)
    style.append(label_style)

    style.set("id", str(style_name))

    return style


def make_styles(
        data: pd.core.frame.DataFrame,
        opts: StyleOptions,
) -> List[KML.Style]:
    """Create a list of styles accordingly the data and StyleOptions.

    `data` is expected to have a IconColorDigit and a LabelColorDigit column,
    added by `add_color_digit_column()` function.

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

    icon_cm = color.get_colormap_from_palette(
        palette_name=opts.icon_color_palette,
        n_colors=opts.icon_n_colors,
    )
    label_cm = color.get_colormap_from_palette(
        palette_name=opts.label_color_palette,
        n_colors=opts.label_n_colors,
    )

    it = data[[ICON_DIGIT, LABEL_DIGIT]].drop_duplicates().itertuples()

    for row in it:
        icon_digit = row[1]
        label_digit = row[2]
        style_name = get_style_name_from_digits(icon_digit, label_digit)

        icon_color_hex = icon_cm.get_color(digit=icon_digit-1).kml_hex()
        label_color_hex = label_cm.get_color(digit=label_digit-1).kml_hex()

        style = make_style(
            style_name=style_name,
            icon_shape=opts.icon_shape,
            icon_color_hex=icon_color_hex,
            label_color_hex=label_color_hex,
        )
        styles.append(style)

    return styles


def add_color_digit_column(
        df: pd.core.frame.DataFrame,
        opts: StyleOptions,
) -> pd.core.frame.DataFrame:
    """Add digit columns for icon and label colors.

    Parameters
    ----------
    df : pd.core.frame.DataFrame
        A dataframe.
    opts : StyleOptions
        Style options.

    Returns
    -------
    pd.core.frame.DataFrame
        Dataframe with IconColorDigit and LabelColorDigit columns.
    """
    if opts.icon_color:
        icon_digits = get_digits(df[opts.icon_color], n=opts.icon_n_colors)
    else:
        icon_digits = 1
    if opts.label_color:
        label_digits = get_digits(df[opts.icon_color], n=opts.label_n_colors)
    else:
        label_digits = 1
    return df.assign(
        **{
            ICON_DIGIT: icon_digits,
            LABEL_DIGIT: label_digits,
        }
    )


def get_style_url_from_row(row: pd.core.series.Series) -> str:
    """Get style string url from row with digits.

    Parameters
    ----------
    row : pd.core.series.Series
        A row of a dataframe with digits to get the style string from.

    Returns
    -------
    str
        The style string URL to refer to the style.
    """
    return f"#color_{row[ICON_DIGIT]-1}-{row[LABEL_DIGIT]-1}"


def get_style_name_from_digits(icon_digit: int, label_digit: int) -> str:
    """Get style string url from digits.

    Parameters
    ----------
    icon_digit : int
        Number identifier for icon style.
    label_digit : int
        Number identifier for label style.

    Returns
    -------
    str
        Style string URL.
    """
    return f"color_{icon_digit-1}-{label_digit-1}"
