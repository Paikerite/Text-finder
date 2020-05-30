import sys

from PySide2.QtCore import QObject, Signal
from PySide2.QtWidgets import QLabel

from Textfinder import MyWindow


class imagelabel_fromMainUi(QLabel, MyWindow):  # QLabel, QObject
    # dropEvent_Signal = Signal(str)
    def __init__(self, parent):
        super(imagelabel_fromMainUi, self).__init__(parent=parent)  # imagelabel_fromMainUi
        self.mainUi = MyWindow
        self.file_dir = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            self.file_dir = url.toLocalFile()
            print("Dropped file: " + self.file_dir)

            # self.dropEvent_Signal.emit(str(self.file_dir))
            print("Send file_dir to main window")
            # super(imagelabel_fromMainUi, self).dropEvent(event)

            # self.send_pic.emit(MyWindow.browsebutton)

            # self.send_pic.emit(file_name)
            # self.mainUi.guion(file_local=self.file_dir)

            # self.guion(file_local=file_name)
