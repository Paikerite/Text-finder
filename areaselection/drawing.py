import sys

# from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint, QRect, QObject, pyqtSignal, QEvent
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QPainterPath, QBrush
from . import ui_drawing


class Position:
    def __init__(self):
        self.begin_x = 0
        self.begin_y = 0

        self.end_x = 0
        self.end_y = 0


position = Position()


class MyWidget(QtWidgets.QMainWindow, ui_drawing.Ui_MainWindow):
    def __init__(self, image=None):
        super().__init__()
        self.setupUi(self)

        if image:
            self.image_from_main = image
            self.labelimage.setPixmap(self.image_from_main)
        else:
            pass

        # self.positin_label.setText(
        #     f"Mouse position. begin - {position.begin_x} {position.begin_y} "
        #     f"end - {position.end_x} {position.end_y}")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWidget()
    application.show()

    sys.exit(app.exec())