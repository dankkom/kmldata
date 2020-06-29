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
    "viridis": (
        (70/255, 0, 85/255),
        (35/255, 140/255, 140/255),
        (1, 230/255, 25/255)
    ),
}


class RGB:
    """Color representation in the RGB color system."""

    __slots__ = ("r", "g", "b")

    def __init__(self, r=0, g=0, b=0):
        self.r = r
        self.g = g
        self.b = b

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
        return self.kml_hex()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.r}, {self.g}, {self.b})"


class ColorInterpolation:
    """Object for calculating color interpolation."""

    def __init__(self, *colors: RGB):
        self.colors = colors
        self.set_colorspace(*colors)

    def set_colorspace(self, *colors):
        """Set the colors for interpolation.

        Parameters
        ----------
        colors : RGB, RGB, ...
            Colors that will be used to get the color interpolation.
        """
        self.r_space = list(c.r for c in colors)
        self.g_space = list(c.g for c in colors)
        self.b_space = list(c.b for c in colors)

    def get_point(self, n: float):
        """Get the color resulting from the interpolation.

        Parameters
        ----------
        n : float
            The point (0, 1.) in colorspace to calculate the interpolated color.

        Returns
        -------
        RGB
            The resulting color object from the interpolation.
        """
        r = interpolate(self.r_space, n)
        g = interpolate(self.g_space, n)
        b = interpolate(self.b_space, n)
        return RGB(r=r, g=g, b=b)

    def __getitem__(self, key):
        if key < 0 or key > self.n:
            raise IndexError()
        return self.get_point(key)

    def __str__(self):
        return f"ColorInterpolation[{' '.join([str(c) for c in self.colors])}]"


def random_color(seed: int = 0) -> str:
    """Generate a random color value for a KML style.

    Parameters
    ----------
    seed : int
        The seed to random generator for reproducible code.

    Returns
    -------
    str
        Random color string.
    """
    random.seed(seed)
    r = hex(random.randint(0, 255))[2:]
    random.seed(seed+1)
    g = hex(random.randint(0, 255))[2:]
    random.seed(seed+2)
    b = hex(random.randint(0, 255))[2:]
    a = "ff"
    return "".join((a, b, g, r)).upper()


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


def get_interpolation(palette_name: str) -> ColorInterpolation:
    """Return a ColorInterpolation object given the palette name.

    Parameters
    ----------
    palette_name : str
        Name of palette to return.

    Returns
    -------
    ColorInterpolation
        An object to get interpolated colors from the palette.
    """
    colors = [RGB(*c) for c in PALETTE.get(palette_name)]
    return ColorInterpolation(*colors)


def interpolate(colorspace, n):
    x = np.linspace(0, 1, len(colorspace))
    return np.interp(x=[n], xp=x, fp=colorspace)[0]
