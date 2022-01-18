from kmldata.factory import Options, make_kmls, save_kml
from kmldata.helper import load_icon_shapes
from kmldata.color import get_colormap_from_palette


from __init__ import make_data_sample


data_sample = make_data_sample(N=1000)
data_sample.to_csv("data_sample.csv", index=False)
data_sample.to_excel("data_sample.xlsx", index=False)
shapes = load_icon_shapes()
opt = Options(
    lat="lat",
    lon="lon",
    data_cols=[
        "name",
        "Folder1",
        "Folder2",
        "Folder3",
        "Color",
        "Category",
        "Altitude",
        "values0",
        "values1",
        "Files",
        "Description",
    ],
    folders=["Folder1", "Folder2", "Folder3"],
    name="name",
    files="Files",
    style={
        "icon_color": "Color",
        "icon_colormap": get_colormap_from_palette("reds", 1),
        "icon_shape": "arrow",
        "label_color": "Color",
        "label_colormap": get_colormap_from_palette("reds", 1),
    },
    altitude="Altitude",
    size=2,
)
kml_dict = make_kmls(data_sample, opt)
for name in kml_dict:
    save_kml(kml_dict[name], f"{name}.kml")
