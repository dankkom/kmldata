import string

import pandas as pd
import numpy as np


def make_data_sample(N=2 * 10**3, seed=4):
    """Create sample data to use in tests."""
    np.random.seed(seed)
    name = np.random.choice(list(string.ascii_letters), N, replace=True)

    np.random.seed(seed+1)
    lat = np.random.uniform(0, -23, N)

    np.random.seed(seed+2)
    lon = np.random.uniform(-45, -70, N)

    np.random.seed(seed+3)
    folder1 = np.random.choice(list("ABC"), N, replace=True)

    np.random.seed(seed+4)
    folder2 = np.random.choice(list("DEF"), N, replace=True)

    np.random.seed(seed+5)
    folder3 = np.random.choice(list("GHI"), N, replace=True)

    np.random.seed(seed+6)
    color = np.random.random(N)

    np.random.seed(seed+7)
    category = np.random.randint(0, 5, N)

    np.random.seed(seed+8)
    altitude = np.random.randint(0, 100000, N)

    np.random.seed(seed+9)
    values0 = np.random.randint(0, 1000, N)

    np.random.seed(seed+10)
    values1 = np.random.randint(0, 1000, N)

    np.random.seed(seed+11)
    files = np.random.choice(list("UVWXYZ"), N, replace=True)

    np.random.seed(seed+12)
    description = np.random.choice(list("KLMNOPQ"), N, replace=True)

    data_sample = pd.DataFrame(
        {
            "name": name,                # str
            "lat": lat,                  # float
            "lon": lon,                  # float
            "Folder1": folder1,          # str
            "Folder2": folder2,          # str
            "Folder3": folder3,          # str
            "Color": color,              # float
            "Category": category,        # int
            "Altitude": altitude,        # int
            "values0": values0,          # int
            "values1": values1,          # int
            "Files": files,              # str
            "Description": description,  # str
        },
    )

    return data_sample
