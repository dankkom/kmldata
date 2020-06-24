# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutWindow.ui'
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

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        if not AboutWindow.objectName():
            AboutWindow.setObjectName(u"AboutWindow")
        AboutWindow.resize(650, 430)
        AboutWindow.setMinimumSize(QSize(650, 430))
        AboutWindow.setMaximumSize(QSize(650, 430))
        font = QFont()
        font.setPointSize(12)
        AboutWindow.setFont(font)
        AboutWindow.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        icon.addFile(u":/images/images/xltokml-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        AboutWindow.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(AboutWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(AboutWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(1)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-image: url(:/images/images/xltokml-logo.png);\n"
"background-position: center;\n"
"background-repeat: false;")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(0)

        self.horizontalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setLineWidth(0)
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.textBrowser = QTextBrowser(self.frame_3)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setFont(font)
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QFrame.Plain)
        self.textBrowser.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.textBrowser)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        self.PythonQtLogo = QFrame(AboutWindow)
        self.PythonQtLogo.setObjectName(u"PythonQtLogo")
        self.PythonQtLogo.setMaximumSize(QSize(16777215, 90))
        self.PythonQtLogo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.PythonQtLogo.setFrameShape(QFrame.NoFrame)
        self.PythonQtLogo.setFrameShadow(QFrame.Plain)
        self.PythonQtLogo.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.PythonQtLogo)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(155, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.labelPythonPowered = QLabel(self.PythonQtLogo)
        self.labelPythonPowered.setObjectName(u"labelPythonPowered")
        self.labelPythonPowered.setMinimumSize(QSize(300, 60))
        self.labelPythonPowered.setMaximumSize(QSize(300, 60))
        self.labelPythonPowered.setAutoFillBackground(False)
        self.labelPythonPowered.setLineWidth(0)
        self.labelPythonPowered.setPixmap(QPixmap(u":/images/images/credits.png"))
        self.labelPythonPowered.setScaledContents(True)
        self.labelPythonPowered.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.labelPythonPowered)


        self.verticalLayout.addWidget(self.PythonQtLogo)


        self.retranslateUi(AboutWindow)

        QMetaObject.connectSlotsByName(AboutWindow)
    # setupUi

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(QCoreApplication.translate("AboutWindow", u"About", None))
        self.label_2.setText(QCoreApplication.translate("AboutWindow", u"xlToKML", None))
        self.textBrowser.setMarkdown(QCoreApplication.translate("AboutWindow", u"xlToKML is part of kmldata Python package.\n"
"\n"
"Author:\n"
"  dkkomesu\n"
"\n"
"License:\n"
"  LGPLv3\n"
"\n"
"Source code:\n"
"  \n"
"[github.com/dkkomesu/kmldata](https://github.com/dkkomesu/kmldata)\n"
"\n"
"", None))
        self.textBrowser.setHtml(QCoreApplication.translate("AboutWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">xlToKML is part of kmldata Python package.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Author:<br />  dkkomesu</p>\n"
"<p style=\"-qt-paragraph-type:empt"
                        "y; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License:<br />  LGPLv3</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Source code:<br />  <a href=\"https://github.com/dkkomesu/kmldata\"><span style=\" text-decoration: underline; color:#0000ff;\">github.com/dkkomesu/kmldata</span></a></p></body></html>", None))
        self.labelPythonPowered.setText("")
    # retranslateUi

