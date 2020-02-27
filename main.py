import sys
from PIL import Image, ImageEnhance, ImageShow
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QDesktopWidget,QApplication
from PyQt5.QtWidgets import QMessageBox
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
        self.ui.pushButton.clicked.connect(self.buttonbegin)
        self.ui.pushButton_2.clicked.connect(self.browsebutton)
        self.ui.checkBox_2.clicked.connect(self.black_and_white)
        self.ui.pushButton_3.clicked.connect(self.scalecheck)
        self.ui.resetScale.clicked.connect(self.scalereset)
        self.ui.horizontalSlider.valueChanged.connect(self.highcontrast)

        self.ui.width.setValidator(QIntValidator())
        self.ui.height.setValidator(QIntValidator())

    def highcontrast(self):
        value = self.ui.horizontalSlider.value()
        value /= 10
        print(value)
        contrast_image = self.ui.imagelabel.pixmap()
        contrast_image = Image.fromqpixmap(contrast_image)

        contrast_image = ImageEnhance.Contrast(contrast_image).enhance(value)

        self.ui.imagelabel.setPixmap(contrast_image.toqpixmap())

    def scalereset(self):
        try:
            self.ui.imagelabel.setPixmap(QPixmap.fromImage(image))
        except NameError as ne:
            print(ne)
            QMessageBox.about(self, 'Error', 'Image not found, upload it')

    def scalecheck(self):
        try:
            width = int(self.ui.width.text())
            height = int(self.ui.height.text())
            print(f"width = {width} height - {height}")
        except ValueError as ve:
            print(ve)
            QMessageBox.about(self, 'Error', 'Please, fill the empty fields')
            width = ''
            height = ''
        if width == '' or height == '':
            pass
        else:
            try:
                global pixmap
                pixmap = image.scaled(width, height, QtCore.Qt.KeepAspectRatio)
                self.ui.imagelabel.setPixmap(QPixmap.fromImage(pixmap))
            except NameError as ne:
                print(ne)
                QMessageBox.about(self, 'Error', 'Image not found, upload it')

    def browsebutton(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(filter='Images (*.png *.xpm *.jpg *.jpeg)',
                                                         caption='Select image')
        self.ui.lineEdit.setText(filename[0])

        global image
        image = QImage(filename[0])

        self.ui.imagelabel.setPixmap(QPixmap.fromImage(image))

    def black_and_white(self, state):
        b_and_w_image = self.ui.imagelabel.pixmap()
        if state is True:
            b_and_w_image_updated = Image.fromqpixmap(b_and_w_image)

            b_and_w_image_updated = b_and_w_image_updated.convert(mode='1', dither=Image.NONE)
            self.ui.imagelabel.setPixmap(b_and_w_image_updated.toqpixmap())
        elif state is False:
            try:
                self.ui.imagelabel.setPixmap(QPixmap.fromImage(pixmap))
            except NameError as ne:
                print(ne)
                self.ui.imagelabel.setPixmap(QPixmap.fromImage(image))

    def buttonbegin(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("Success")
        msg.setInformativeText("")
        msg.setWindowTitle("Result")
        msg.setDetailedText('result')
        msg.setStandardButtons(QMessageBox.Save)

        res = msg.exec_()
        if res == QMessageBox.Save:
            print('save')



app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
