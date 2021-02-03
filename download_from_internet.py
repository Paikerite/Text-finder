from PySide2 import QtWidgets
from PySide2.QtCore import QThread, Signal, Slot
from PySide2.QtGui import QPixmap, QImage
from requests import get
import ui_download_from_internet as ui

class ProgressBar(QThread):
    signalImage = Signal()

    def __init__(self, parent=None):
        super(ProgressBar, self).__init__(parent=parent)

    def run(self):
        self.parent().progressBar_downloadimage.setMaximum(0)
        image = get(self.parent().lineEdit_url.text())
        file = open("temp.png", "wb")
        file.write(image.content)
        file.close()
        # image = QImage("temp.png")
        # piximage = QPixmap.fromImage(QImage("temp.png"))
        self.signalImage.emit()
        self.parent().progressBar_downloadimage.setMaximum(1)

class Download_dialog(QtWidgets.QDialog, ui.Ui_Dialog):

    def __init__(self,parent):
        super(Download_dialog, self).__init__(parent=parent)
        self.setupUi(self)
        self.Parent = self.parent()
        self.buttonBox_ok_or_cancel.accepted.connect(self.download)
        self.buttonBox_ok_or_cancel.rejected.connect(self.cancel)
        self.ProgressBar = ProgressBar(parent=self)

        self.ProgressBar.signalImage.connect(self.send_image)

    def download(self):
        self.ProgressBar.start()

    def cancel(self):
        pass

    @Slot()
    def send_image(self):
        self.Parent.guion_withloadfile(file_local="temp.png")