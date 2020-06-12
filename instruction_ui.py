# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instruction.ui'
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

import data

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1114, 748)
        MainWindow.setMaximumSize(QSize(1852, 1025))
        icon = QIcon()
        icon.addFile(u"../../../Progri/Python/Text finder/ebook.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
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
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:"
                        "0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
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
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* s"
                        "pacing between items in the tool bar */\n"
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
"    margin-right: 5px;\n"
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
""
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
"QTabBar::tab:!selected\n"
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
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, st"
                        "op:0.2 #343434, stop:0.1 #ffaa00);\n"
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
"        fx: 0.5, fy: 0.5,\n"
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
""
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
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
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
"    height: 14"
                        "px;\n"
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
"QGroupBox:hover{\n"
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
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.treeWidget = QTreeWidget(self.centralwidget)
        brush = QBrush(QColor(181, 181, 181, 255))
        brush.setStyle(Qt.NoBrush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem.setBackground(0, brush);
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2.setBackground(0, brush1);
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.treeWidget.setFont(font)
        self.treeWidget.setStyleSheet(u"QTreeView {\n"
"	/**color: rgb(255, 255, 255);**/\n"
"	background-color: #323232;\n"
"	/**border-color: rgb(255, 255, 255);**/\n"
"}\n"
"\n"
"QTreeView::item:hover {\n"
"	background: rgb(238, 147, 38);\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"	background-color:  rgb(238, 147, 38);\n"
"	selection-background-color: rgb(238, 147, 38);\n"
"}")

        self.horizontalLayout.addWidget(self.treeWidget)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setFrameShape(QFrame.Box)
        self.stackedWidget.setFrameShadow(QFrame.Raised)
        self.stackedWidget.setLineWidth(4)
        self.page_loadfile = QWidget()
        self.page_loadfile.setObjectName(u"page_loadfile")
        self.verticalLayout_2 = QVBoxLayout(self.page_loadfile)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_Instruction_loadfile = QLabel(self.page_loadfile)
        self.label_Instruction_loadfile.setObjectName(u"label_Instruction_loadfile")
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei UI Light")
        font1.setPointSize(14)
        self.label_Instruction_loadfile.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_Instruction_loadfile)

        self.line = QFrame(self.page_loadfile)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setLineWidth(4)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line)

        self.label_image_for_instruction_loadfile = QLabel(self.page_loadfile)
        self.label_image_for_instruction_loadfile.setObjectName(u"label_image_for_instruction_loadfile")
        self.label_image_for_instruction_loadfile.setPixmap(QPixmap(
            u"../../Progri/Python/Text finder/instruction/1.png"))
        self.label_image_for_instruction_loadfile.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label_image_for_instruction_loadfile)

        self.verticalLayout_2.setStretch(2, 1)
        self.stackedWidget.addWidget(self.page_loadfile)
        self.page_areaselection = QWidget()
        self.page_areaselection.setObjectName(u"page_areaselection")
        self.verticalLayout = QVBoxLayout(self.page_areaselection)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_Instruction_areaselection = QLabel(self.page_areaselection)
        self.label_Instruction_areaselection.setObjectName(u"label_Instruction_areaselection")
        font2 = QFont()
        font2.setFamily(u"Microsoft YaHei UI Light")
        self.label_Instruction_areaselection.setFont(font2)

        self.verticalLayout.addWidget(self.label_Instruction_areaselection)

        self.label_areaselection2 = QLabel(self.page_areaselection)
        self.label_areaselection2.setObjectName(u"label_areaselection2")
        self.label_areaselection2.setFont(font2)
        self.label_areaselection2.setScaledContents(False)

        self.verticalLayout.addWidget(self.label_areaselection2)

        self.stackedWidget.addWidget(self.page_areaselection)
        self.page_DragandDrop = QWidget()
        self.page_DragandDrop.setObjectName(u"page_DragandDrop")
        self.verticalLayout_3 = QVBoxLayout(self.page_DragandDrop)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_DragandDrop = QLabel(self.page_DragandDrop)
        self.label_DragandDrop.setObjectName(u"label_DragandDrop")
        self.label_DragandDrop.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_DragandDrop)

        self.line_3 = QFrame(self.page_DragandDrop)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.horizontalLayout_DragandDrop = QHBoxLayout()
        self.horizontalLayout_DragandDrop.setObjectName(u"horizontalLayout_DragandDrop")
        self.label_DragandDrop_3 = QLabel(self.page_DragandDrop)
        self.label_DragandDrop_3.setObjectName(u"label_DragandDrop_3")
        self.label_DragandDrop_3.setFont(font1)

        self.horizontalLayout_DragandDrop.addWidget(self.label_DragandDrop_3)

        self.line_2 = QFrame(self.page_DragandDrop)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLineWidth(5)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_DragandDrop.addWidget(self.line_2)

        self.label_DragandDrop_2 = QLabel(self.page_DragandDrop)
        self.label_DragandDrop_2.setObjectName(u"label_DragandDrop_2")
        self.label_DragandDrop_2.setFont(font1)

        self.horizontalLayout_DragandDrop.addWidget(self.label_DragandDrop_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_DragandDrop)

        self.stackedWidget.addWidget(self.page_DragandDrop)
        self.page_Scale = QWidget()
        self.page_Scale.setObjectName(u"page_Scale")
        self.verticalLayout_4 = QVBoxLayout(self.page_Scale)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_Scale = QLabel(self.page_Scale)
        self.label_Scale.setObjectName(u"label_Scale")
        self.label_Scale.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_Scale)

        self.stackedWidget.addWidget(self.page_Scale)
        self.page_position = QWidget()
        self.page_position.setObjectName(u"page_position")
        self.page_position.setFont(font1)
        self.verticalLayout_5 = QVBoxLayout(self.page_position)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_position = QLabel(self.page_position)
        self.label_position.setObjectName(u"label_position")
        self.label_position.setFont(font1)
        self.label_position.setScaledContents(False)
        self.label_position.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_position)

        self.stackedWidget.addWidget(self.page_position)
        self.page_begin = QWidget()
        self.page_begin.setObjectName(u"page_begin")
        self.verticalLayout_6 = QVBoxLayout(self.page_begin)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_about = QLabel(self.page_begin)
        self.label_about.setObjectName(u"label_about")
        self.label_about.setFont(font1)
        self.label_about.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.label_about)

        self.stackedWidget.addWidget(self.page_begin)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Instruction", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u0431 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"1. \u041d\u0430\u0447\u0430\u043b\u043e", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem2.child(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Drag & Drop", None));
        ___qtreewidgetitem5 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"2. \u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem5.child(0)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0440\u0435\u043a\u0446\u0438\u044f", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem5.child(1)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u043e\u0432", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem5.child(2)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem5.child(3)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043a\u0430\u0440\u0442\u0438\u043d\u044b", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem5.child(4)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0435\u0437\u043a\u0430 \u043f\u043e \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u044e", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.label_Instruction_loadfile.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u0443\u0441\u043a\u0430 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b, \u0441\u043b\u0435\u0434\u0443\u0435\u0442 \u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c</p><p>\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443/\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044e. \u0427\u0442\u043e \u0431\u044b \u044d\u0442\u043e \u0441\u0434\u0435\u043b\u0430\u0442\u044c, </p><p>\u043d\u0443\u0436\u043d\u043e \u043d\u0430\u0436\u0430\u0442\u044c \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 <span style=\" font-weight:600;\">&quot;Browse&quot;</span>, \u043f\u043e\u0441\u043b\u0435 \u0447\u0435\u0433\u043e </p><p>\u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b.</p></body></html>", None))
        self.label_image_for_instruction_loadfile.setText("")
        self.label_Instruction_areaselection.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u0432\u0430\u043c \u043f\u043e\u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u043f\u0440\u043e\u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c </span></p><p><span style=\" font-size:14pt;\">\u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u0443\u044e \u043e\u0431\u043b\u0430\u0441\u0442\u044c, \u0430 \u043d\u0435 \u0432\u0441\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435. </span></p><p><span style=\" font-size:14pt;\">\u0414\u043b\u044f \u044d\u0442\u043e\u0433\u043e \u043d\u0443\u0436\u043d\u043e \u043f\u0435\u0440\u0435\u0439\u0442\u0438 \u0432 \u0440\u0430\u0437\u0434\u0435\u043b &quot;</span><span style=\" font-size:14pt; font-weight:600;\">Area selection</span><span style=\" font-size:14pt;\">&quot;</span></p><p><img src=\":/inst_areselection/instruction/2.png\"/></p></body></html>", None))
        self.label_areaselection2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u0417\u0430\u0442\u0435\u043c \u0437\u0430\u0436\u0430\u0442\u044c \u043b\u0435\u0432\u0443\u044e \u043a\u043d\u043e\u043f\u043a\u0443 \u043c\u044b\u0448\u0438 \u043d\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0439 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u0438 \u0432\u044b\u0434\u0435\u043b\u0438\u0442\u044c \u0435\u0435,</span></p><p><span style=\" font-size:14pt;\">\u043f\u043e\u0441\u043b\u0435 \u0447\u0435\u0433\u043e \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0431\u0443\u0434\u0435\u0442 \u043e\u0431\u0440\u0435\u0437\u0430\u043d\u043e. \u041f\u043e\u0442\u043e\u043c \u043d\u0430\u0436\u0430\u0442\u044c \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 &quot;</span><span style=\" font-size:14pt; font-weight:600;\">Save</span><span style=\" font-size:14pt;\">&quot;.</span></p><p><span style=\" font-size:14pt;\">\u0415\u0441\u043b\u0438 \u0432\u044b \u043e\u0448\u0438\u0431\u043b\u0438\u0441\u044c, \u043d\u0430"
                        "\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 &quot;</span><span style=\" font-size:14pt; font-weight:600;\">Reset</span><span style=\" font-size:14pt;\">&quot;.</span><br/><img src=\":/inst_areselection/instruction/3_4_5.png\"/></p></body></html>", None))
        self.label_DragandDrop.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u043e \u0431\u044b\u0441\u0442\u0440\u0430\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439, \u0431\u043b\u043e\u0433\u0430\u0434\u0430\u0440\u044f Drag &amp; Drop.</p><p>\u0414\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e \u043f\u0440\u043e\u0441\u0442\u043e \u0437\u0430\u0436\u0430\u0442\u044c \u0438 \u043f\u0435\u0440\u0435\u0442\u044f\u043d\u0443\u0442\u044c \u0444\u0430\u0439\u043b...<br/></p></body></html>", None))
        self.label_DragandDrop_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><img src=\":/inst_areselection/instruction/71.png\"/></p></body></html>", None))
        self.label_DragandDrop_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><img src=\":/inst_areselection/instruction/81.png\"/></p></body></html>", None))
        self.label_Scale.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0415\u0441\u0442\u044c \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u043a\u0430\u0440\u0442\u0438\u043d\u044b \u0441 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435\u043c \u043f\u0440\u043e\u043f\u043e\u0440\u0446\u044b\u0439.</p><p>\u041d\u0443\u0436\u043d\u043e \u0432\u0432\u0435\u0441\u0442\u0438 \u043d\u0443\u0436\u043d\u044b\u0439 \u0432\u0430\u043c\u0438 \u0448\u0438\u0440\u0438\u043d\u0443 \u0438 \u0432\u044b\u0441\u043e\u0442\u0443.</p><p>Reset - \u0441\u0431\u0440\u0430\u0441\u044b\u0432\u0430\u0435\u0442 \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u043a\u0430\u0440\u0442\u0438\u043d\u044b.</p><p><br/></p><p align=\"center\"><img src=\":/inst_areselection/instruction/9.png\"/></p></body></html>", None))
        self.label_position.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043a\u0430\u0440\u0442\u0438\u043d\u044b, \u043c\u043e\u0436\u043d\u043e \u0431\u043b\u0430\u0433\u043e\u0434\u0430\u0440\u044f \u043a\u043d\u043e\u043f\u043a\u0430\u043c \u0440\u0430\u0437\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u044b\u0445 \u0432\u043d\u0438\u0437\u0443.</p><p><br/></p><p><img src=\":/inst_areselection/instruction/10.png\"/></p></body></html>", None))
        self.label_about.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Text finder</span></p><p align=\"center\">\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f \u043f\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b<br/></p><p><br/></p></body></html>", None))
    # retranslateUi

