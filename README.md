# kmldata - transform table data into a KML file and vice versa

![tests](https://github.com/dkkomesu/kmldata/workflows/tests/badge.svg?branch=master) [![Coverage Status](https://coveralls.io/repos/github/dkkomesu/kmldata/badge.svg?branch=master)](https://coveralls.io/github/dkkomesu/kmldata?branch=master)

## Installation

`kmldata` isn't published on PyPI yet. Install it from GitHub repository:

```shell
pip install git+https://github.com/dkkomesu/kmldata#egg=kmldata
```

## Usage

First import `kmldata`

```python
import kmldata
```

We can transform a Pandas DataFrame into a KML file.

```python
import pandas as pd


data = pd.read_csv("data.csv")
opt = kmldata.Options(
    lat="Latitude",
    lon="Longitude",
    altitude="Altitude",
)
kml = kmldata.make_kml(data, opt)
kmldata.save_kml(kml, "data.kml")
```

```python
df = kmldata.read_kml("data.kml")
```

## License

This package is licensed under GNU GPLv3.
