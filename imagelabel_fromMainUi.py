import sys

from PySide2.QtCore import QObject, Signal, Qt
from PySide2.QtGui import QGuiApplication, QPixmap, QImage
from PySide2.QtWidgets import QLabel, QWidget, QMenu, QAction


class imagelabel_fromMainUi(QLabel):
    dropEvent_Signal = Signal(str)
    pastEvent_signal = Signal(list)
    resetEvent_signal = Signal()

    def __init__(self, parent=None):
        super(imagelabel_fromMainUi, self).__init__(parent=parent)
        self.file_dir = None

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

        self.popMenu = QMenu(self)
        self.popMenu.addAction(QAction('Paste', self, triggered=self.context_trigger_paste))
        self.popMenu.addAction(QAction('Copy', self, triggered=self.context_trigger_copy))
        self.popMenu.addSeparator()
        self.popMenu.addAction(QAction('Reset', self, triggered=self.context_trigger_reset))

        # self.popMenu.triggered[QAction].connect(self.context_trigger)

    def context_trigger_reset(self):
        print("reset")
        self.clear()
        self.resetEvent_signal.emit()

    def context_trigger_copy(self):
        print("copy")
        clipboard = QGuiApplication.clipboard()
        image = self.pixmap()
        clipboard.setImage(QPixmap.toImage(image))

    def context_trigger_paste(self):
        clipboard = QGuiApplication.clipboard()
        mimeData = clipboard.mimeData()

        if mimeData.hasImage():
            print("Image has been detected on paste")
            self.pastEvent_signal.emit([mimeData.imageData()])

            # self.setPixmap(QPixmap.fromImage(mimeData.imageData()))
        elif mimeData.hasHtml():
            print("HTML has been detected on paste")
            # setText(mimeData.html())
            # setTextFormat(Qt.RichText)
        elif mimeData.hasText():
            print("Text has been detected on paste")
            # setText(mimeData.text())
            # setTextFormat(Qt.PlainText)
        else:
            print("Cannot display data")

    def on_context_menu(self, point):
        # show context menu
        self.popMenu.exec_(self.mapToGlobal(point))

    def dragEnterEvent(self, event):
        self.setStyleSheet(u'''QLabel {
        background-color: rgb(170, 170, 170);
        }''')

        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            self.file_dir = url.toLocalFile()
            print("Dropped file: " + self.file_dir)

            self.dropEvent_Signal.emit(str(self.file_dir))
            print("Send file_dir to main window")

    def dragLeaveEvent(self, event):
        self.setStyleSheet(u'')
