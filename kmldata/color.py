"""Classes and functions to work with colors."""


import random

import numpy as np


PALETTE = {
    "reds": ((1, 1, 1), (1, 0, 0)),
    "yellows": ((1, 1, 1), (1, 1, 0)),
    "greens": ((1, 1, 1), (0, 1, 0)),
    "cyans": ((1, 1, 1), (0, 1, 1)),
    "blues": ((1, 1, 1), (0, 0, 1)),
    "magentas": ((1, 1, 1), (1, 0, 1)),
}


class Color:
    """Color representation in the RGB color system."""

    __slots__ = ("r", "g", "b")

    def __init__(self, r: float = 0, g: float = 0, b: float = 0):
        for v in (r, g, b):
            if v > 1:
                raise ValueError(
                    "Color components values must be between 0-1\n"
                    f"Values passed: {r}, {g}, {b}"
                )
            if v < 0:
                raise ValueError(
                    "Color components values must be between 0-1\n"
                    f"Values passed: {r}, {g}, {b}"
                )
        self.r, self.g, self.b = float(r), float(g), float(b)

    def kml_hex(self):
        """Get hexadecimal string code for RGB color in KML format.

        Returns
        -------
        str
            String with hexadecimal code of the color.
        """
        r = int(self.r * 255)
        g = int(self.g * 255)
        b = int(self.b * 255)
        return f"#FF{b:02X}{g:02X}{r:02X}"

    def __str__(self):
        return f"{self.__class__.__name__}({self.r}, {self.g}, {self.b})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.r}, {self.g}, {self.b})"

    def __eq__(self, o):
        r = self.r == o.r
        g = self.g == o.g
        b = self.b == o.b
        return r and g and b


class ColorMap:

    def __init__(self, color_a, color_b, n_colors):
        self.color_a = color_a
        self.color_b = color_b
        self.n_colors = n_colors
        self.calculate_mapping()

    def calculate_mapping(self):
        r = np.linspace(self.color_a.r, self.color_b.r, self.n_colors)
        g = np.linspace(self.color_a.g, self.color_b.g, self.n_colors)
        b = np.linspace(self.color_a.b, self.color_b.b, self.n_colors)
        self.mapping = {
            i: Color(r=r[i], g=g[i], b=b[i])
            for i in range(self.n_colors)
        }

    def get_color(self, digit: int) -> Color:
        if digit not in self.mapping:
            raise ValueError(f"Invalid digit value: {digit}")
        return self.mapping[digit]

    def __getitem__(self, digit: int):
        return self.get_color(digit)


def get_colormap_from_palette(palette_name, n_colors):
    palette = PALETTE.get(palette_name, ((0, 0, 0), (1, 1, 1)))
    color_a = Color(*palette[0])
    color_b = Color(*palette[1])
    cm = ColorMap(color_a, color_b, n_colors)
    return cm


def random_color(seed: int = 0) -> Color:
    """Generate a random color object for a KML style.

    Parameters
    ----------
    seed : int
        The seed to random generator for reproducible code.

    Returns
    -------
    Color
        Random color object.
    """
    random.seed(seed)
    r = random.random()
    random.seed(seed + 1)
    g = random.random()
    random.seed(seed + 2)
    b = random.random()
    return Color(r=r, g=g, b=b)


def get_value(digit: int, n: int, inverse: bool = False) -> float:
    """Return a value between 0-1 given `digit` and `n`.

    Parameters
    ----------
    digit : int
        Position in the linear space that will be returned.
    n : int
        The size o linear space.
    inverse : bool
        If True returns the inverse value of `digit` position in linear space.

    Returns
    -------
    float
        Number that equals `digit / n` or `1 - digit / n` when `inverse=True`.
    """
    v = digit / n
    if inverse:
        v = 1 - v
    return v
