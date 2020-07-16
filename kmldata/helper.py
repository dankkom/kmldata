import json
from pkg_resources import resource_filename

import numpy as np


def get_digits(array, n):
    """Return an ndarray with bins digits.

    Parameters
    ----------
    array : np.ndarray
        An array of normalized numerical values (0.0 - 1.0) to get the digits.
    n : int
        The number of bins to calculate.

    Returns
    -------
    np.ndarray
        Array of bins digits.
    """
    array = normalize(array)
    bins = np.linspace(0, 1, n+1)
    d = np.digitize(array, bins)
    d[d == n+1] = n
    return d


def normalize(array):
    """Normalize values in an array.

    Parameters
    ----------
    array : np.ndarray
        The array with numerical values to normalize.

    Returns
    -------
    np.ndarray
        Array with normalized values.
    """
    min_value = np.min(array)
    array = array - min_value
    max_value = np.max(array)
    array = array / max_value
    return array


def load_icon_shapes():
    """Load a dict of shape names and its URLs

    Returns
    -------
    dict
        Google's shapes at the Internet
    """
    path = resource_filename(
        "kmldata",
        "icons.json"
    )
    with open(path, "r") as f:
        return json.load(f)
