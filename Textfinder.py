###############################################
# Только Бог и я, разбирались в этом дерьме,
# Теперь только Бог. Удачи!
##############################################

import sys
import pytesseract
from PIL import Image
from PySide2 import QtUiTools
from PySide2.QtCore import Qt, Signal, Slot
from PySide2.QtGui import QPixmap, QImage, QIntValidator
from PySide2.QtWidgets import QMessageBox, QMainWindow, QFileDialog, QApplication
import img_helper
import ui
import instruction as ins
# import about_tf
import drawing as drawing_file
# from imagelabel_frommainui import imagelabel_fromMainUi

images_type = ['.jpg', '.png', 'jpeg']

_img_preview = None

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


class Operations:
    def __init__(self):
        self.color_filter = None

        self.flip_left = False
        self.flip_top = False
        self.rotation_angle = 0

        self.size = None

        self.brightness = 0
        self.sharpness = 0
        self.contrast = 0
        self.color_balance = 0
        self.unsharmask = 0
        self.gaussianblur = 0
        self.blackandwhite = False
        self.medianfilter = False


operations = Operations()


def _get_img_with_all_operations(self):
    b = operations.brightness
    c = operations.contrast
    s = operations.sharpness
    cb = operations.color_balance
    u = operations.unsharmask
    g = operations.gaussianblur
    baw = operations.blackandwhite
    mf = operations.medianfilter

    if self.pixmap:
        img = Image.fromqpixmap(self.pixmap)
    else:
        img = Image.fromqimage(self.image)

    if mf:
        img = img_helper.medianfilter(img, mf)

    if baw:
        img = img_helper.black_and_white(img, baw)

    if b != 0:
        img = img_helper.brightness(img, b)

    if c != 0:
        img = img_helper.contrast(img, c)

    if s != 0:
        img = img_helper.sharpness(img, s)

    if cb != 0:
        img = img_helper.color_balance(img, cb)

    if u != 0:
        img = img_helper.unsharmask(img, u)

    if g != 0:
        img = img_helper.gaussianblur(img, g)

    if operations.rotation_angle:
        img = img_helper.rotate(img, operations.rotation_angle)

    if operations.flip_left:
        img = img_helper.flip_left(img)

    if operations.flip_top:
        img = img_helper.flip_top(img)

    return img


def calculating(from_slider_value, min, max):
    value = from_slider_value
    value = (value + 100) / (100 + 100)
    value = min + value * (max - min)
    print(value)

    return value


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # self.threadpool = QtCore.QThreadPool()

        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        # send_pic = pyqtSignal(str)
        # self.imagelabel = imagelabel_fromMainUi(self)

        self.drawing = None
        self.image = None
        self.pixmap = None
        self.b_and_w_image_updated = None
        self.backup_image_updated = None
        self.image_for_enchance_reset = None
        self.ab = None
        self.ins = None

        # self.imagelabel.dropEvent_Signal.connect(self.guion)

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
        self.ui.pushButton_rotate_left.clicked.connect(self.on_rotate_left)
        self.ui.pushButton_rotate_right.clicked.connect(self.on_rotate_right)
        self.ui.pushButton_4.clicked.connect(self.on_flip_left)
        self.ui.pushButton_5.clicked.connect(self.on_flip_top)

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
        self.ins = ins.Instruction(self)
        self.ins.show()

    def about(self):
        self.ab = QtUiTools.QUiLoader().load(r"ui interface\about.ui")
        self.ab.show()

    def areaSelection(self):
        self.drawing = drawing_file.MyWidget(self, self.ui.imagelabel.pixmap())
        self.drawing.show()

        # if self.pixmap:
        #     self.pixmap = self.ui.imagelabel.pixmap()
        # elif self.image:
        #     self.image = self.ui.imagelabel.pixmap()
        # else:
        #     print("Warning")

    def black_and_white(self, state):
        operations.blackandwhite = state
        self.place_preview_img()

        # if state is True:
        #     operations.blackandwhite = True
        # elif state is False:
        #     operations.blackandwhite = False

    def medianfilter(self, state):
        operations.medianfilter = state
        self.place_preview_img()

    def unsharmask(self):
        self.ui.horizontalSlider_unsharmask.setToolTip(str(self.ui.horizontalSlider_unsharmask.value()))
        self.ui.horizontalSlider_unsharmask.setStatusTip(str(self.ui.horizontalSlider_unsharmask.value()))

        value = calculating(self.ui.horizontalSlider_unsharmask.value(),
                            UNSHARPMASK_FACTOR_MIN,
                            UNSHARPMASK_FACTOR_MAX)

        operations.unsharmask = value
        self.place_preview_img()

    def gaussianblur(self):
        self.ui.horizontalSlider_gaussian.setToolTip(str(self.ui.horizontalSlider_gaussian.value()))
        self.ui.horizontalSlider_gaussian.setStatusTip(str(self.ui.horizontalSlider_gaussian.value()))
        value = calculating(self.ui.horizontalSlider_gaussian.value(),
                            GAUSSIANBLUR_FACTOR_MIN,
                            GAUSSIANBLUR_FACTOR_MAX)

        operations.gaussianblur = value
        self.place_preview_img()

    def colorbalance(self):
        self.ui.horizontalSlider_color_blalance.setToolTip(str(self.ui.horizontalSlider_color_blalance.value()))
        self.ui.horizontalSlider_color_blalance.setStatusTip(str(self.ui.horizontalSlider_color_blalance.value()))
        value = calculating(self.ui.horizontalSlider_color_blalance.value(),
                            COLORBALANCE_FACTOR_MIN,
                            COLORBALANCE_FACTOR_MAX)

        operations.color_balance = value
        self.place_preview_img()

    def brightness(self):
        self.ui.horizontalSlider_brightness.setToolTip(str(self.ui.horizontalSlider_brightness.value()))
        self.ui.horizontalSlider_brightness.setStatusTip(str(self.ui.horizontalSlider_brightness.value()))
        value = calculating(self.ui.horizontalSlider_brightness.value(),
                            BRIGHTNESS_FACTOR_MIN,
                            BRIGHTNESS_FACTOR_MAX)

        operations.brightness = value
        self.place_preview_img()

    def highcontrast(self):
        self.ui.horizontalSlider.setToolTip(str(self.ui.horizontalSlider.value()))
        self.ui.horizontalSlider.setStatusTip(str(self.ui.horizontalSlider.value()))
        value = calculating(self.ui.horizontalSlider.value(),
                            CONTRAST_FACTOR_MIN,
                            CONTRAST_FACTOR_MAX)

        operations.contrast = value
        self.place_preview_img()

    def sharpness(self):
        self.ui.horizontalSlider_for_sharpness.setToolTip(str(self.ui.horizontalSlider_for_sharpness.value()))
        self.ui.horizontalSlider_for_sharpness.setStatusTip(str(self.ui.horizontalSlider_for_sharpness.value()))
        value = calculating(self.ui.horizontalSlider_for_sharpness.value(),
                            SHARPNESS_FACTOR_MIN,
                            SHARPNESS_FACTOR_MAX)

        operations.sharpness = value
        self.place_preview_img()

    def enchancereset(self):
        if self.pixmap:
            self.ui.imagelabel.setPixmap(self.pixmap)
        elif self.image:
            self.ui.imagelabel.setPixmap(QPixmap.fromImage(self.image)) # self.image_for_enchance_reset
        else:
            self.ui.imagelabel.setPixmap(QPixmap.fromImage(self.image_for_enchance_reset))

        self.ui.horizontalSlider_color_blalance.setValue(0)
        self.ui.horizontalSlider.setValue(0)
        self.ui.horizontalSlider_brightness.setValue(0)
        self.ui.horizontalSlider_for_sharpness.setValue(0)
        self.ui.horizontalSlider_unsharmask.setValue(-100)
        self.ui.horizontalSlider_gaussian.setValue(-100)
        self.ui.checkBox_2.setChecked(False)
        self.ui.checkBox_medianfilter.setChecked(False)

        operations.unsharmask = operations.gaussianblur = operations.color_balance =\
            operations.brightness = operations.contrast = operations.sharpness = 0

        operations.medianfilter = operations.blackandwhite = False

    def on_rotate_left(self):

        operations.rotation_angle = 0 if operations.rotation_angle == 270 else operations.rotation_angle + 90
        self.place_preview_img()

    def on_rotate_right(self):

        operations.rotation_angle = 0 if operations.rotation_angle == -270 else operations.rotation_angle - 90
        self.place_preview_img()

    def on_flip_left(self):

        operations.flip_left = not operations.flip_left
        self.place_preview_img()

    def on_flip_top(self):

        operations.flip_top = not operations.flip_top
        self.place_preview_img()

    def place_preview_img(self):
        img = _get_img_with_all_operations(self)

        preview_pix = img.toqpixmap()
        self.ui.imagelabel.setPixmap(preview_pix)

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
                self.pixmap = self.image.scaled(width, height, Qt.KeepAspectRatio)
                self.ui.imagelabel.setPixmap(QPixmap.fromImage(self.pixmap))
            except NameError as ne:
                print(ne)
                QMessageBox.about(self, 'Error', 'Image not found, upload it')

    def guion(self, file_local):
        print(f"file_local - {file_local}")
        self.ui.lineEdit.setText(file_local)
        self.image = QImage(file_local)
        self.image_for_enchance_reset = QImage(file_local)
        self.pixmap = None

        self.ui.imagelabel.setPixmap(QPixmap.fromImage(self.image))
        self.ui.checkBox_2.setChecked(False)

        self.ui.areaSelection_button.setEnabled(True)
        self.ui.ScaleCheckBox.setEnabled(True)
        self.ui.pushButton.setEnabled(True)
        self.ui.checkBox_2.setEnabled(True)
        self.ui.ContrastGroup.setEnabled(True)
        self.ui.progressBar.setEnabled(True)
        self.ui.comboBox.setEnabled(True)
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_5.setEnabled(True)
        self.ui.pushButton_rotate_right.setEnabled(True)
        self.ui.pushButton_rotate_left.setEnabled(True)
        self.ui.horizontalSlider.setEnabled(True)

        self.ui.horizontalSlider_color_blalance.setValue(0)
        self.ui.horizontalSlider.setValue(0)
        self.ui.horizontalSlider_brightness.setValue(0)
        self.ui.horizontalSlider_for_sharpness.setValue(0)
        self.ui.horizontalSlider_unsharmask.setValue(-100)
        self.ui.horizontalSlider_gaussian.setValue(-100)
        self.ui.checkBox_2.setChecked(False)
        self.ui.checkBox_medianfilter.setChecked(False)

        operations.unsharmask = operations.gaussianblur = operations.color_balance = \
            operations.brightness = operations.contrast = operations.sharpness = 0

        operations.medianfilter = operations.blackandwhite = False

    def browsebutton(self):
        filename = QFileDialog.getOpenFileName(filter='Images (*.png *.jpg *.jpeg)',
                                                         caption='Select image')

        print(f"filename - {filename}")

        if filename[0] != '':
            self.guion(file_local=filename[0])
        else:
            pass

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
        self.ui.progressBar.setValue(value_for_PB)

        try:
            pytesseract.image_to_osd(fortxt)
            value_for_PB += 1
            self.ui.progressBar.setValue(value_for_PB)
        except pytesseract.pytesseract.TesseractError as te:
            print(te)
        except pytesseract.pytesseract.TesseractNotFoundError as fe:
            print(fe)
            QMessageBox.about(self, 'Error', 'Tesseract not found')
               
        lang = self.ui.comboBox.currentText()
        value_for_PB += 1

        self.ui.progressBar.setValue(value_for_PB)
        text = pytesseract.image_to_string(fortxt, lang=languages[lang])
        value_for_PB += 1

        self.ui.progressBar.setValue(value_for_PB)
        if text == '':
            value_for_PB += 1
            self.ui.progressBar.setValue(value_for_PB)
            QMessageBox.about(self, 'Error', "Text hasn't found")
        else:
            value_for_PB += 1
            self.ui.progressBar.setValue(value_for_PB)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Success")
            msg.setInformativeText("")
            msg.setWindowTitle("Result")
            msg.setDetailedText(text)
            msg.setStandardButtons(QMessageBox.Save | QMessageBox.Close)

            res = msg.exec_()
            if res == QMessageBox.Save:
                name = QFileDialog.getSaveFileName(self, "Save result", "",
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
    app = QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec_())
