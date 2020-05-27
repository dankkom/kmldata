import string

import pandas as pd
import numpy as np


def make_data_sample(N=2 * 10**3, seed=4):
    """Create sample data to use in tests."""
    np.random.seed(seed)
    name = np.random.choice(list(string.ascii_letters), N, replace=True)

    np.random.seed(seed+1)
    lat = np.random.uniform(-80, 80, N)

    np.random.seed(seed+2)
    lon = np.random.uniform(-180, 180, N)

    np.random.seed(seed+3)
    aaa = np.random.choice(list("ABC"), N, replace=True)

    np.random.seed(seed+4)
    bbb = np.random.choice(list("DEF"), N, replace=True)

    np.random.seed(seed+5)
    ccc = np.random.choice(list("GHI"), N, replace=True)

    np.random.seed(seed+6)
    x = np.random.random(N)

    np.random.seed(seed+7)
    y = np.random.random(N)

    np.random.seed(seed+8)
    category = np.random.randint(0, 5, N)

    np.random.seed(seed+9)
    altitude = np.random.randint(0, 100000, N)

    np.random.seed(seed+10)
    values = np.random.randint(0, 1000, N)

    data_sample = pd.DataFrame(
        {
            "name": name,                # str
            "lat": lat,                  # float
            "lon": lon,                  # float
            "AAA": aaa,                  # str
            "BBB": bbb,                  # str
            "CCC": ccc,                  # str
            "x": x,                      # float
            "y": y,                      # float
            "Category": category,        # int
            "Altitude": altitude,        # int
            "values": values,            # int
        },
    )

    return data_sample
