import sys

from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QFileDialog
from PIL import Image
from ui_result import Ui_MainWindow


class ResultWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent, text, image_data, timer):
        super().__init__()
        self.setupUi(self)
        self.Parent = parent
        self.result_text = text
        self.image_data = image_data
        # self.timer_result = timer

        self.label_timer.setText(f"recognition time - {timer}")
        self.label_dataimage.setPixmap(Image.fromarray(image_data).toqpixmap())
        self.textBrowser_result.setText(text)
        self.pushButton_save.clicked.connect(self.saveResult)
        self.pushButton_showimage.clicked.connect(self.setTextPage)
        self.pushButton_showtext.clicked.connect(self.setImagePage)
        self.pushButton_back.clicked.connect(self.closeResult)

    def closeResult(self):
        self.close()

    def setTextPage(self):
        self.stackedWidget.setCurrentIndex(1)

    def setImagePage(self):
        self.stackedWidget.setCurrentIndex(0)

    def saveResult(self):
        name = QFileDialog.getSaveFileName(self, "Save result", "",
                                           filter="*.txt;;*.doc;;*.docx;;*.rtf",
                                           )
        try:
            file = open(name[0], 'w')
            file.write(self.textBrowser_result.toPlainText()) # self.result_text
            file.close()
        except FileNotFoundError as fe:
            print(fe)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = ResultWidget()
    application.show()

    sys.exit(app.exec_())