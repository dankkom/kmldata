# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectIconWindow.ui'
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

class Ui_SelectIconWindow(object):
    def setupUi(self, SelectIconWindow):
        if not SelectIconWindow.objectName():
            SelectIconWindow.setObjectName(u"SelectIconWindow")
        SelectIconWindow.resize(300, 600)
        SelectIconWindow.setMinimumSize(QSize(300, 300))
        font = QFont()
        SelectIconWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/images/xltokml-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        SelectIconWindow.setWindowIcon(icon)
        SelectIconWindow.setStyleSheet(u"font-size: 20px;")
        self.verticalLayout = QVBoxLayout(SelectIconWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidgetSelectIcon = QListWidget(SelectIconWindow)
        self.listWidgetSelectIcon.setObjectName(u"listWidgetSelectIcon")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetSelectIcon.sizePolicy().hasHeightForWidth())
        self.listWidgetSelectIcon.setSizePolicy(sizePolicy)
        self.listWidgetSelectIcon.setStyleSheet(u"font-size: 20px;")
        self.listWidgetSelectIcon.setFrameShape(QFrame.NoFrame)
        self.listWidgetSelectIcon.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.listWidgetSelectIcon)

        self.frameButtons = QFrame(SelectIconWindow)
        self.frameButtons.setObjectName(u"frameButtons")
        self.frameButtons.setMaximumSize(QSize(16777215, 80))
        self.frameButtons.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(235, 235, 235);\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px  solid rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frameButtons.setFrameShape(QFrame.NoFrame)
        self.frameButtons.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frameButtons)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.pushButtonCancel = QPushButton(self.frameButtons)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        self.pushButtonCancel.setMinimumSize(QSize(0, 50))
        self.pushButtonCancel.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(0, 0, 0);\n"
"	background-color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButtonCancel)

        self.pushButtonOk = QPushButton(self.frameButtons)
        self.pushButtonOk.setObjectName(u"pushButtonOk")
        self.pushButtonOk.setMinimumSize(QSize(0, 50))
        self.pushButtonOk.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(200, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 100,100);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButtonOk)


        self.verticalLayout.addWidget(self.frameButtons)


        self.retranslateUi(SelectIconWindow)

        QMetaObject.connectSlotsByName(SelectIconWindow)
    # setupUi

    def retranslateUi(self, SelectIconWindow):
        SelectIconWindow.setWindowTitle(QCoreApplication.translate("SelectIconWindow", u"Select Icon", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("SelectIconWindow", u"Cancel", None))
        self.pushButtonOk.setText(QCoreApplication.translate("SelectIconWindow", u"OK", None))
    # retranslateUi

