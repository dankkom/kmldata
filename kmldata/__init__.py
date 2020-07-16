"""Transform tabular data into KML and vice-versa."""


__version__ = "1.1.2"


from .factory import Options, make_kml, make_kmls, save_kml
from .parser import read_kml_data as read_kml
