
from typing import List

import pandas as pd
from pykml.factory import KML_ElementMaker as KML

from table2kml.helper import get_digits, load_icon_shapes, normalize
from table2kml import color


class StyleOptions:

    def __init__(self, **kwargs):
        self.ICON_SHAPES = load_icon_shapes()
        self.icon_color_palette = None
        self.icon_color = None
        self.icon_n_colors = 1
        self.icon_inverse_colors = False
        self.icon_shape = self.ICON_SHAPES["donut"]
        self.label_color_palette = None
        self.label_color = None
        self.label_n_colors = 1
        self.label_inverse_colors = False
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
        label_color: str,
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

    icon_color_interpolation = color.get_interpolation(
        palette_name=opts.icon_color_palette,
    )
    label_color_interpolation = color.get_interpolation(
        palette_name=opts.label_color_palette,
    )

    it = data[
        [
            "IconColorDigit",
            "LabelColorDigit",
        ]
    ].drop_duplicates().itertuples()

    for row in it:
        icon_digit = row[1]
        label_digit = row[2]

        icon_color = str(
            icon_color_interpolation.get_point(
                n=color.get_value(
                    icon_digit-1,
                    opts.icon_n_colors,
                    inverse=opts.icon_inverse_colors,
                ),
            )
        )
        label_color = str(
            label_color_interpolation.get_point(
                n=color.get_value(
                    label_digit-1,
                    opts.label_n_colors,
                    inverse=opts.label_inverse_colors,
                ),
            )
        )

        style = make_style(
            style_name=get_style_name_from_digits(icon_digit, label_digit),
            icon_shape=opts.icon_shape,
            icon_color=icon_color,
            label_color=label_color,
        )
        styles.append(style)

    return styles


def add_color_digit_column(
        df: pd.DataFrame,
        opts: StyleOptions,
) -> pd.DataFrame:
    """Add columns for icon and label digit colors."""
    if opts.icon_color:
        normal_values = normalize(df[opts.icon_color])
        icon_digits = get_digits(normal_values, n=opts.icon_n_colors)
    else:
        icon_digits = 1
    if opts.label_color:
        normal_values = normalize(df[opts.label_color])
        label_digits = get_digits(normal_values, n=opts.label_n_colors)
    else:
        label_digits = 1
    return df.assign(IconColorDigit=icon_digits, LabelColorDigit=label_digits)


def get_style_url_from_row(row):
    return f"#color_{row['IconColorDigit']-1}-{row['LabelColorDigit']-1}"


def get_style_name_from_digits(icon_digit, label_digit):
    return f"color_{icon_digit-1}-{label_digit-1}"
