import sys

from PySide2.QtCore import QObject, Signal
from PySide2.QtWidgets import QLabel, QWidget


class imagelabel_fromMainUi(QLabel):
    dropEvent_Signal = Signal(str)

    def __init__(self, parent=None):
        super(imagelabel_fromMainUi, self).__init__(parent=parent)
        self.file_dir = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            self.file_dir = url.toLocalFile()
            print("Dropped file: " + self.file_dir)

            self.dropEvent_Signal.emit(str(self.file_dir))
            print("Send file_dir to main window")
