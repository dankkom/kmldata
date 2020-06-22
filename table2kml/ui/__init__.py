"""GUI for table2kml"""


import os
from pkg_resources import resource_filename
import pprint
import sys

import numpy as np
import pandas as pd

from PySide2 import QtCore
from PySide2.QtCore import QUrl
from PySide2.QtGui import (
    QDesktopServices,
    QIcon,
    QPixmap,
)
from PySide2.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog,
    QListWidgetItem,
    QMainWindow,
)

import table2kml
from table2kml.helper import load_icon_shapes

from .ui_aboutwindow import Ui_AboutWindow
from .ui_mainwindow import Ui_MainWindow
from .ui_selecticonwindow import Ui_SelectIconWindow


url_license = "https://github.com/dkkomesu/table2kml/blob/master/LICENSE"
url_source_code = "https://github.com/dkkomesu/table2kml"


class About(QDialog, Ui_AboutWindow):

    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(
            QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)


class SelectIcon(QDialog, Ui_SelectIconWindow):

    def __init__(self, icons, parent=None):
        super(SelectIcon, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(
            QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
        self.icons = icons
        self.add_icons()
        self.pushButtonCancel.clicked.connect(self.cancel)
        self.pushButtonOk.clicked.connect(self.confirm)
        self.selected_icon = None

    def add_icons(self):
        for icon_name in self.icons:
            pixmap = get_icon_pixmap(icon_name)
            icon = QIcon(pixmap)
            item = QListWidgetItem(icon, icon_name)
            self.listWidgetSelectIcon.addItem(item)

    def confirm(self):
        self.selected_icon = self.listWidgetSelectIcon.currentItem().text()
        self.close()

    def cancel(self):
        self.selected_icon = None
        self.close()


class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.dirpath = None
        self.pushButtonOpenFile.clicked.connect(self.file_dialog_open)
        self.pushButtonMakeKML.clicked.connect(self.make_kml)
        self.pushButtonSelectIcon.clicked.connect(self.select_icon_window)
        self.actionOpenFile.triggered.connect(self.file_dialog_open)
        self.actionExit.triggered.connect(self.close_application)
        self.actionLicense.triggered.connect(self.view_license)
        self.actionSourceCode.triggered.connect(self.view_source_code)
        self.actionAbout.triggered.connect(self.about_window)
        self.icons = load_icon_shapes()
        self.change_selected_icon_shape("donut")

    def change_selected_icon_shape(self, name):
        """Change icon shape image"""
        pixmap = get_icon_pixmap(name)
        self.labelSelectedIconShape.setPixmap(pixmap)
        self.labelSelectedIconShape.setScaledContents(True)
        self.selected_icon = name

    def change_label_open_file(self, text):
        self.labelOpenFile.setText(text)

    # DATA FILE METHODS
    def get_columns(self):
        columns = [
            (name, ty)
            for name, ty in zip(self.data.dtypes.index, self.data.dtypes)
        ]
        return columns

    def open_data_file(self, filepath):
        self.data = pd.read_excel(filepath)
        self.columns = self.get_columns()
        self.groupBoxOptions.setEnabled(True)
        self.groupBoxStyleOptions.setEnabled(True)
        self.fill_combobox_description()
        self.fill_combobox_latitude()
        self.fill_combobox_longitude()
        self.fill_combobox_name()
        self.fill_combobox_altitude()
        self.fill_combobox_folders()
        self.fill_combobox_files()

        # Style options
        self.fill_combobox_color()
        self.fill_combobox_label_color()

    # ------------------------------OTHER WINDOWS-------------------------------
    def file_dialog_open(self):
        filepath, _ = QFileDialog.getOpenFileName()
        if filepath:
            self.open_data_file(filepath)
            self.change_label_open_file(filepath)
            self.dirpath = os.path.dirname(filepath)

    def select_icon_window(self):
        self.select_icon = SelectIcon(icons=self.icons)
        self.select_icon.exec_()
        selected = self.select_icon.selected_icon
        if selected:
            self.change_selected_icon_shape(selected)

    def about_window(self):
        about = About()
        about.exec_()

    # ---------------------------------ACTIONS----------------------------------
    def close_application(self):
        self.close()

    def view_license(self):
        url = QUrl(url_license)
        QDesktopServices.openUrl(url)

    def view_source_code(self):
        url = QUrl(url_source_code)
        QDesktopServices.openUrl(url)

    # --------------------------FILL COMBOBOX METHODS---------------------------
    def fill_combobox_description(self):
        self.comboBoxDescription.clear()
        items = [""] + [name for name, _ in self.columns[1:]]
        self.comboBoxDescription.addItems(items)

    def fill_combobox_latitude(self):
        self.comboBoxLatitude.clear()
        items = [name for name, ty in self.columns if ty is np.dtype("float64")]
        self.comboBoxLatitude.addItems(items)

    def fill_combobox_longitude(self):
        self.comboBoxLongitude.clear()
        items = [name for name, ty in self.columns if ty is np.dtype("float64")]
        self.comboBoxLongitude.addItems(items)

    def fill_combobox_name(self):
        self.comboBoxName.clear()
        items = [""] + [name for name, _ in self.columns]
        self.comboBoxName.addItems(items)

    def fill_combobox_altitude(self):
        self.comboBoxAltitude.clear()
        items = [""] + [
            name for name, ty in self.columns
            if ty is np.dtype("float64") or ty is np.dtype("int64")
        ]
        self.comboBoxAltitude.addItems(items)

    def fill_combobox_folders(self):
        self.comboBoxFolders.clear()
        items = [""] + [name for name, _ in self.columns]
        self.comboBoxFolders.addItems(items)

    def fill_combobox_files(self):
        self.comboBoxFiles.clear()
        items = [""] + [
            name for name, ty in self.columns
            if ty is not np.dtype("float64") and ty is not np.dtype("int64")
        ]
        self.comboBoxFiles.addItems(items)

    def fill_combobox_color(self):
        self.comboBoxColorColumn.clear()
        items = [""] + [
            name for name, ty in self.columns
            if ty is np.dtype("float64") or ty is np.dtype("int64")
        ]
        self.comboBoxColorColumn.addItems(items)
        self.fill_combobox_palette()

    def fill_combobox_palette(self):
        self.comboBoxColorPalette.clear()
        self.comboBoxColorPalette.addItems(
            [
                "reds",
                "yellows",
                "greens",
                "cyans",
                "blues",
                "magentas",
                "viridis",
            ]
        )

    def fill_combobox_label_color(self):
        self.comboBoxLabelColorColumn.clear()
        items = [""] + [
            name for name, ty in self.columns
            if ty is np.dtype("float64") or ty is np.dtype("int64")
        ]
        self.comboBoxLabelColorColumn.addItems(items)
        self.fill_combobox_label_palette()

    def fill_combobox_label_palette(self):
        self.comboBoxLabelColorPalette.clear()
        self.comboBoxLabelColorPalette.addItems(
            [
                "reds",
                "yellows",
                "greens",
                "cyans",
                "blues",
                "magentas",
                "viridis",
            ]
        )

    # ---------------------------------MAKE KML---------------------------------
    def get_options(self):
        options = dict(
            lat=self.comboBoxLatitude.currentText(),
            lon=self.comboBoxLongitude.currentText(),
            name=self.comboBoxName.currentText(),
            data_cols=[self.comboBoxDescription.currentText()],
            altitude=self.comboBoxAltitude.currentText(),
            folders=self.comboBoxFolders.currentText(),
            files=self.comboBoxFiles.currentText(),
            style=dict(
                icon_color=self.comboBoxColorColumn.currentText(),
                icon_color_palette=self.comboBoxColorPalette.currentText(),
                icon_n_colors=self.spinBoxBinNumber.value(),
                icon_shape=self.icons.get(self.selected_icon),
                icon_inverse_colors=self.checkBoxInverseColor.isChecked(),
                label_color=self.comboBoxLabelColorColumn.currentText(),
                label_color_palette=self.comboBoxLabelColorPalette.currentText(),
                label_n_colors=self.spinBoxLabelBinNumber.value(),
                label_inverse_colors=self.checkBoxLabelInverseColor.isChecked(),
            ),
        )
        opts = table2kml.Options(**options)
        return opts

    def make_kml(self):
        options = self.get_options()
        kmls = table2kml.make_kmls(self.data, options)
        for kml_name in kmls:
            table2kml.save_kml(
                kmls[kml_name],
                os.path.join(
                    self.dirpath,
                    f"{kml_name}.kml",
                )
            )


def get_icon_pixmap(name):
    """Get icon shape image"""
    path = resource_filename("table2kml.ui", f"icons/{name}.png")
    with open(path, "rb") as f:
        data = f.read()
    pixmap = QPixmap()
    pixmap.loadFromData(data)
    return pixmap
