import sys

# from PyQt5 import QtCore
#import PyQt5.QtWidgets.QRubberBand
from PyQt5.QtWidgets import QRubberBand, QLabel, QWidget
from PyQt5.QtCore import Qt, QPoint, QRect, QObject, pyqtSignal, QEvent, QSize
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QPainterPath, QBrush
from PIL import Image
from . import drawing


class labelimage(QLabel):
    def __init__(self, parent):
        super(labelimage, self).__init__(parent=parent)

        self.originQPoint = None
        self.currentQRubberBand = None
        self.drawing = False
        self.begin = QPoint()
        self.end = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.begin = event.pos()
            self.originQPoint = event.pos()
            self.currentQRubberBand = QRubberBand(QRubberBand.Rectangle, self)
            self.currentQRubberBand.setGeometry(QRect(self.originQPoint, QSize()))
            self.currentQRubberBand.show()
            self.drawing = True

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.end = event.pos()
            self.setStatusTip(f"Mouse position. begin - {self.begin.x()} {self.begin.y()} "
                              f"end - {self.end.x()} {self.end.y()}")

            self.currentQRubberBand.setGeometry(QRect(self.originQPoint, event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        self.currentQRubberBand.hide()
        currentQRect = self.currentQRubberBand.geometry()
        self.currentQRubberBand.deleteLater()

        cropQPixmap = self.pixmap().copy(currentQRect)
        self.setPixmap(cropQPixmap)
        self.drawing = False