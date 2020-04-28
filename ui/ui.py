# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text_finder_search.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1080, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/ebook.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QToolTip\n"
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
"        x2:0, y2:1,\n"
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
"QPushButton\n"
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
"{\n"
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
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/dark_orange/img/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox\n"
"{   \n"
"    border: 1px solid black;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"    border: 1px solid rgb(33,33,33)\n"
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
"      width: 14px;\n"
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
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
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
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
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
"    color: #414141;\n"
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
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
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
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
"     margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
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
"    image:url(:/dark_orange/img/checkbox.png);\n"
"    background-color: rgb(255, 170, 0);\n"
"    color: rgb(255, 170, 0);\n"
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
"    border-top: 2px solid black;\n"
"}\n"
"\n"
"QGroupBox{\n"
"    border-color:rgb(33,33,33)\n"
"}\n"
"\n"
"QGroupBox:hover{\n"
"    border-color:rgb(33,33,33)\n"
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
"    background-color: rgb(255, 170, 0);\n"
"    color: rgb(255, 170, 0);\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(64, 64))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(1000000, 1000000))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.areaSelection_button = QtWidgets.QPushButton(self.centralwidget)
        self.areaSelection_button.setMinimumSize(QtCore.QSize(52, 50))
        self.areaSelection_button.setObjectName("areaSelection_button")
        self.areaSelection_button.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.areaSelection_button)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(52, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(97, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_2.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/find.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignVCenter)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(955, 20))
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 948, 595))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.imagelabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imagelabel.setMouseTracking(True)
        self.imagelabel.setTabletTracking(False)
        self.imagelabel.setAcceptDrops(True)
        self.imagelabel.setText("")
        self.imagelabel.setObjectName("imagelabel")
        self.verticalLayout_3.addWidget(self.imagelabel)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(52, 32))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 32))
        self.pushButton.setCheckable(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setEnabled(False)
        self.verticalLayout.addWidget(self.pushButton)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(100, 25))
        self.progressBar.setMaximumSize(QtCore.QSize(100, 25))
        self.progressBar.setStyleSheet("    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMaximum(8)
        self.progressBar.setEnabled(False)
        self.verticalLayout.addWidget(self.progressBar, 0, QtCore.Qt.AlignRight)
        self.label_for_language = QtWidgets.QLabel(self.centralwidget)
        self.label_for_language.setAlignment(QtCore.Qt.AlignCenter)
        self.label_for_language.setObjectName("label_for_language")
        self.verticalLayout.addWidget(self.label_for_language)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setMaxCount(20)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setEnabled(False)
        self.verticalLayout.addWidget(self.comboBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setMinimumSize(QtCore.QSize(100, 13))
        self.checkBox_2.setMaximumSize(QtCore.QSize(100, 13))
        self.checkBox_2.setTristate(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setEnabled(False)
        self.verticalLayout.addWidget(self.checkBox_2, 0, QtCore.Qt.AlignRight)
        self.ContrastGroup = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ContrastGroup.sizePolicy().hasHeightForWidth())
        self.ContrastGroup.setSizePolicy(sizePolicy)
        self.ContrastGroup.setTabPosition(QtWidgets.QTabWidget.North)
        self.ContrastGroup.setElideMode(QtCore.Qt.ElideNone)
        self.ContrastGroup.setObjectName("ContrastGroup")
        self.ContrastGroup.setEnabled(False)
        self.ContrastGroupPage1_2 = QtWidgets.QWidget()
        self.ContrastGroupPage1_2.setObjectName("ContrastGroupPage1_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.ContrastGroupPage1_2)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(2, 5, 2, -1)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_for_contrast = QtWidgets.QLabel(self.ContrastGroupPage1_2)
        self.label_for_contrast.setAlignment(QtCore.Qt.AlignCenter)
        self.label_for_contrast.setObjectName("label_for_contrast")
        self.verticalLayout_6.addWidget(self.label_for_contrast)
        self.horizontalSlider = QtWidgets.QSlider(self.ContrastGroupPage1_2)
        self.horizontalSlider.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(88, 0))
        self.horizontalSlider.setMaximumSize(QtCore.QSize(125, 22))
        self.horizontalSlider.setMinimum(-100)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_6.addWidget(self.horizontalSlider)
        self.lable_for_brightness = QtWidgets.QLabel(self.ContrastGroupPage1_2)
        self.lable_for_brightness.setAlignment(QtCore.Qt.AlignCenter)
        self.lable_for_brightness.setObjectName("lable_for_brightness")
        self.verticalLayout_6.addWidget(self.lable_for_brightness)
        self.horizontalSlider_brightness = QtWidgets.QSlider(self.ContrastGroupPage1_2)
        self.horizontalSlider_brightness.setMinimum(-100)
        self.horizontalSlider_brightness.setMaximum(100)
        self.horizontalSlider_brightness.setProperty("value", 0)
        self.horizontalSlider_brightness.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_brightness.setObjectName("horizontalSlider_brightness")
        self.verticalLayout_6.addWidget(self.horizontalSlider_brightness)
        self.label_for_color_balance = QtWidgets.QLabel(self.ContrastGroupPage1_2)
        self.label_for_color_balance.setAlignment(QtCore.Qt.AlignCenter)
        self.label_for_color_balance.setObjectName("label_for_color_balance")
        self.verticalLayout_6.addWidget(self.label_for_color_balance)
        self.horizontalSlider_color_blalance = QtWidgets.QSlider(self.ContrastGroupPage1_2)
        self.horizontalSlider_color_blalance.setMinimum(-100)
        self.horizontalSlider_color_blalance.setMaximum(100)
        self.horizontalSlider_color_blalance.setProperty("value", 0)
        self.horizontalSlider_color_blalance.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_color_blalance.setObjectName("horizontalSlider_color_blalance")
        self.verticalLayout_6.addWidget(self.horizontalSlider_color_blalance)
        self.label_for_sharpness = QtWidgets.QLabel(self.ContrastGroupPage1_2)
        self.label_for_sharpness.setTextFormat(QtCore.Qt.AutoText)
        self.label_for_sharpness.setScaledContents(False)
        self.label_for_sharpness.setAlignment(QtCore.Qt.AlignCenter)
        self.label_for_sharpness.setObjectName("label_for_sharpness")
        self.verticalLayout_6.addWidget(self.label_for_sharpness)
        self.horizontalSlider_for_sharpness = QtWidgets.QSlider(self.ContrastGroupPage1_2)
        self.horizontalSlider_for_sharpness.setMinimum(-100)
        self.horizontalSlider_for_sharpness.setMaximum(100)
        self.horizontalSlider_for_sharpness.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_for_sharpness.setObjectName("horizontalSlider_for_sharpness")
        self.verticalLayout_6.addWidget(self.horizontalSlider_for_sharpness)
        self.pushButton_Reset_enhance = QtWidgets.QPushButton(self.ContrastGroupPage1_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Reset_enhance.sizePolicy().hasHeightForWidth())
        self.pushButton_Reset_enhance.setSizePolicy(sizePolicy)
        self.pushButton_Reset_enhance.setMinimumSize(QtCore.QSize(52, 0))
        self.pushButton_Reset_enhance.setMaximumSize(QtCore.QSize(86, 32))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_Reset_enhance.setFont(font)
        self.pushButton_Reset_enhance.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_Reset_enhance.setObjectName("pushButton_Reset_enhance")
        self.verticalLayout_6.addWidget(self.pushButton_Reset_enhance, 0, QtCore.Qt.AlignHCenter)
        self.ContrastGroup.addTab(self.ContrastGroupPage1_2, "")
        self.ContrastGroupPage2 = QtWidgets.QWidget()
        self.ContrastGroupPage2.setObjectName("ContrastGroupPage2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.ContrastGroupPage2)
        self.verticalLayout_7.setContentsMargins(2, 5, 2, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(self.ContrastGroupPage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.horizontalSlider_unsharmask = QtWidgets.QSlider(self.ContrastGroupPage2)
        self.horizontalSlider_unsharmask.setMinimum(-100)
        self.horizontalSlider_unsharmask.setMaximum(100)
        self.horizontalSlider_unsharmask.setValue(-100)
        self.horizontalSlider_unsharmask.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_unsharmask.setObjectName("horizontalSlider_unsharmask")
        self.verticalLayout_7.addWidget(self.horizontalSlider_unsharmask)
        self.label_GaussianBlur = QtWidgets.QLabel(self.ContrastGroupPage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_GaussianBlur.sizePolicy().hasHeightForWidth())
        self.label_GaussianBlur.setSizePolicy(sizePolicy)
        self.label_GaussianBlur.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_GaussianBlur.setObjectName("label_GaussianBlur")
        self.verticalLayout_7.addWidget(self.label_GaussianBlur)
        self.horizontalSlider_gaussian = QtWidgets.QSlider(self.ContrastGroupPage2)
        self.horizontalSlider_gaussian.setMinimum(-100)
        self.horizontalSlider_gaussian.setMaximum(100)
        self.horizontalSlider_gaussian.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_gaussian.setValue(-100)
        self.horizontalSlider_gaussian.setObjectName("horizontalSlider_gaussian")
        self.verticalLayout_7.addWidget(self.horizontalSlider_gaussian)
        self.checkBox_medianfilter = QtWidgets.QCheckBox(self.ContrastGroupPage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_medianfilter.sizePolicy().hasHeightForWidth())
        self.checkBox_medianfilter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.checkBox_medianfilter.setFont(font)
        self.checkBox_medianfilter.setStyleSheet("QCheckBox {\n"
"    padding-left: 5px\n"
"}")
        self.checkBox_medianfilter.setTristate(False)
        self.checkBox_medianfilter.setObjectName("checkBox_medianfilter")
        self.verticalLayout_7.addWidget(self.checkBox_medianfilter, 0, QtCore.Qt.AlignTop)
        self.ContrastGroup.addTab(self.ContrastGroupPage2, "")
        self.verticalLayout.addWidget(self.ContrastGroup)
        self.ScaleCheckBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScaleCheckBox.sizePolicy().hasHeightForWidth())
        self.ScaleCheckBox.setSizePolicy(sizePolicy)
        self.ScaleCheckBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ScaleCheckBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ScaleCheckBox.setFlat(False)
        self.ScaleCheckBox.setCheckable(False)
        self.ScaleCheckBox.setChecked(False)
        self.ScaleCheckBox.setObjectName("ScaleCheckBox")
        self.ScaleCheckBox.setEnabled(False)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.ScaleCheckBox)
        self.verticalLayout_5.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.height_label = QtWidgets.QLabel(self.ScaleCheckBox)
        self.height_label.setScaledContents(False)
        self.height_label.setAlignment(QtCore.Qt.AlignCenter)
        self.height_label.setObjectName("height_label")
        self.verticalLayout_5.addWidget(self.height_label)
        self.width = QtWidgets.QLineEdit(self.ScaleCheckBox)
        self.width.setMaximumSize(QtCore.QSize(100, 16777215))
        self.width.setStyleSheet("")
        self.width.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.width.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.width.setClearButtonEnabled(False)
        self.width.setObjectName("width")
        self.verticalLayout_5.addWidget(self.width)
        self.width_label = QtWidgets.QLabel(self.ScaleCheckBox)
        self.width_label.setAlignment(QtCore.Qt.AlignCenter)
        self.width_label.setObjectName("width_label")
        self.verticalLayout_5.addWidget(self.width_label)
        self.height = QtWidgets.QLineEdit(self.ScaleCheckBox)
        self.height.setMaximumSize(QtCore.QSize(100, 16777215))
        self.height.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.height.setObjectName("height")
        self.verticalLayout_5.addWidget(self.height)
        self.pushButton_3 = QtWidgets.QPushButton(self.ScaleCheckBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.pushButton_3)
        self.resetScale = QtWidgets.QPushButton(self.ScaleCheckBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetScale.sizePolicy().hasHeightForWidth())
        self.resetScale.setSizePolicy(sizePolicy)
        self.resetScale.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.resetScale.setObjectName("resetScale")
        self.verticalLayout_5.addWidget(self.resetScale)
        self.verticalLayout.addWidget(self.ScaleCheckBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1080, 21))
        self.menuBar.setObjectName("menuBar")
        self.Info = QtWidgets.QMenu(self.menuBar)
        self.Info.setObjectName("Info")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.About = QtWidgets.QAction(MainWindow)
        self.About.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.About.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.About.setObjectName("About")
        self.actionInstructiom = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/question.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInstructiom.setIcon(icon2)
        self.actionInstructiom.setObjectName("actionInstructiom")
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.Info.addAction(self.About)
        self.Info.addAction(self.actionInstructiom)
        self.Info.addSeparator()
        self.Info.addAction(self.actionAbout_Qt)
        self.menuBar.addAction(self.Info.menuAction())

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(-1)
        self.ContrastGroup.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_2, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.checkBox_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text Finder"))
        self.areaSelection_button.setStatusTip(_translate("MainWindow", " Allocate area for recognition"))
        self.areaSelection_button.setWhatsThis(_translate("MainWindow", " Allocate area for recognition"))
        self.areaSelection_button.setText(_translate("MainWindow", "Area selection"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "Open the picture"))
        self.pushButton_2.setStatusTip(_translate("MainWindow", "Open the picture"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.pushButton.setStatusTip(_translate("MainWindow", "Recognize text on the picture"))
        self.pushButton.setWhatsThis(_translate("MainWindow", "Recognize text on the picture"))
        self.pushButton.setText(_translate("MainWindow", "Begin"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.label_for_language.setText(_translate("MainWindow", "Languages"))
        self.checkBox_2.setText(_translate("MainWindow", "Gray"))
        self.label_for_contrast.setText(_translate("MainWindow", "Contrast"))
        self.lable_for_brightness.setText(_translate("MainWindow", "Brightness"))
        self.label_for_color_balance.setText(_translate("MainWindow", "Color balance"))
        self.label_for_sharpness.setText(_translate("MainWindow", "Sharpness"))
        self.pushButton_Reset_enhance.setText(_translate("MainWindow", "Reset"))
        self.ContrastGroup.setTabText(self.ContrastGroup.indexOf(self.ContrastGroupPage1_2), _translate("MainWindow", "1"))
        self.label.setText(_translate("MainWindow", "Unsharp Mask"))
        self.label_GaussianBlur.setText(_translate("MainWindow", "Gaussian Blur"))
        self.checkBox_medianfilter.setText(_translate("MainWindow", "Median Filter"))
        self.ContrastGroup.setTabText(self.ContrastGroup.indexOf(self.ContrastGroupPage2), _translate("MainWindow", "2"))
        self.ScaleCheckBox.setTitle(_translate("MainWindow", "Scale"))
        self.height_label.setText(_translate("MainWindow", "Width"))
        self.width_label.setText(_translate("MainWindow", "Height"))
        self.pushButton_3.setStatusTip(_translate("MainWindow", "Change the resolution"))
        self.pushButton_3.setWhatsThis(_translate("MainWindow", "Change the resolution"))
        self.pushButton_3.setText(_translate("MainWindow", "Scale"))
        self.resetScale.setText(_translate("MainWindow", "Reset"))
        self.Info.setTitle(_translate("MainWindow", "Info"))
        self.About.setText(_translate("MainWindow", "About..."))
        self.actionInstructiom.setText(_translate("MainWindow", "Instruction"))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt"))
