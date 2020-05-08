# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiforDrawing.ui',
# licensing of 'uiforDrawing.ui' applies.
#
# Created: Fri May  8 15:17:02 2020
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/find.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QToolTip\n"
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
"    \n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.positin_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.positin_label.setFont(font)
        self.positin_label.setAlignment(QtCore.Qt.AlignCenter)
        self.positin_label.setObjectName("positin_label")
        self.verticalLayout.addWidget(self.positin_label)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("QScrollArea{\n"
"    background-color: rgb(90, 90, 90);\n"
"}")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 778, 495))
        self.scrollAreaWidgetContents.setAutoFillBackground(False)
        self.scrollAreaWidgetContents.setStyleSheet("QWidget {\n"
"    \n"
"    background-color: rgb(95, 95, 95);\n"
"}")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelimage = labelimage(self.scrollAreaWidgetContents)
        self.labelimage.setCursor(QtCore.Qt.CrossCursor)
        self.labelimage.setMouseTracking(True)
        self.labelimage.setFocusPolicy(QtCore.Qt.NoFocus)
        self.labelimage.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.labelimage.setAutoFillBackground(False)
        self.labelimage.setText("")
        self.labelimage.setScaledContents(False)
        self.labelimage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelimage.setWordWrap(False)
        self.labelimage.setObjectName("labelimage")
        self.verticalLayout_2.addWidget(self.labelimage)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SaveChangedPic = QtWidgets.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveChangedPic.setIcon(icon1)
        self.SaveChangedPic.setObjectName("SaveChangedPic")
        self.horizontalLayout.addWidget(self.SaveChangedPic)
        self.resetPicture = QtWidgets.QPushButton(self.centralwidget)
        self.resetPicture.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/arr_repeat.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetPicture.setIcon(icon2)
        self.resetPicture.setObjectName("resetPicture")
        self.horizontalLayout.addWidget(self.resetPicture)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Size off", None, -1))
        self.positin_label.setText(QtWidgets.QApplication.translate("MainWindow", "Select certain field", None, -1))
        self.SaveChangedPic.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.resetPicture.setText(QtWidgets.QApplication.translate("MainWindow", "Reset", None, -1))

from labelimage import labelimage
