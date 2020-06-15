# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from . import image_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/images/images/xltokml-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"")
        self.actionOpenFile = QAction(MainWindow)
        self.actionOpenFile.setObjectName(u"actionOpenFile")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionLicense = QAction(MainWindow)
        self.actionLicense.setObjectName(u"actionLicense")
        self.actionSourceCode = QAction(MainWindow)
        self.actionSourceCode.setObjectName(u"actionSourceCode")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"font-size: 16px;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameHeader = QFrame(self.centralwidget)
        self.frameHeader.setObjectName(u"frameHeader")
        self.frameHeader.setMinimumSize(QSize(0, 60))
        self.frameHeader.setMaximumSize(QSize(16777215, 60))
        self.frameHeader.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.frameHeader.setFrameShape(QFrame.NoFrame)
        self.frameHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameHeader)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(30, 0, 30, 0)
        self.labelOpenFile = QLabel(self.frameHeader)
        self.labelOpenFile.setObjectName(u"labelOpenFile")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelOpenFile.sizePolicy().hasHeightForWidth())
        self.labelOpenFile.setSizePolicy(sizePolicy1)
        self.labelOpenFile.setMaximumSize(QSize(16777215, 40))
        self.labelOpenFile.setStyleSheet(u"")
        self.labelOpenFile.setFrameShape(QFrame.Box)
        self.labelOpenFile.setMargin(0)
        self.labelOpenFile.setIndent(10)

        self.horizontalLayout.addWidget(self.labelOpenFile)

        self.pushButtonOpenFile = QPushButton(self.frameHeader)
        self.pushButtonOpenFile.setObjectName(u"pushButtonOpenFile")
        self.pushButtonOpenFile.setMinimumSize(QSize(150, 40))
        self.pushButtonOpenFile.setMaximumSize(QSize(16777215, 40))
        self.pushButtonOpenFile.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(200,  0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 100, 100);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButtonOpenFile)


        self.verticalLayout.addWidget(self.frameHeader)

        self.frameContent = QFrame(self.centralwidget)
        self.frameContent.setObjectName(u"frameContent")
        self.frameContent.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QGroupBox {\n"
"	border: 1px solid rgb(200, 200, 200);\n"
"	margin-top: 10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top center;\n"
"}\n"
"")
        self.frameContent.setFrameShape(QFrame.NoFrame)
        self.frameContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frameContent)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBoxOptions = QGroupBox(self.frameContent)
        self.groupBoxOptions.setObjectName(u"groupBoxOptions")
        self.groupBoxOptions.setEnabled(False)
        sizePolicy.setHeightForWidth(self.groupBoxOptions.sizePolicy().hasHeightForWidth())
        self.groupBoxOptions.setSizePolicy(sizePolicy)
        self.groupBoxOptions.setStyleSheet(u"")
        self.groupBoxOptions.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBoxOptions.setFlat(False)
        self.groupBoxOptions.setCheckable(False)
        self.formLayout_2 = QFormLayout(self.groupBoxOptions)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(-1, 18, -1, -1)
        self.labelLatitude = QLabel(self.groupBoxOptions)
        self.labelLatitude.setObjectName(u"labelLatitude")
        self.labelLatitude.setMinimumSize(QSize(0, 0))
        self.labelLatitude.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.labelLatitude)

        self.comboBoxLatitude = QComboBox(self.groupBoxOptions)
        self.comboBoxLatitude.setObjectName(u"comboBoxLatitude")
        self.comboBoxLatitude.setMinimumSize(QSize(0, 0))
        self.comboBoxLatitude.setMaximumSize(QSize(16777215, 16777215))
        self.comboBoxLatitude.setStyleSheet(u"")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBoxLatitude)

        self.labelLongitude = QLabel(self.groupBoxOptions)
        self.labelLongitude.setObjectName(u"labelLongitude")
        self.labelLongitude.setMinimumSize(QSize(0, 0))
        self.labelLongitude.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.labelLongitude)

        self.comboBoxLongitude = QComboBox(self.groupBoxOptions)
        self.comboBoxLongitude.setObjectName(u"comboBoxLongitude")
        self.comboBoxLongitude.setMinimumSize(QSize(0, 0))
        self.comboBoxLongitude.setMaximumSize(QSize(16777215, 16777215))
        self.comboBoxLongitude.setStyleSheet(u"")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBoxLongitude)

        self.labelName = QLabel(self.groupBoxOptions)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setMinimumSize(QSize(0, 0))
        self.labelName.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.labelName)

        self.comboBoxName = QComboBox(self.groupBoxOptions)
        self.comboBoxName.setObjectName(u"comboBoxName")
        self.comboBoxName.setMinimumSize(QSize(0, 0))
        self.comboBoxName.setMaximumSize(QSize(16777215, 16777215))
        self.comboBoxName.setStyleSheet(u"")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.comboBoxName)

        self.labelDesciption = QLabel(self.groupBoxOptions)
        self.labelDesciption.setObjectName(u"labelDesciption")
        self.labelDesciption.setMinimumSize(QSize(0, 0))
        self.labelDesciption.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.labelDesciption)

        self.comboBoxDescription = QComboBox(self.groupBoxOptions)
        self.comboBoxDescription.setObjectName(u"comboBoxDescription")
        self.comboBoxDescription.setMinimumSize(QSize(0, 0))
        self.comboBoxDescription.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.comboBoxDescription)

        self.labelAltitude = QLabel(self.groupBoxOptions)
        self.labelAltitude.setObjectName(u"labelAltitude")
        self.labelAltitude.setMinimumSize(QSize(0, 0))
        self.labelAltitude.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.labelAltitude)

        self.comboBoxAltitude = QComboBox(self.groupBoxOptions)
        self.comboBoxAltitude.setObjectName(u"comboBoxAltitude")
        self.comboBoxAltitude.setMinimumSize(QSize(0, 0))
        self.comboBoxAltitude.setMaximumSize(QSize(16777215, 16777215))
        self.comboBoxAltitude.setStyleSheet(u"")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.comboBoxAltitude)

        self.labelFiles = QLabel(self.groupBoxOptions)
        self.labelFiles.setObjectName(u"labelFiles")
        self.labelFiles.setMinimumSize(QSize(0, 0))
        self.labelFiles.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.labelFiles)

        self.comboBoxFiles = QComboBox(self.groupBoxOptions)
        self.comboBoxFiles.setObjectName(u"comboBoxFiles")
        self.comboBoxFiles.setMinimumSize(QSize(0, 0))
        self.comboBoxFiles.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.comboBoxFiles)

        self.comboBoxFolders = QComboBox(self.groupBoxOptions)
        self.comboBoxFolders.setObjectName(u"comboBoxFolders")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.comboBoxFolders)

        self.labelFolders = QLabel(self.groupBoxOptions)
        self.labelFolders.setObjectName(u"labelFolders")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.labelFolders)


        self.horizontalLayout_3.addWidget(self.groupBoxOptions)

        self.groupBoxStyleOptions = QGroupBox(self.frameContent)
        self.groupBoxStyleOptions.setObjectName(u"groupBoxStyleOptions")
        self.groupBoxStyleOptions.setEnabled(False)
        self.groupBoxStyleOptions.setCheckable(True)
        self.groupBoxStyleOptions.setChecked(False)
        self.formLayout = QFormLayout(self.groupBoxStyleOptions)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, 18, -1, -1)
        self.labelIconColor = QLabel(self.groupBoxStyleOptions)
        self.labelIconColor.setObjectName(u"labelIconColor")
        self.labelIconColor.setMinimumSize(QSize(0, 0))
        self.labelIconColor.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelIconColor)

        self.widgetColorSelection = QWidget(self.groupBoxStyleOptions)
        self.widgetColorSelection.setObjectName(u"widgetColorSelection")
        self.widgetColorSelection.setMinimumSize(QSize(0, 0))
        self.widgetColorSelection.setSizeIncrement(QSize(0, 0))
        self.gridLayout = QGridLayout(self.widgetColorSelection)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBoxColorPalette = QComboBox(self.widgetColorSelection)
        self.comboBoxColorPalette.setObjectName(u"comboBoxColorPalette")
        self.comboBoxColorPalette.setMaximumSize(QSize(16777215, 16777215))
        self.comboBoxColorPalette.setStyleSheet(u"")
        self.comboBoxColorPalette.setEditable(False)

        self.gridLayout.addWidget(self.comboBoxColorPalette, 1, 0, 1, 1)

        self.comboBoxColorColumn = QComboBox(self.widgetColorSelection)
        self.comboBoxColorColumn.setObjectName(u"comboBoxColorColumn")
        self.comboBoxColorColumn.setMaximumSize(QSize(16777215, 16777215))
        self.comboBoxColorColumn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.comboBoxColorColumn, 0, 0, 1, 1)

        self.spinBoxBinNumber = QSpinBox(self.widgetColorSelection)
        self.spinBoxBinNumber.setObjectName(u"spinBoxBinNumber")
        self.spinBoxBinNumber.setMinimumSize(QSize(0, 0))
        self.spinBoxBinNumber.setMaximumSize(QSize(16777215, 16777215))
        self.spinBoxBinNumber.setStyleSheet(u"")
        self.spinBoxBinNumber.setMinimum(1)
        self.spinBoxBinNumber.setMaximum(10)

        self.gridLayout.addWidget(self.spinBoxBinNumber, 0, 1, 1, 1)

        self.checkBoxInverseColor = QCheckBox(self.widgetColorSelection)
        self.checkBoxInverseColor.setObjectName(u"checkBoxInverseColor")
        self.checkBoxInverseColor.setMinimumSize(QSize(0, 0))
        self.checkBoxInverseColor.setMaximumSize(QSize(16777215, 16777215))
        self.checkBoxInverseColor.setStyleSheet(u"")

        self.gridLayout.addWidget(self.checkBoxInverseColor, 1, 1, 1, 1)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.widgetColorSelection)

        self.labelIconShape = QLabel(self.groupBoxStyleOptions)
        self.labelIconShape.setObjectName(u"labelIconShape")
        self.labelIconShape.setMinimumSize(QSize(0, 0))
        self.labelIconShape.setSizeIncrement(QSize(0, 35))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelIconShape)

        self.widgetIconShapeSelection = QWidget(self.groupBoxStyleOptions)
        self.widgetIconShapeSelection.setObjectName(u"widgetIconShapeSelection")
        self.horizontalLayout_5 = QHBoxLayout(self.widgetIconShapeSelection)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.labelSelectedIconShape = QLabel(self.widgetIconShapeSelection)
        self.labelSelectedIconShape.setObjectName(u"labelSelectedIconShape")
        self.labelSelectedIconShape.setMinimumSize(QSize(50, 50))
        self.labelSelectedIconShape.setMaximumSize(QSize(50, 50))
        self.labelSelectedIconShape.setStyleSheet(u"")
        self.labelSelectedIconShape.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.labelSelectedIconShape)

        self.pushButtonSelectIcon = QPushButton(self.widgetIconShapeSelection)
        self.pushButtonSelectIcon.setObjectName(u"pushButtonSelectIcon")
        self.pushButtonSelectIcon.setMinimumSize(QSize(0, 0))
        self.pushButtonSelectIcon.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.pushButtonSelectIcon)


        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.widgetIconShapeSelection)


        self.horizontalLayout_3.addWidget(self.groupBoxStyleOptions)


        self.verticalLayout.addWidget(self.frameContent)

        self.frameFooter = QFrame(self.centralwidget)
        self.frameFooter.setObjectName(u"frameFooter")
        self.frameFooter.setMinimumSize(QSize(0, 60))
        self.frameFooter.setMaximumSize(QSize(16777215, 60))
        self.frameFooter.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.frameFooter.setFrameShape(QFrame.NoFrame)
        self.frameFooter.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameFooter)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(30, 0, 30, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButtonMakeKML = QPushButton(self.frameFooter)
        self.pushButtonMakeKML.setObjectName(u"pushButtonMakeKML")
        self.pushButtonMakeKML.setMinimumSize(QSize(150, 40))
        self.pushButtonMakeKML.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(200,  0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 100, 100);\n"
"}")
        self.pushButtonMakeKML.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButtonMakeKML)


        self.verticalLayout.addWidget(self.frameFooter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionOpenFile)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionLicense)
        self.menuAbout.addAction(self.actionSourceCode)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ExcelToKML App", None))
        self.actionOpenFile.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About this app", None))
        self.actionLicense.setText(QCoreApplication.translate("MainWindow", u"License", None))
        self.actionSourceCode.setText(QCoreApplication.translate("MainWindow", u"Source code", None))
        self.labelOpenFile.setText(QCoreApplication.translate("MainWindow", u"Select a data file", None))
        self.pushButtonOpenFile.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.groupBoxOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.labelLatitude.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.comboBoxLatitude.setCurrentText("")
        self.labelLongitude.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.labelName.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.labelDesciption.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.labelAltitude.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.labelFiles.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.labelFolders.setText(QCoreApplication.translate("MainWindow", u"Folders", None))
        self.groupBoxStyleOptions.setTitle(QCoreApplication.translate("MainWindow", u"Style Options", None))
        self.labelIconColor.setText(QCoreApplication.translate("MainWindow", u"Icon Color", None))
        self.checkBoxInverseColor.setText(QCoreApplication.translate("MainWindow", u"Inverse", None))
        self.labelIconShape.setText(QCoreApplication.translate("MainWindow", u"Icon Shape", None))
        self.labelSelectedIconShape.setText("")
        self.pushButtonSelectIcon.setText(QCoreApplication.translate("MainWindow", u"Select Icon Shape", None))
        self.pushButtonMakeKML.setText(QCoreApplication.translate("MainWindow", u"Make KML", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

