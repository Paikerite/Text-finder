import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QDesktopWidget,QApplication
from PyQt5 import QtWidgets
from ui import Ui_MainWindow  # импорт нашего сгенерированного файла

images_type = ['.jpg', '.png', 'jpeg']

# app_2 = QApplication(sys.argv)
# resolution = QDesktopWidget().availableGeometry()

# print(resolution)


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Buttonbegin)
        self.ui.pushButton_2.clicked.connect(self.Browsebutton)
        self.ui.ScaleCheckBox.stateChanged.connect(self.ScaleCheck)
        self.ui.checkBox_2.clicked.connect(self.Black_And_White)

    def ScaleCheck(self, state):

        if state == QtCore.Qt.Checked:
            pixmap = image.scaled(1030, 677, QtCore.Qt.KeepAspectRatio)
            self.ui.imagelabel.setPixmap(QPixmap.fromImage(pixmap))
        else:
            try:
                self.ui.imagelabel.setPixmap(QPixmap.fromImage(image))
            except NameError as ne:
                print(ne)

    def Browsebutton(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(filter='Images (*.png *.xpm *.jpg *.jpeg)',
                                                         caption='Select image')
        self.ui.lineEdit.setText(filename[0])

        global image
        image = QImage(filename[0])

        self.ui.imagelabel.setPixmap(QPixmap.fromImage(image))

    def Black_And_White(self):
        pass

    def Buttonbegin(self):
        print("Pressed")


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
