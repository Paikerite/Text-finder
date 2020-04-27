###############################################
# Только Бог и я, разбирались в этом дерьме,
# Теперь только Бог. Удачи!
##############################################
import sys
import pytesseract
from copy import copy
from PIL import Image, ImageEnhance, ImageShow, ImageFilter
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtGui import QPixmap, QImage, QIntValidator, QPainter, QBrush, QColor
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMessageBox, QMainWindow
from ui import ui, about_tf
import drawing

images_type = ['.jpg', '.png', 'jpeg']

dir = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

BRIGHTNESS_FACTOR_MIN = 0.5
BRIGHTNESS_FACTOR_MAX = 1.5

CONTRAST_FACTOR_MIN = 0.5
CONTRAST_FACTOR_MAX = 1.5

COLORBALANCE_FACTOR_MIN = 0.0
COLORBALANCE_FACTOR_MAX = 2.0

SHARPNESS_FACTOR_MIN = 0.0
SHARPNESS_FACTOR_MAX = 2.0

MEDIANFILTER_FACTOR_MIN = 0.0
MEDIANFILTER_FACTOR_MAX = 3.0

GAUSSIANBLUR_FACTOR_MIN = 0.0
GAUSSIANBLUR_FACTOR_MAX = 2.0

UNSHARPMASK_FACTOR_MIN = 0.0
UNSHARPMASK_FACTOR_MAX = 2.0

languages = {"Russian": 'rus',
             "English": 'eng',
             "Ukrainan": 'ukr',
             "Spanish": 'spa',
             "French": 'fra',
             "German": 'deu',
             "Italian": 'ita',
             "Math(test)": 'equ',
             }


def calculating(from_slider_value, min, max):
    value = from_slider_value
    value = (value + 100) / (100 + 100)
    value = min + value * (max - min)
    print(value)

    return value


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # self.threadpool = QtCore.QThreadPool()
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.image = None
        self.pixmap = None
        self.b_and_w_image_updated = None
        self.backup_image_updated = None
        self.image_for_enchance_reset = None
        self.ui.pushButton.clicked.connect(self.buttonbegin)
        self.ui.pushButton_2.clicked.connect(self.browsebutton)
        self.ui.checkBox_2.clicked.connect(self.black_and_white)
        self.ui.pushButton_3.clicked.connect(self.scalecheck)
        self.ui.resetScale.clicked.connect(self.scalereset)
        self.ui.areaSelection_button.clicked.connect(self.areaSelection)
        self.ui.pushButton_Reset_enhance.clicked.connect(self.enchancereset)
        self.ui.horizontalSlider.sliderReleased.connect(self.highcontrast)
        self.ui.horizontalSlider_brightness.sliderReleased.connect(self.brightness)
        self.ui.horizontalSlider_color_blalance.sliderReleased.connect(self.colorbalance)
        self.ui.horizontalSlider_for_sharpness.sliderReleased.connect(self.sharpness)
        self.ui.checkBox_medianfilter.clicked.connect(self.medianfilter)
        self.ui.horizontalSlider_unsharmask.sliderReleased.connect(self.unsharmask)
        self.ui.horizontalSlider_gaussian.sliderReleased.connect(self.gaussianblur)
        self.ui.comboBox.addItems(
            ["Russian", "English", "Ukrainan", "Spanish", "French", "German", "Italian", "Math(test)"])
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
        self.ab = uic.loadUi("about.ui")
        self.ab.show()

    def areaSelection(self):
        self.uidraw = drawing.MyWidget(self.ui.imagelabel.pixmap())
        self.uidraw.show()

    def medianfilter(self, state):
        backup_image = self.ui.imagelabel.pixmap()
        if state is True:
            backup_image_updated = Image.fromqpixmap(backup_image)

            self.backup_image_updated = backup_image_updated.filter(ImageFilter.MedianFilter())
            self.ui.imagelabel.setPixmap(self.backup_image_updated.toqpixmap())
        elif state is False:
            try:
                self.ui.imagelabel.setPixmap(QPixmap.fromImage(self.pixmap))
            except NameError as ne:
                print(ne)
                self.ui.imagelabel.setPixmap(QPixmap.fromImage(self.image))

    def unsharmask(self):
        image = Image.fromqpixmap(self.ui.imagelabel.pixmap())

        value = calculating(self.ui.horizontalSlider_unsharmask.value(),
                            UNSHARPMASK_FACTOR_MIN,
                            UNSHARPMASK_FACTOR_MAX)

        image = image.filter(ImageFilter.UnsharpMask(radius=value))

        self.ui.imagelabel.setPixmap(image.toqpixmap())

    def gaussianblur(self):
        image = Image.fromqpixmap(self.ui.imagelabel.pixmap())

        value = calculating(self.ui.horizontalSlider_gaussian.value(),
                            GAUSSIANBLUR_FACTOR_MIN,
                            GAUSSIANBLUR_FACTOR_MAX)

        image = image.filter(ImageFilter.GaussianBlur(radius=value))

        self.ui.imagelabel.setPixmap(image.toqpixmap())

    def colorbalance(self):
        image = Image.fromqpixmap(self.ui.imagelabel.pixmap())

        value = calculating(self.ui.horizontalSlider_color_blalance.value(),
                            COLORBALANCE_FACTOR_MIN,
                            COLORBALANCE_FACTOR_MAX)

        image = ImageEnhance.Color(image)
        image = image.enhance(value)

        self.ui.imagelabel.setPixmap(image.toqpixmap())

    def brightness(self):
        image = Image.fromqpixmap(self.ui.imagelabel.pixmap())

        value = calculating(self.ui.horizontalSlider_brightness.value(),
                            BRIGHTNESS_FACTOR_MIN,
                            BRIGHTNESS_FACTOR_MAX)

        image = ImageEnhance.Brightness(image)
        image = image.enhance(value)

        self.ui.imagelabel.setPixmap(image.toqpixmap())

    def highcontrast(self):
        image = Image.fromqpixmap(self.ui.imagelabel.pixmap())

        value = calculating(self.ui.horizontalSlider.value(),
                            CONTRAST_FACTOR_MIN,
                            CONTRAST_FACTOR_MAX)

        image = ImageEnhance.Contrast(image)
        image = image.enhance(value)

        self.ui.imagelabel.setPixmap(image.toqpixmap())

    def sharpness(self):
        image = Image.fromqpixmap(self.ui.imagelabel.pixmap())

        value = calculating(self.ui.horizontalSlider_for_sharpness.value(),
                            SHARPNESS_FACTOR_MIN,
                            SHARPNESS_FACTOR_MAX)

        image = ImageEnhance.Sharpness(image)
        image = image.enhance(value)

        self.ui.imagelabel.setPixmap(image.toqpixmap())

    def enchancereset(self):
        if self.ui.checkBox_2.isChecked():
            self.ui.imagelabel.setPixmap(self.b_and_w_image_updated.toqpixmap())
        else:
            try:
                self.ui.imagelabel.setPixmap(QPixmap.fromImage(self.pixmap))
            except NameError as ne:
                print(ne)
                self.ui.imagelabel.setPixmap(QPixmap.fromImage(self.image_for_enchance_reset))

        self.ui.horizontalSlider_color_blalance.setValue(0)
        self.ui.horizontalSlider.setValue(0)
        self.ui.horizontalSlider_brightness.setValue(0)
        self.ui.horizontalSlider_for_sharpness.setValue(0)
        self.ui.horizontalSlider_unsharmask.setValue(0)
        self.ui.horizontalSlider_gaussian.setValue(0)
        self.ui.checkBox_medianfilter.setChecked(False)

    def scalereset(self):
        try:
            self.ui.imagelabel.setPixmap(QPixmap.fromImage(self.image))
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
                self.pixmap = self.image.scaled(width, height, QtCore.Qt.KeepAspectRatio)
                self.ui.imagelabel.setPixmap(QPixmap.fromImage(self.pixmap))
            except NameError as ne:
                print(ne)
                QMessageBox.about(self, 'Error', 'Image not found, upload it')

    def browsebutton(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(filter='Images (*.png *.xpm *.jpg *.jpeg)',
                                                         caption='Select image')
        self.ui.lineEdit.setText(filename[0])
        self.image = QImage(filename[0])
        self.image_for_enchance_reset = QImage(filename[0])

        self.ui.imagelabel.setPixmap(QPixmap.fromImage(self.image))
        self.ui.checkBox_2.setChecked(False)

        self.ui.areaSelection_button.setEnabled(True)
        self.ui.ScaleCheckBox.setEnabled(True)
        self.ui.pushButton.setEnabled(True)
        self.ui.checkBox_2.setEnabled(True)
        self.ui.ContrastGroup.setEnabled(True)
        self.ui.progressBar.setEnabled(True)
        self.ui.comboBox.setEnabled(True)

    def black_and_white(self, state):
        b_and_w_image = self.ui.imagelabel.pixmap()
        if state is True:
            b_and_w_image_updated = Image.fromqpixmap(b_and_w_image)

            self.b_and_w_image_updated = b_and_w_image_updated.convert(mode='L')
            self.ui.imagelabel.setPixmap(self.b_and_w_image_updated.toqpixmap())
        elif state is False:
            try:
                self.ui.imagelabel.setPixmap(QPixmap.fromImage(self.pixmap))
            except NameError as ne:
                print(ne)
                self.ui.imagelabel.setPixmap(QPixmap.fromImage(self.image))

    def buttonbegin(self):
        value_for_PB = 0
        fortxt = self.ui.imagelabel.pixmap()

        value_for_PB += 1
        self.ui.progressBar.setValue(value_for_PB)
        fortxt = Image.fromqpixmap(fortxt)

        value_for_PB += 1
        self.ui.progressBar.setValue(value_for_PB)
        pytesseract.pytesseract.tesseract_cmd = dir

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


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())
