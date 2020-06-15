import os
import urllib.request

from table2kml.helper import load_icon_shapes


if not os.path.exists("icons"):
    os.makedirs("icons")

icon_shapes = load_icon_shapes()
for name in icon_shapes:
    print("Downloading", name)
    url = icon_shapes.get(name)
    data = urllib.request.urlopen(url).read()
    path = os.path.join("icons", "{}.png".format(name))
    with open(path, "wb") as f:
        f.write(data)
