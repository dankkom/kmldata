import os


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
