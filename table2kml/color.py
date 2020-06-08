"""Classes for color manipulation."""


import random

import numpy as np


PALETTE = {
    "reds":   ((1, 1, 1), (1, 0, 0)),
    "greens": ((1, 1, 1), (0, 1, 0)),
    "blues":  ((1, 1, 1), (0, 0, 1)),
}


class RGB:
    """Color representation in the RGB color system."""

    __slots__ = ("r", "g", "b")

    def __init__(self, r=0, g=0, b=0):
        self.r = r
        self.g = g
        self.b = b

    def kml_hex(self):
        r = int(self.r * 255)
        g = int(self.g * 255)
        b = int(self.b * 255)
        return f"#FF{b:02X}{g:02X}{r:02X}"

    def __str__(self):
        return self.kml_hex()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.r}, {self.g}, {self.b})"


class ColorInterpolation:

    def __init__(self, color_start: RGB, color_end: RGB, n: int = 5):
        self.set_lim(color_start, color_end, n=n)
        self.set_linspace()

    def set_lim(self, color_start: RGB, color_end: RGB, n=5):
        self.rlim = (color_start.r, color_end.r)
        self.glim = (color_start.g, color_end.g)
        self.blim = (color_start.b, color_end.b)
        self.n = n

    def set_linspace(self):
        self.r = np.linspace(self.rlim[0], self.rlim[1], self.n)
        self.g = np.linspace(self.glim[0], self.glim[1], self.n)
        self.b = np.linspace(self.blim[0], self.blim[1], self.n)

    def get_point(self, n, inverse=False):
        if inverse:
            n = self.n - (n + 1)
        r = self.r[n]
        g = self.g[n]
        b = self.b[n]
        return RGB(r=r, g=g, b=b)

    def __getitem__(self, key):
        if key < 0 or key > self.n:
            raise IndexError()
        return self.get_point(key)


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


def get_color_value(digit: int, n: int, inverse: bool = False) -> int:
    v = digit / n
    if inverse:
        v = 1 - v
    value = int(v * 255)
    return value


def get_color_interpolation(
        palette_name: str,
        n: int = 5,
) -> ColorInterpolation:
    color_start = RGB(*PALETTE.get(palette_name)[0])
    color_end = RGB(*PALETTE.get(palette_name)[1])
    return ColorInterpolation(
        color_start=color_start,
        color_end=color_end,
        n=n,
    )
