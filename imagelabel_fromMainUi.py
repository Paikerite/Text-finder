import sys

from PySide2.QtCore import QObject
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import QLabel

from Textfinder import MyWindow


class imagelabel_fromMainUi(QLabel, QObject):
    def __init__(self, parent):
        super(imagelabel_fromMainUi, self).__init__(parent=parent)
        self.image = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_name = url.toLocalFile()
            print("Dropped file: " + file_name)

            self.image = QImage(file_name)
            self.setPixmap(QPixmap.fromImage(file_name))
