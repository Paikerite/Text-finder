#
# Только Бог и я, разбирались в этом дерьме,
# Теперь только Бог. Удачи!
#
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

BRIGHTNESS_FACTOR_MIN = 0.5
BRIGHTNESS_FACTOR_MAX = 2

CONTRAST_FACTOR_MIN = 0.5
CONTRAST_FACTOR_MAX = 1.5

COLORBALANCE_FACTOR_MIN = 0.0
COLORBALANCE_FACTOR_MAX = 2.0

SHARPNESS_FACTOR_MIN = 0.0
SHARPNESS_FACTOR_MAX = 2.0

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
        self.ui.pushButton_Reset_enhance.clicked.connect(self.enchancereset)
        self.ui.horizontalSlider.valueChanged.connect(self.highcontrast)
        self.ui.horizontalSlider_brightness.valueChanged.connect(self.brightness)
        self.ui.horizontalSlider_color_blalance.valueChanged.connect(self.colorbalance)
        self.ui.horizontalSlider_for_sharpness.valueChanged.connect(self.sharpness)
        self.ui.comboBox.addItems(["Russian", "English", "Ukrainan", "Spanish", "French", "German", "Italian", "Math(test)"])
        self.ui.About.triggered.connect(self.about)
        self.ui.actionInstructiom.triggered.connect(self.instruction)
        self.ui.actionAbout_Qt.triggered.connect(self.aboutPyqt)

        self.ui.width.setValidator(QIntValidator())
        self.ui.height.setValidator(QIntValidator())

    def aboutPyqt(self):
        QMessageBox.aboutQt(self)

    def instruction(self):
        print('yet dibil')

    def about(self):
        print('dibil')

    def colorbalance(self):
        colorbalance_value = self.ui.horizontalSlider_color_blalance.value()
        # colorbalance_value /= 10

        colorbalance_image = self.ui.imagelabel.pixmap()
        colorbalance_image = Image.fromqpixmap(colorbalance_image)

        colorbalance_value = (colorbalance_value - -100) / (100 - -100)
        colorbalance_value = COLORBALANCE_FACTOR_MIN + colorbalance_value * (
                COLORBALANCE_FACTOR_MAX - COLORBALANCE_FACTOR_MIN)
        print(colorbalance_value)
        colorbalance_enchancer = ImageEnhance.Color(colorbalance_image)
        # colorbalance = ImageEnhance.Color(colorbalance_image).enhance(colorbalance_value)
        colorbalance = colorbalance_enchancer.enhance(colorbalance_value)

        self.ui.imagelabel.setPixmap(colorbalance.toqpixmap())

    def brightness(self):
        brightness_value = self.ui.horizontalSlider_brightness.value()
        # brightness_value /= 10

        brightness_image = self.ui.imagelabel.pixmap()
        brightness_image = Image.fromqpixmap(brightness_image)

        brightness_value = (brightness_value - -100) / (100 - -100)
        brightness_value = BRIGHTNESS_FACTOR_MIN + brightness_value * (
                    BRIGHTNESS_FACTOR_MAX - BRIGHTNESS_FACTOR_MIN)
        print(brightness_value)
        # brightness_image = ImageEnhance.Brightness(brightness_image).enhance(brightness_value)
        brightness_enchancer = ImageEnhance.Brightness(brightness_image)
        brightness = brightness_enchancer.enhance(brightness_value)

        self.ui.imagelabel.setPixmap(brightness.toqpixmap())

    def highcontrast(self):
        value = self.ui.horizontalSlider.value()
        # value /= 10

        contrast_image = self.ui.imagelabel.pixmap()
        contrast_image = Image.fromqpixmap(contrast_image)

        value = (value - -100) / (100 - -100)
        value = CONTRAST_FACTOR_MIN + value * (
                CONTRAST_FACTOR_MAX - CONTRAST_FACTOR_MIN)
        print(value)
        contrast_image = ImageEnhance.Contrast(contrast_image).enhance(value)

        self.ui.imagelabel.setPixmap(contrast_image.toqpixmap())

    def sharpness(self):
        sharpness_value = self.ui.horizontalSlider_for_sharpness.value()

        sharpness_image = self.ui.imagelabel.pixmap()
        sharpness_image = Image.fromqpixmap(sharpness_image)

        sharpness_value = (sharpness_value - -100) / (100 - -100)
        sharpness_value = SHARPNESS_FACTOR_MIN + sharpness_value * (
                SHARPNESS_FACTOR_MAX - SHARPNESS_FACTOR_MIN)
        print(sharpness_value)
        sharpness_image = ImageEnhance.Sharpness(sharpness_image).enhance(sharpness_value)

        self.ui.imagelabel.setPixmap(sharpness_image.toqpixmap())

    def enchancereset(self):
        if self.ui.checkBox_2.isChecked():
            self.ui.imagelabel.setPixmap(b_and_w_image_updatedx2.toqpixmap())
        else:
            try:
                self.ui.imagelabel.setPixmap(QPixmap.fromImage(pixmap))
            except NameError as ne:
                print(ne)
                self.ui.imagelabel.setPixmap(QPixmap.fromImage(image))

        self.ui.horizontalSlider_color_blalance.setValue(0)
        self.ui.horizontalSlider.setValue(0)
        self.ui.horizontalSlider_brightness.setValue(0)
        self.ui.horizontalSlider_for_sharpness.setValue(0)

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
        self.ui.checkBox_2.setChecked(False)

    def black_and_white(self, state):
        b_and_w_image = self.ui.imagelabel.pixmap()
        if state is True:
            b_and_w_image_updated = Image.fromqpixmap(b_and_w_image)

            # b_and_w_image_updated = b_and_w_image_updated.convert(mode='1', dither=Image.NONE)
            global b_and_w_image_updatedx2

            b_and_w_image_updatedx2 = b_and_w_image_updated.convert(mode='L')
            self.ui.imagelabel.setPixmap(b_and_w_image_updatedx2.toqpixmap())
        elif state is False:
            try:
                self.ui.imagelabel.setPixmap(QPixmap.fromImage(pixmap))
            except NameError as ne:
                print(ne)
                self.ui.imagelabel.setPixmap(QPixmap.fromImage(image))

    def buttonbegin(self):
        value_for_PB = 0
        fortxt = self.ui.imagelabel.pixmap()
        value_for_PB += 1
        self.ui.progressBar.setValue(value_for_PB)
        fortxt = Image.fromqpixmap(fortxt)
        value_for_PB += 1
        self.ui.progressBar.setValue(value_for_PB)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        value_for_PB += 1
        self.ui.progressBar.setValue(value_for_PB + 1)
        try:
            pytesseract.image_to_osd(fortxt)
            value_for_PB += 1
            self.ui.progressBar.setValue(value_for_PB + 1)
        except pytesseract.pytesseract.TesseractError as te:
            print(te)
        lang = self.ui.comboBox.currentText()
        value_for_PB += 1
        self.ui.progressBar.setValue(value_for_PB + 1)
        text = pytesseract.image_to_string(fortxt, lang=languages[lang])
        value_for_PB += 1
        self.ui.progressBar.setValue(value_for_PB + 1)
        if text == '':
            QMessageBox.about(self, 'Error', "Text hasn't found")
        else:
            value_for_PB += 1
            self.ui.progressBar.setValue(value_for_PB + 1)
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
                                                             filter="*.txt",
                                                             )
                try:
                    file = open(name[0], 'w')
                    file.write(text)
                    file.close()
                except FileNotFoundError as fe:
                    print(fe)
        self.ui.progressBar.setValue(0)


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
