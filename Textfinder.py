###############################################
# Только Бог и я, разбирались в этом дерьме,
# Теперь только Бог. Удачи!
##############################################
import os
import sys
from datetime import datetime

import cv2
import pytesseract
from PIL import Image
from PySide2 import QtXml
from PySide2 import QtUiTools
from PySide2.QtCore import Qt, Signal, Slot, QThread
from PySide2.QtGui import QPixmap, QImage, QIntValidator
from PySide2.QtWidgets import QMessageBox, QMainWindow, QFileDialog, QApplication

# import about_tf
import drawing as drawing_file
import img_helper
import instruction as ins
import result
import ui

images_type = ['.jpg', '.png', 'jpeg']

_img_preview = None

dir = r'Tesseract-OCR\tesseract.exe'

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

languages = {"Русский": 'rus',
             "Английский": 'eng',
             "Украинский": 'ukr',
             "Испанский": 'spa',
             "Французский": 'fra',
             "Немецкий": 'deu',
             "Итальянский": 'ita',
             "Математический(test)": 'equ',
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

class RecognizeBegin(QThread):
    signalMain = Signal()
    signalResult = Signal(str, list)
    signalGuion = Signal()
    signalGuioff = Signal()

    def __init__(self, parent=None):
        super(RecognizeBegin, self).__init__(parent=parent)

    def run(self):
        begin = datetime.now()

        self.parent().ui.progressBar.setMaximum(0)
        self.signalGuioff.emit()

        fortxt = self.parent().ui.imagelabel.pixmap()

        fortxt.toImage().save('temp.png', 'png')
        forimage_box = cv2.imread('temp.png')
        os.remove('temp.png')

        fortxt = Image.fromqpixmap(fortxt)
        pytesseract.pytesseract.tesseract_cmd = dir

        text = pytesseract.image_to_string(fortxt, lang='+'.join(self.parent().lang_lst)) #eng+rus
        dict_data = pytesseract.image_to_boxes(fortxt, lang='+'.join(self.parent().lang_lst))

        h, w, _ = forimage_box.shape  # assumes color image

        for b in dict_data.splitlines():
            b = b.split(' ')
            img = cv2.rectangle(forimage_box, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 1)

        print(dict_data)

        if text == '':
            print("empty text")
            self.signalMain.emit()
        else:
            timer = datetime.now() - begin
            self.signalResult.emit(text, [img, timer])

        self.signalGuion.emit()
        self.parent().ui.progressBar.setMaximum(1)


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        # send_pic = pyqtSignal(str)
        # self.imagelabel = imagelabel_fromMainUi(parent=self)

        self.RecognizeBegin = RecognizeBegin(parent=self)
        self.RecognizeBegin.signalMain.connect(self.notfoundtexterr)
        self.RecognizeBegin.signalResult.connect(self.resultWindow)
        self.RecognizeBegin.signalGuion.connect(self.guion)
        self.RecognizeBegin.signalGuioff.connect(self.guioff)
        self.drawing = None
        self.image = None
        self.pixmap = None
        self.b_and_w_image_updated = None
        self.backup_image_updated = None
        self.image_for_enchance_reset = None
        self.ab = None
        self.ins = None
        self.lang_lst = []

        self.ui.imagelabel.resetEvent_signal.connect(self.reset)
        self.ui.imagelabel.dropEvent_Signal.connect(self.guion_withloadfile)
        self.ui.imagelabel.pastEvent_signal.connect(self.guion_withpastefile)
        # self.imagelabel_fromMainUi = imagelabel_fromMainUi()
        # self.imagelabel_fromMainUi.dropEvent_Signal.connect(self.guion_withloadfile)

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
        self.ui.pushButton_add.clicked.connect(self.add_leng)
        self.ui.pushButton_remove.clicked.connect(self.remove_leng)

        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setValue(0)
        self.toknowresolution_of_pixmap()

        self.lang = ["Русский", "Английский", "Украинский",
                     "Испанский", "Французский", "Немецкий",
                     "Итальянский", "Математический(test)"]

        self.ui.comboBox.addItems(self.lang)

        self.ui.About.triggered.connect(self.about)
        self.ui.actionInstructiom.triggered.connect(self.instruction)
        self.ui.actionAbout_Qt.triggered.connect(self.aboutPyqt)

        self.ui.width.setValidator(QIntValidator())
        self.ui.height.setValidator(QIntValidator())

    def toknowresolution_of_pixmap(self):
        try:
            self.width_pixmap = self.ui.imagelabel.pixmap().width()
            self.height_pixmap = self.ui.imagelabel.pixmap().height()
            self.ui.imagelabel.setStatusTip(f"Текущее разрешение - {self.width_pixmap}x{self.height_pixmap}")
        except AttributeError as AE:
            print(AE)

    def aboutPyqt(self):
        QMessageBox.aboutQt(self)

    def instruction(self):
        print("instruction")
        self.ins = ins.Instruction(self)
        self.ins.show()

    def about(self):
        self.ab = QtUiTools.QUiLoader().load(r"ui interface\about.ui")
        self.ab.show()

    def areaSelection(self):
        self.drawing = drawing_file.MyWidget(self, self.ui.imagelabel.pixmap())
        self.drawing.show()

    def black_and_white(self, state):
        operations.blackandwhite = state
        self.place_preview_img()

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

    def add_leng(self):
        lang = self.ui.comboBox.currentText()

        if languages[lang] in self.lang_lst:
            print("already exists in languages list")
        else:
            self.lang_lst.append(languages[lang])

        print(self.lang_lst)
        self.ui.textBrowser_lang.setText(str('\n'.join(self.lang_lst)))

    def remove_leng(self):
        # lang = self.ui.comboBox.currentText()

        # if languages[lang] in self.lang_lst:
        #     # self.lang_lst.remove(self.lang_lst.index(languages[lang]))
        #     self.lang_lst.remove(languages[lang])
        try:
            self.lang_lst.pop()
        except IndexError as IE:
            print(IE)

        self.ui.textBrowser_lang.setText(str('\n'.join(self.lang_lst)))

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
        except TypeError as te:
            print(te)
            self.ui.imagelabel.setPixmap(self.image)

        self.toknowresolution_of_pixmap()

    def scalecheck(self):
        if self.ui.width.text().isdigit() and self.ui.height.text().isdigit():
            width = int(self.ui.width.text())
            height = int(self.ui.height.text())
            print(f"width = {width} height - {height}")

            try:
                if self.ui.radioButton_keepAssRatio.isChecked():
                    self.pixmap = self.image.scaled(width, height, Qt.KeepAspectRatio)
                else:
                    self.pixmap = self.image.scaled(width, height)
                self.ui.imagelabel.setPixmap(QPixmap.fromImage(self.pixmap))
            except TypeError as te:
                print(te)
                self.ui.imagelabel.setPixmap(self.pixmap)

        self.toknowresolution_of_pixmap()

    @Slot(str)
    def guion_withloadfile(self, file_local):
        if file_local:
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
        self.ui.pushButton_add.setEnabled(True)
        self.ui.pushButton_remove.setEnabled(True)
        self.ui.groupBox_lang.setEnabled(True)

        self.ui.horizontalSlider_color_blalance.setValue(0)
        self.ui.horizontalSlider.setValue(0)
        self.ui.horizontalSlider_brightness.setValue(0)
        self.ui.horizontalSlider_for_sharpness.setValue(0)
        self.ui.horizontalSlider_unsharmask.setValue(-100)
        self.ui.horizontalSlider_gaussian.setValue(-100)
        self.ui.checkBox_2.setChecked(False)
        self.ui.checkBox_medianfilter.setChecked(False)

        self.ui.width.clear()
        self.ui.height.clear()

        operations.unsharmask = operations.gaussianblur = operations.color_balance = \
            operations.brightness = operations.contrast = operations.sharpness = 0

        operations.medianfilter = operations.blackandwhite = False

    def guioff(self):
        self.ui.lineEdit.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.areaSelection_button.setEnabled(False)
        self.ui.ScaleCheckBox.setEnabled(False)
        self.ui.pushButton.setEnabled(False)
        self.ui.checkBox_2.setEnabled(False)
        self.ui.ContrastGroup.setEnabled(False)
        self.ui.progressBar.setEnabled(False)
        self.ui.comboBox.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_5.setEnabled(False)
        self.ui.pushButton_rotate_right.setEnabled(False)
        self.ui.pushButton_rotate_left.setEnabled(False)
        self.ui.horizontalSlider.setEnabled(False)
        self.ui.pushButton_remove.setEnabled(False)
        self.ui.pushButton_add.setEnabled(False)
        self.ui.groupBox_lang.setEnabled(False)

    def guion(self):
        self.ui.lineEdit.setEnabled(True)
        self.ui.pushButton_2.setEnabled(True)
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
        self.ui.pushButton_add.setEnabled(True)
        self.ui.pushButton_remove.setEnabled(True)
        self.ui.groupBox_lang.setEnabled(True)

    def browsebutton(self):
        filename = QFileDialog.getOpenFileName(filter='Images (*.png *.jpg *.jpeg *.bmp *.tiff)',
                                                         caption='Select image')

        print(f"filename - {filename}")

        if filename[0] != '':
            self.guion_withloadfile(file_local=filename[0])
        else:
            pass

        self.toknowresolution_of_pixmap()

    def buttonbegin(self):
        if self.lang_lst:
            self.RecognizeBegin.start()
        else:
            QMessageBox.about(self, 'Error', "No language selected")

###########################################
# Next function for Thread and ImageLabel #
###########################################
    @Slot(str, list)
    def resultWindow(self, text, image_data):

        self.result = result.ResultWidget(self, text, image_data[0], image_data[1])
        self.result.show()

    def notfoundtexterr(self):
        QMessageBox.about(self, 'Error', "Text hasn't found")

    @Slot(str)
    def saveresult(self, text):
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
                                               filter="*.txt;;*.doc;;*.docx;;*.rtf",
                                               )
            try:
                file = open(name[0], 'w')
                file.write(text)
                file.close()
            except FileNotFoundError as fe:
                print(fe)

    @Slot(list)
    def guion_withpastefile(self, image):
        # self.image = QImage(image[0])
        self.image = image[0]
        self.image_for_enchance_reset = image
        self.pixmap = None

        self.ui.imagelabel.setPixmap(QPixmap.fromImage(self.image))

        self.ui.width.clear()
        self.ui.height.clear()
        self.guion()

    @Slot()
    def reset(self):
        self.guioff()
        self.ui.pushButton_2.setEnabled(True)
        self.ui.lineEdit.setEnabled(True)

        self.ui.horizontalSlider_color_blalance.setValue(0)
        self.ui.horizontalSlider.setValue(0)
        self.ui.horizontalSlider_brightness.setValue(0)
        self.ui.horizontalSlider_for_sharpness.setValue(0)
        self.ui.horizontalSlider_unsharmask.setValue(-100)
        self.ui.horizontalSlider_gaussian.setValue(-100)
        self.ui.checkBox_2.setChecked(False)
        self.ui.checkBox_medianfilter.setChecked(False)
        self.ui.width.clear()
        self.ui.height.clear()

        operations.unsharmask = operations.gaussianblur = operations.color_balance = \
            operations.brightness = operations.contrast = operations.sharpness = 0

        operations.medianfilter = operations.blackandwhite = False


if __name__ == "__main__":
    app = QApplication([])
    application = MyWindow()
    application.show()

    print("Textfinder [Version 1.0]")
    sys.exit(app.exec_())
