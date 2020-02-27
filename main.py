import sys
import pytesseract
from PIL import Image, ImageEnhance, ImageShow
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QDesktopWidget, QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from ui import Ui_MainWindow  # импорт нашего сгенерированного файла

images_type = ['.jpg', '.png', 'jpeg']

# app_2 = QApplication(sys.argv)
# resolution = QDesktopWidget().availableGeometry()

# print(resolution)

languages = {"Russian": 'rus',
             "English": 'eng',
             "Ukrainan": 'ukr',
             "Spanish": 'spa',
             "French": 'fra',
             "German": 'deu',
             "Italian": 'ita',
             "Math(test)": 'equ',
             }

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
        self.ui.horizontalSlider_brightness.valueChanged.connect(self.brightness)
        self.ui.horizontalSlider_color_blalance.valueChanged.connect(self.colorbalance)

        self.ui.width.setValidator(QIntValidator())
        self.ui.height.setValidator(QIntValidator())

    def colorbalance(self):
        colorbalance_value = self.ui.horizontalSlider_color_blalance.value()
        colorbalance_value /= 10
        print(colorbalance_value)
        colorbalance_image = self.ui.imagelabel.pixmap()
        colorbalance_image = Image.fromqpixmap(colorbalance_image)

        colorbalance = ImageEnhance.Color(colorbalance_image).enhance(colorbalance_value)

        self.ui.imagelabel.setPixmap(colorbalance.toqpixmap())

    def brightness(self):
        brightness_value = self.ui.horizontalSlider_brightness.value()
        brightness_value /= 10
        print(brightness_value)
        brightness_image = self.ui.imagelabel.pixmap()
        brightness_image = Image.fromqpixmap(brightness_image)

        brightness_image = ImageEnhance.Brightness(brightness_image).enhance(brightness_value)

        self.ui.imagelabel.setPixmap(brightness_image.toqpixmap())

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
        fortxt = self.ui.imagelabel.pixmap()
        fortxt = Image.fromqpixmap(fortxt)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        try:
            pytesseract.image_to_osd(fortxt)
        except pytesseract.pytesseract.TesseractError as te:
            print(te)
        else:
        lang = self.ui.comboBox.currentText()
        text = pytesseract.image_to_string(fortxt, lang=languages[lang])
        if text == '':
            QMessageBox.about(self, 'Error', "Text hasn't found")
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Success")
            msg.setInformativeText("")
            msg.setWindowTitle("Result")
            msg.setDetailedText(text)
            msg.setStandardButtons(QMessageBox.Save | QMessageBox.Close)

            res = msg.exec_()
            if res == QMessageBox.Save:
                name = QtWidgets.QFileDialog.getSaveFileName(self, "Save result", "",
                                                             filter=".txt",
                                                             )
                file = open(name[0], 'w')
                file.write(text)
                file.close()


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
