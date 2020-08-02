# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text_finder_search.ui'
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

from imagelabel_frommainui import imagelabel_fromMainUi

import data_main

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1270, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(640, 480))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamily(u"Yu Gothic UI Light")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u":/main_icon/Icons/ebook.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    background-color: silver;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
" "
                        "       x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #808080;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 1px solid darkgray;*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushBu"
                        "tton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 20px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{"
                        "\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboB"
                        "ox::down-arrow\n"
"{\n"
"     image: url(:/dark_orange/img/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox\n"
"{   \n"
"	border: 1px solid black;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"	border: 1px solid rgb(33,33,33)\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 1px solid darkgray;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      w"
                        "idth: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"  "
                        "    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QS"
                        "crollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"	color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.318182, x2:0.693, y2:0.563, stop:0.147727 rgba(50, 50, 50, 255), stop:0.732955 rgba(235, 144, 37, 255));\n"
"\n"
"/*    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232); */\n"
"	border-radius: 5;\n"
"}\n"
"\n"
""
                        "QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"	background-color: rgb(235, 144, 37);\n"
"   /*  background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232); */\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/dark_orange/img/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: "
                        "5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
"	 margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!select"
                        "ed\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5,"
                        " fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"	image:url(:/dark_orange/img/checkbox.png);\n"
"	background-color: rgb(255, 170, 0);\n"
"	color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0,"
                        " y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"      stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid darkgray;\n"
"\n"
"    border-radius: 2px;\n"
"    min-width: 50px;\n"
"}\n"
"QMainWindow{\n"
"	border-top: 2px solid black;\n"
"}\n"
"\n"
"QGroupBox{\n"
"	border-color:rgb(33,33,33)\n"
"}\n"
"\n"
"QGroupBox:hover{"
                        "\n"
"	border-color:rgb(33,33,33)\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"}\n"
"\n"
"QGroupBox::indicator:checked\n"
"{\n"
"	background-color: rgb(255, 170, 0);\n"
"	color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"/* QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px;  spacing between items in the tool bar \n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar\n"
"}\n"
"*/\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"	width:0px; \n"
"	height:0px;\n"
"}\n"
"")
        MainWindow.setIconSize(QSize(64, 64))
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.About = QAction(MainWindow)
        self.About.setObjectName(u"About")
        self.About.setShortcutContext(Qt.WindowShortcut)
        self.About.setMenuRole(QAction.TextHeuristicRole)
        self.actionInstructiom = QAction(MainWindow)
        self.actionInstructiom.setObjectName(u"actionInstructiom")
        icon1 = QIcon()
        icon1.addFile(u":/main_icon/Icons/question.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionInstructiom.setIcon(icon1)
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(1000000, 1000000))
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.areaSelection_button = QPushButton(self.centralwidget)
        self.areaSelection_button.setObjectName(u"areaSelection_button")
        self.areaSelection_button.setEnabled(False)
        self.areaSelection_button.setMinimumSize(QSize(52, 50))

        self.horizontalLayout_2.addWidget(self.areaSelection_button)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(52, 50))
        self.pushButton_2.setMaximumSize(QSize(97, 50))
        font1 = QFont()
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	font-size: 15px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/main_icon/Icons/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/main_icon/Icons/upload \u2014 \u043a\u043e\u043f\u0438\u044f.svg", QSize(), QIcon.Disabled, QIcon.Off)
        self.pushButton_2.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.pushButton_2, 0, Qt.AlignVCenter)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(955, 20))
        self.lineEdit.setDragEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFocusPolicy(Qt.ClickFocus)
        self.scrollArea.setFrameShape(QFrame.Box)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1126, 635))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.imagelabel = imagelabel_fromMainUi(self.scrollAreaWidgetContents)
        self.imagelabel.setObjectName(u"imagelabel")
        self.imagelabel.setMouseTracking(True)
        self.imagelabel.setTabletTracking(False)
        self.imagelabel.setContextMenuPolicy(Qt.CustomContextMenu)
        self.imagelabel.setAcceptDrops(True)

        self.verticalLayout_3.addWidget(self.imagelabel)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_rotate_left = QPushButton(self.centralwidget)
        self.pushButton_rotate_left.setObjectName(u"pushButton_rotate_left")
        self.pushButton_rotate_left.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.pushButton_rotate_left)

        self.pushButton_rotate_right = QPushButton(self.centralwidget)
        self.pushButton_rotate_right.setObjectName(u"pushButton_rotate_right")
        self.pushButton_rotate_right.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.pushButton_rotate_right)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1270, 21))
        self.Info = QMenu(self.menuBar)
        self.Info.setObjectName(u"Info")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.dockWidget_editor = QDockWidget(MainWindow)
        self.dockWidget_editor.setObjectName(u"dockWidget_editor")
        self.dockWidget_editor.setMaximumSize(QSize(120, 99999))
        self.dockWidget_editor.setStyleSheet(u"")
        self.dockWidget_editor.setFloating(False)
        self.dockWidget_editor.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidget_editor.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.verticalLayout_8 = QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.dockWidgetContents_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(52, 32))
        self.pushButton.setMaximumSize(QSize(100, 32))
        self.pushButton.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setKerning(False)
        self.pushButton.setFont(font2)
        self.pushButton.setLayoutDirection(Qt.RightToLeft)
        self.pushButton.setCheckable(False)
        self.pushButton.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton)

        self.progressBar = QProgressBar(self.dockWidgetContents_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy2)
        self.progressBar.setMinimumSize(QSize(100, 25))
        self.progressBar.setMaximumSize(QSize(100, 25))
        self.progressBar.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.progressBar.setStyleSheet(u"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;")
        self.progressBar.setMaximum(8)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout.addWidget(self.progressBar)

        self.groupBox_lang = QGroupBox(self.dockWidgetContents_3)
        self.groupBox_lang.setObjectName(u"groupBox_lang")
        self.groupBox_lang.setEnabled(False)
        self.groupBox_lang.setStyleSheet(u"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 2px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 0;\n"
"    padding: 1px;\n"
"    font-size: 15px;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    min-width: 0px;\n"
"}\n"
"QPushButton:disabled {\n"
"	color: #808080;\n"
"	background-color: #323232;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}")
        self.groupBox_lang.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.groupBox_lang.setFlat(False)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_lang)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 20, -1, -1)
        self.comboBox = QComboBox(self.groupBox_lang)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(False)
        self.comboBox.setEditable(False)
        self.comboBox.setMaxCount(20)
        self.comboBox.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setFrame(True)

        self.verticalLayout_9.addWidget(self.comboBox)

        self.horizontalLayout_for2button = QHBoxLayout()
        self.horizontalLayout_for2button.setSpacing(0)
        self.horizontalLayout_for2button.setObjectName(u"horizontalLayout_for2button")
        self.horizontalLayout_for2button.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_for2button.setContentsMargins(0, 0, 0, 0)
        self.pushButton_add = QPushButton(self.groupBox_lang)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy3)
        self.pushButton_add.setMinimumSize(QSize(6, 0))
        self.pushButton_add.setMaximumSize(QSize(16777210, 16777215))
        self.pushButton_add.setSizeIncrement(QSize(0, 0))
        self.pushButton_add.setBaseSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamily(u"MS Serif")
        self.pushButton_add.setFont(font3)
        self.pushButton_add.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_add.setStyleSheet(u"QPushButtoon {\n"
"	min-width: 30px;\n"
"}")
        self.pushButton_add.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_for2button.addWidget(self.pushButton_add)

        self.pushButton_remove = QPushButton(self.groupBox_lang)
        self.pushButton_remove.setObjectName(u"pushButton_remove")
        self.pushButton_remove.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.pushButton_remove.sizePolicy().hasHeightForWidth())
        self.pushButton_remove.setSizePolicy(sizePolicy2)
        self.pushButton_remove.setMinimumSize(QSize(6, 0))
        self.pushButton_remove.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_remove.setFont(font3)

        self.horizontalLayout_for2button.addWidget(self.pushButton_remove)


        self.verticalLayout_9.addLayout(self.horizontalLayout_for2button)

        self.textBrowser_lang = QTextBrowser(self.groupBox_lang)
        self.textBrowser_lang.setObjectName(u"textBrowser_lang")
        self.textBrowser_lang.setFrameShape(QFrame.Box)

        self.verticalLayout_9.addWidget(self.textBrowser_lang)

        self.verticalLayout_9.setStretch(2, 5)

        self.verticalLayout.addWidget(self.groupBox_lang)

        self.checkBox_2 = QCheckBox(self.dockWidgetContents_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setMinimumSize(QSize(100, 13))
        self.checkBox_2.setMaximumSize(QSize(100, 13))
        self.checkBox_2.setTristate(False)

        self.verticalLayout.addWidget(self.checkBox_2)

        self.ContrastGroup = QTabWidget(self.dockWidgetContents_3)
        self.ContrastGroup.setObjectName(u"ContrastGroup")
        self.ContrastGroup.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ContrastGroup.sizePolicy().hasHeightForWidth())
        self.ContrastGroup.setSizePolicy(sizePolicy4)
        self.ContrastGroup.setTabPosition(QTabWidget.North)
        self.ContrastGroup.setElideMode(Qt.ElideNone)
        self.ContrastGroupPage1_2 = QWidget()
        self.ContrastGroupPage1_2.setObjectName(u"ContrastGroupPage1_2")
        self.verticalLayout_6 = QVBoxLayout(self.ContrastGroupPage1_2)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(2, 5, 2, -1)
        self.label_for_contrast = QLabel(self.ContrastGroupPage1_2)
        self.label_for_contrast.setObjectName(u"label_for_contrast")
        self.label_for_contrast.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_for_contrast)

        self.horizontalSlider = QSlider(self.ContrastGroupPage1_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy5)
        self.horizontalSlider.setMinimumSize(QSize(88, 0))
        self.horizontalSlider.setMaximumSize(QSize(125, 22))
        self.horizontalSlider.setMinimum(-100)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setValue(0)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_6.addWidget(self.horizontalSlider)

        self.lable_for_brightness = QLabel(self.ContrastGroupPage1_2)
        self.lable_for_brightness.setObjectName(u"lable_for_brightness")
        self.lable_for_brightness.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lable_for_brightness)

        self.horizontalSlider_brightness = QSlider(self.ContrastGroupPage1_2)
        self.horizontalSlider_brightness.setObjectName(u"horizontalSlider_brightness")
        self.horizontalSlider_brightness.setMinimum(-100)
        self.horizontalSlider_brightness.setMaximum(100)
        self.horizontalSlider_brightness.setValue(0)
        self.horizontalSlider_brightness.setOrientation(Qt.Horizontal)

        self.verticalLayout_6.addWidget(self.horizontalSlider_brightness)

        self.label_for_color_balance = QLabel(self.ContrastGroupPage1_2)
        self.label_for_color_balance.setObjectName(u"label_for_color_balance")
        self.label_for_color_balance.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_for_color_balance)

        self.horizontalSlider_color_blalance = QSlider(self.ContrastGroupPage1_2)
        self.horizontalSlider_color_blalance.setObjectName(u"horizontalSlider_color_blalance")
        self.horizontalSlider_color_blalance.setMinimum(-100)
        self.horizontalSlider_color_blalance.setMaximum(100)
        self.horizontalSlider_color_blalance.setValue(0)
        self.horizontalSlider_color_blalance.setOrientation(Qt.Horizontal)

        self.verticalLayout_6.addWidget(self.horizontalSlider_color_blalance)

        self.label_for_sharpness = QLabel(self.ContrastGroupPage1_2)
        self.label_for_sharpness.setObjectName(u"label_for_sharpness")
        self.label_for_sharpness.setTextFormat(Qt.AutoText)
        self.label_for_sharpness.setScaledContents(False)
        self.label_for_sharpness.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_for_sharpness)

        self.horizontalSlider_for_sharpness = QSlider(self.ContrastGroupPage1_2)
        self.horizontalSlider_for_sharpness.setObjectName(u"horizontalSlider_for_sharpness")
        self.horizontalSlider_for_sharpness.setMinimum(-100)
        self.horizontalSlider_for_sharpness.setMaximum(100)
        self.horizontalSlider_for_sharpness.setOrientation(Qt.Horizontal)

        self.verticalLayout_6.addWidget(self.horizontalSlider_for_sharpness)

        self.pushButton_Reset_enhance = QPushButton(self.ContrastGroupPage1_2)
        self.pushButton_Reset_enhance.setObjectName(u"pushButton_Reset_enhance")
        sizePolicy5.setHeightForWidth(self.pushButton_Reset_enhance.sizePolicy().hasHeightForWidth())
        self.pushButton_Reset_enhance.setSizePolicy(sizePolicy5)
        self.pushButton_Reset_enhance.setMinimumSize(QSize(52, 0))
        self.pushButton_Reset_enhance.setMaximumSize(QSize(9999, 9999))
        font4 = QFont()
        font4.setStyleStrategy(QFont.PreferDefault)
        self.pushButton_Reset_enhance.setFont(font4)
        self.pushButton_Reset_enhance.setFocusPolicy(Qt.StrongFocus)
        icon3 = QIcon()
        icon3.addFile(u":/main_icon/Icons/arr_repeat.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/main_icon/Icons/arr_repeat_blacklivesmatter.svg", QSize(), QIcon.Disabled, QIcon.Off)
        self.pushButton_Reset_enhance.setIcon(icon3)

        self.verticalLayout_6.addWidget(self.pushButton_Reset_enhance)

        self.ContrastGroup.addTab(self.ContrastGroupPage1_2, "")
        self.ContrastGroupPage2 = QWidget()
        self.ContrastGroupPage2.setObjectName(u"ContrastGroupPage2")
        self.verticalLayout_7 = QVBoxLayout(self.ContrastGroupPage2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 5, 2, -1)
        self.label = QLabel(self.ContrastGroupPage2)
        self.label.setObjectName(u"label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy6)
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_7.addWidget(self.label)

        self.horizontalSlider_unsharmask = QSlider(self.ContrastGroupPage2)
        self.horizontalSlider_unsharmask.setObjectName(u"horizontalSlider_unsharmask")
        self.horizontalSlider_unsharmask.setMinimum(-100)
        self.horizontalSlider_unsharmask.setMaximum(100)
        self.horizontalSlider_unsharmask.setValue(-100)
        self.horizontalSlider_unsharmask.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.horizontalSlider_unsharmask)

        self.label_GaussianBlur = QLabel(self.ContrastGroupPage2)
        self.label_GaussianBlur.setObjectName(u"label_GaussianBlur")
        sizePolicy6.setHeightForWidth(self.label_GaussianBlur.sizePolicy().hasHeightForWidth())
        self.label_GaussianBlur.setSizePolicy(sizePolicy6)
        self.label_GaussianBlur.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_7.addWidget(self.label_GaussianBlur)

        self.horizontalSlider_gaussian = QSlider(self.ContrastGroupPage2)
        self.horizontalSlider_gaussian.setObjectName(u"horizontalSlider_gaussian")
        self.horizontalSlider_gaussian.setMinimum(-100)
        self.horizontalSlider_gaussian.setMaximum(100)
        self.horizontalSlider_gaussian.setValue(-100)
        self.horizontalSlider_gaussian.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.horizontalSlider_gaussian)

        self.checkBox_medianfilter = QCheckBox(self.ContrastGroupPage2)
        self.checkBox_medianfilter.setObjectName(u"checkBox_medianfilter")
        sizePolicy1.setHeightForWidth(self.checkBox_medianfilter.sizePolicy().hasHeightForWidth())
        self.checkBox_medianfilter.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        font5.setKerning(True)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.checkBox_medianfilter.setFont(font5)
        self.checkBox_medianfilter.setStyleSheet(u"QCheckBox {\n"
"	padding-left: 5px\n"
"}")
        self.checkBox_medianfilter.setTristate(False)

        self.verticalLayout_7.addWidget(self.checkBox_medianfilter, 0, Qt.AlignTop)

        self.ContrastGroup.addTab(self.ContrastGroupPage2, "")

        self.verticalLayout.addWidget(self.ContrastGroup)

        self.ScaleCheckBox = QGroupBox(self.dockWidgetContents_3)
        self.ScaleCheckBox.setObjectName(u"ScaleCheckBox")
        self.ScaleCheckBox.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.ScaleCheckBox.sizePolicy().hasHeightForWidth())
        self.ScaleCheckBox.setSizePolicy(sizePolicy5)
        self.ScaleCheckBox.setMaximumSize(QSize(100, 16777215))
        self.ScaleCheckBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ScaleCheckBox.setFlat(False)
        self.ScaleCheckBox.setCheckable(False)
        self.ScaleCheckBox.setChecked(False)
        self.verticalLayout_5 = QVBoxLayout(self.ScaleCheckBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 20, -1, -1)
        self.height_label = QLabel(self.ScaleCheckBox)
        self.height_label.setObjectName(u"height_label")
        self.height_label.setScaledContents(False)
        self.height_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.height_label)

        self.width = QLineEdit(self.ScaleCheckBox)
        self.width.setObjectName(u"width")
        self.width.setMaximumSize(QSize(100, 16777215))
        self.width.setStyleSheet(u"")
        self.width.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.width.setEchoMode(QLineEdit.Normal)
        self.width.setClearButtonEnabled(False)

        self.verticalLayout_5.addWidget(self.width)

        self.width_label = QLabel(self.ScaleCheckBox)
        self.width_label.setObjectName(u"width_label")
        self.width_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.width_label)

        self.height = QLineEdit(self.ScaleCheckBox)
        self.height.setObjectName(u"height")
        self.height.setMaximumSize(QSize(100, 16777215))
        self.height.setInputMethodHints(Qt.ImhPreferNumbers)

        self.verticalLayout_5.addWidget(self.height)

        self.radioButton_keepAssRatio = QRadioButton(self.ScaleCheckBox)
        self.radioButton_keepAssRatio.setObjectName(u"radioButton_keepAssRatio")

        self.verticalLayout_5.addWidget(self.radioButton_keepAssRatio)

        self.pushButton_3 = QPushButton(self.ScaleCheckBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	font-size: 11px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/main_icon/Icons/scale_whitelivesmatter.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/main_icon/Icons/scale.svg", QSize(), QIcon.Disabled, QIcon.Off)
        self.pushButton_3.setIcon(icon4)

        self.verticalLayout_5.addWidget(self.pushButton_3)

        self.resetScale = QPushButton(self.ScaleCheckBox)
        self.resetScale.setObjectName(u"resetScale")
        sizePolicy1.setHeightForWidth(self.resetScale.sizePolicy().hasHeightForWidth())
        self.resetScale.setSizePolicy(sizePolicy1)
        self.resetScale.setMaximumSize(QSize(16777215, 16777215))
        self.resetScale.setIcon(icon3)

        self.verticalLayout_5.addWidget(self.resetScale)


        self.verticalLayout.addWidget(self.ScaleCheckBox)


        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.dockWidget_editor.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget_editor)
        QWidget.setTabOrder(self.pushButton_2, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.checkBox_2)

        self.menuBar.addAction(self.Info.menuAction())
        self.Info.addAction(self.About)
        self.Info.addAction(self.actionInstructiom)
        self.Info.addSeparator()
        self.Info.addAction(self.actionAbout_Qt)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)
        self.comboBox.setCurrentIndex(-1)
        self.ContrastGroup.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Text Finder", None))
        self.About.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435...", None))
        self.actionInstructiom.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e Qt", None))
#if QT_CONFIG(statustip)
        self.areaSelection_button.setStatusTip(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0435\u0437\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u0435", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.areaSelection_button.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0435\u0437\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u0435", None))
#endif // QT_CONFIG(whatsthis)
        self.areaSelection_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0435\u0437\u0430\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_2.setStatusTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.imagelabel.setText("")
#if QT_CONFIG(statustip)
        self.pushButton_5.setStatusTip(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0432\u0435\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443 \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButton_5.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0432\u0435\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u2191\u2193", None))
#if QT_CONFIG(statustip)
        self.pushButton_rotate_left.setStatusTip(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443 \u043d\u0430 -90 \u00b0", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButton_rotate_left.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443 \u043d\u0430 -90 \u00b0", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_rotate_left.setText(QCoreApplication.translate("MainWindow", u"\u21ba 90\u00b0", None))
#if QT_CONFIG(statustip)
        self.pushButton_rotate_right.setStatusTip(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443 \u043d\u0430 +90 \u00b0", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButton_rotate_right.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443 \u043d\u0430 +90 \u00b0", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_rotate_right.setText(QCoreApplication.translate("MainWindow", u"\u21bb 90\u00b0", None))
#if QT_CONFIG(statustip)
        self.pushButton_4.setStatusTip(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0432\u0435\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443 \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u043e", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButton_4.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0432\u0435\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443 \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u043e", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u21c6", None))
        self.Info.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e", None))
        self.dockWidget_editor.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440", None))
#if QT_CONFIG(statustip)checkBox_medianfilter
        self.pushButton.setStatusTip(QCoreApplication.translate("MainWindow", u" \u0420\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0442\u044c \u0442\u0435\u043a\u0441\u0442 \u043d\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0435", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButton.setWhatsThis(QCoreApplication.translate("MainWindow", u"\n"
"\u0420\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0442\u044c \u0442\u0435\u043a\u0441\u0442 \u043d\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0435", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0422\u0410\u0420\u0422", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.groupBox_lang.setTitle(QCoreApplication.translate("MainWindow", u"\u042f\u0437\u044b\u043a\u0438", None))
        self.comboBox.setCurrentText("")
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_remove.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.textBrowser_lang.setMarkdown("")
        self.textBrowser_lang.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u042f\u0437\u044b\u043a\u0438...", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0440\u043d\u043e-\u0431\u0435\u043b\u044b\u0439", None))
        self.label_for_contrast.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u0430\u0441\u0442", None))
        self.lable_for_brightness.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0440\u043a\u043e\u0441\u0442\u044c", None))
        self.label_for_color_balance.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442\u043e\u0432\u043e\u0439 \u0431\u0430\u043b\u0430\u043d\u0441", None))
        self.label_for_sharpness.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0442\u043a\u043e\u0441\u0442\u044c", None))
#if QT_CONFIG(statustip)
        self.pushButton_Reset_enhance.setStatusTip(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441 \u0443\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u0435 \u043d\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0435", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButton_Reset_enhance.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441 \u0443\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u0435 \u043d\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0435", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_Reset_enhance.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441", None))
        self.ContrastGroup.setTabText(self.ContrastGroup.indexOf(self.ContrastGroupPage1_2), QCoreApplication.translate("MainWindow", u"1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0443\u0440\u043d\u0430\u044f\n"
"\u0440\u0435\u0437\u043a\u043e\u0441\u0442\u044c", None))
        self.label_GaussianBlur.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u044b\u0442\u0438\u0435\n"
"\u043f\u043e \u0413\u0430\u0443\u0441\u0441\u0443", None))
        self.checkBox_medianfilter.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0434\u0438\u0430\u043d\u043d\u044b\u0439\n\u0444\u0438\u043b\u044c\u0442\u0440", None))
        self.ContrastGroup.setTabText(self.ContrastGroup.indexOf(self.ContrastGroupPage2), QCoreApplication.translate("MainWindow", u"2", None))
        self.ScaleCheckBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0448\u0442\u0430\u0431", None))
        self.height_label.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430", None))
        self.width_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430", None))
        self.radioButton_keepAssRatio.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c\n"
"\u043f\u0440\u043e\u043f\u043e\u0440\u0446\u0438\u0438", None))
#if QT_CONFIG(statustip)
        self.pushButton_3.setStatusTip(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButton_3.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
#if QT_CONFIG(statustip)
        self.resetScale.setStatusTip(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u043c\u0430\u0441\u0448\u0442\u0430\u0431", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.resetScale.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u043c\u0430\u0441\u0448\u0442\u0430\u0431", None))
#endif // QT_CONFIG(whatsthis)
        self.resetScale.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441", None))
    # retranslateUi

