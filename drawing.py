import sys

# from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint, QRect, QObject, pyqtSignal, QEvent
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QPainterPath, QBrush
from ui import ui_drawing


class MyWidget(QtWidgets.QMainWindow, ui_drawing.Ui_MainWindow):
    def __init__(self, image=None):
        super().__init__()
        self.setupUi(self)

        if image:
            self.image_from_main = image
            self.label_2.setPixmap(self.image_from_main)
        else:
            pass


class label_2(QtWidgets.QLabel):
    def __init__(self, parent=MyWidget):
        super(label_2, self).__init__()#parent=MyWidget)

        self.begin = QPoint()
        self.end = QPoint()

    def paintEvent(self, event):
        super().paintEvent(event)
        # painter = QPainter(self)
        # painter.drawPixmap(self.rect(), self.label_2.pixmap())
        # br = QBrush(QColor(100, 10, 10, 40))
        # painter.setBrush(br)
        #
        # if self.drawingPath:
        #     painter.drawPath(self.drawingPath)

        qp = QPainter(self)
        br = QBrush(QColor(100, 10, 10, 40)) # 100, 10, 10, 40
        qp.setBrush(br)
        qp.drawRect(QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        # self.positin_label.setText(f"Mouse position. begin - {self.begin.x()} {self.begin.y()} end - {self.end.x()} {self.end.y()}")
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWidget()
    application.show()

    sys.exit(app.exec())