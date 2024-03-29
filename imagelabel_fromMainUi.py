import sys

from PySide2.QtCore import QObject, Signal, Qt
from PySide2.QtGui import QGuiApplication, QPixmap, QImage
from PySide2.QtWidgets import QLabel, QWidget, QMenu, QAction

img_format = (".png", ".jpg", ".jpeg", ".bmp", ".tiff")

class imagelabel_fromMainUi(QLabel):
    dropEvent_Signal = Signal(str)
    pastEvent_signal = Signal(list)
    resetEvent_signal = Signal()

    def __init__(self, parent=None):
        super(imagelabel_fromMainUi, self).__init__(parent=parent)
        self.file_dir = None

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

        self.popMenu = QMenu(self)
        self.popMenu.addAction(QAction('Вставить', self, triggered=self.context_trigger_paste))
        self.popMenu.addAction(QAction('Копировать', self, triggered=self.context_trigger_copy))
        self.popMenu.addSeparator()
        self.popMenu.addAction(QAction('Сбросить', self, triggered=self.context_trigger_reset))

        # self.popMenu.triggered[QAction].connect(self.context_trigger)

    def context_trigger_reset(self):
        print("reset")
        self.clear()
        self.resetEvent_signal.emit()

    def context_trigger_copy(self):
        print("copy")
        clipboard = QGuiApplication.clipboard()
        image = self.pixmap()
        try:
            clipboard.setImage(QPixmap.toImage(image))
        except TypeError:
            print("[err] Coping empty file")

    def context_trigger_paste(self):
        clipboard = QGuiApplication.clipboard()
        mimeData = clipboard.mimeData()

        if mimeData.hasImage():
            print("Image has been detected on paste")
            self.pastEvent_signal.emit([mimeData.imageData()])

            # self.setPixmap(QPixmap.fromImage(mimeData.imageData()))
        elif mimeData.hasHtml():
            print("HTML has been detected on paste")
            # setText(mimeData.html())
            # setTextFormat(Qt.RichText)
        elif mimeData.hasText():
            print("Text has been detected on paste")
            # setText(mimeData.text())
            # setTextFormat(Qt.PlainText)
        else:
            print("Cannot display data")

    def on_context_menu(self, point):
        # show context menu
        self.popMenu.exec_(self.mapToGlobal(point))

    def dragEnterEvent(self, event):
        self.setStyleSheet(u'''QLabel {
        background-color: rgb(170, 170, 170);
        }''')

        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            self.file_dir = url.toLocalFile()
            if str(self.file_dir).endswith(img_format):
                print("Dropped file: " + self.file_dir)

                self.dropEvent_Signal.emit(str(self.file_dir))
                print("Send file_dir to main window")
            self.setStyleSheet(u'')
        else:
            self.setStyleSheet(u'')

    def dragLeaveEvent(self, event):
        self.setStyleSheet(u'')
