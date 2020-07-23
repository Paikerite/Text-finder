# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiforDrawing.ui'
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

from labelimage import labelimage

import data_main

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"Icons/find.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QMainWindow{\n"
"	\n"
"	background-color: rgb(80, 80, 80);\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.positin_label = QLabel(self.centralwidget)
        self.positin_label.setObjectName(u"positin_label")
        font = QFont()
        font.setPointSize(16)
        self.positin_label.setFont(font)
        self.positin_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.positin_label)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"	background-color: rgb(90, 90, 90);\n"
"}")
        self.scrollArea.setFrameShape(QFrame.WinPanel)
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 778, 495))
        self.scrollAreaWidgetContents.setAutoFillBackground(False)
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget {\n"
"	\n"
"	background-color: rgb(95, 95, 95);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelimage = labelimage(self.scrollAreaWidgetContents)
        self.labelimage.setObjectName(u"labelimage")
        self.labelimage.setCursor(QCursor(Qt.CrossCursor))
        self.labelimage.setMouseTracking(True)
        self.labelimage.setFocusPolicy(Qt.NoFocus)
        self.labelimage.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.labelimage.setAutoFillBackground(False)
        self.labelimage.setScaledContents(False)
        self.labelimage.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.labelimage.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.labelimage)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SaveChangedPic = QPushButton(self.centralwidget)
        self.SaveChangedPic.setObjectName(u"SaveChangedPic")
        icon1 = QIcon()
        icon1.addFile(u":/main_icon/Icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.SaveChangedPic.setIcon(icon1)

        self.horizontalLayout.addWidget(self.SaveChangedPic)

        self.resetPicture = QPushButton(self.centralwidget)
        self.resetPicture.setObjectName(u"resetPicture")
        self.resetPicture.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/main_icon/Icons/arr_repeat.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.resetPicture.setIcon(icon2)

        self.horizontalLayout.addWidget(self.resetPicture)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Size off", None))
        self.positin_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0435\u043b\u0438\u0442\u0435 \u043e\u0431\u043b\u0430\u0441\u0442\u044c", None))
        self.labelimage.setText("")
        self.SaveChangedPic.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.resetPicture.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441", None))
    # retranslateUi

