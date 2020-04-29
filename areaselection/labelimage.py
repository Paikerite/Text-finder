import sys

# from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint, QRect, QObject, pyqtSignal, QEvent
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QPainterPath, QBrush
from . import drawing


class labelimage(QtWidgets.QLabel):
    def __init__(self, parent):
        super(labelimage, self).__init__(parent=parent)

        self.drawing = False
        self.begin = QPoint()
        self.end = QPoint()

    def paintEvent(self, event):
        super().paintEvent(event)

        qp = QPainter(self)
        br = QBrush(QColor(100, 10, 10, 40)) # 100, 10, 10, 40
        qp.setBrush(br)
        qp.drawRect(QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.begin = event.pos()
            self.end = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        # drawing.MyWidget.positin_label.setText(
        #     f"Mouse position. begin - {self.begin.x()} {self.begin.y()} "
        #     f"end - {self.end.x()} {self.end.y()}")

        # drawing.position.begin_x = self.begin.x()
        # drawing.position.begin_y = self.begin.y()
        #
        # drawing.position.end_x = self.end.x()
        # drawing.position.end_y = self.end.y()

        if self.drawing:
            self.end = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()
        self.drawing = False
