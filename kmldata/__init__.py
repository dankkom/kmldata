"""Transform tabular data into KML and vice-versa."""


__version__ = "1.1.0"


from .factory import make_kml, make_kmls, save_kml
from .parser import read_kml_data as read_kml
