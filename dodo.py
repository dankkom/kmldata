import os
import urllib.request

from table2kml.helper import load_icon_shapes


def task_compile_ui_files():
    dependencies = (
        "aboutWindow.ui",
        "mainWindow.ui",
        "selectIconWindow.ui",
    )
    targets = (
        "ui_aboutwindow.py",
        "ui_mainwindow.py",
        "ui_selecticonwindow.py",
    )
    for dependency, target in zip(dependencies, targets):
        yield {
            "name": dependency,
            "file_dep": [os.path.join("designer", dependency)],
            "targets": [os.path.join("table2kml", "ui", target)],
            "actions": ["pyside2-uic %(dependencies)s > %(targets)s"],
        }


def task_compile_qrc_image():
    return {
        "file_dep": [os.path.join("designer", "image.qrc")],
        "targets": [os.path.join("table2kml", "ui", "image_rc.py")],
        "actions": ["pyside2-rcc %(dependencies)s -o %(targets)s"],
    }


def correct_imports(filepath):
    with open(filepath, "r") as f:
        contents = f.read()
    contents = contents.replace("import image_rc", "from . import image_rc")
    with open(filepath, "w") as f:
        f.write(contents)


def task_correct_imports():
    files = [
        os.path.join("table2kml", "ui", "ui_mainwindow.py"),
        os.path.join("table2kml", "ui", "ui_aboutwindow.py"),
        os.path.join("table2kml", "ui", "ui_selecticonwindow.py"),
    ]
    return {
        "file_dep": files,
        "actions": [(correct_imports, [file]) for file in files]
    }


def download_icon(url, name, icon_dir_path):
    if not os.path.exists(icon_dir_path):
        os.makedirs(icon_dir_path)
    data = urllib.request.urlopen(url).read()
    path = os.path.join(icon_dir_path, "{}.png".format(name))
    with open(path, "wb") as f:
        f.write(data)


def task_download_icons():
    icon_dir_path = os.path.join("table2kml", "ui", "icons")
    icon_shapes = load_icon_shapes()
    for name in icon_shapes:
        url = icon_shapes.get(name)
        yield {
            "name": name,
            "targets": [os.path.join(icon_dir_path, f"{name}.png")],
            "actions": [(download_icon, (url, name, icon_dir_path))]
        }
