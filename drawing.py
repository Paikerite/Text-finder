import sys

# from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint, QRect, QObject, pyqtSignal, QEvent
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QPainterPath, QBrush
import ui_drawing


class MyWidget(QtWidgets.QMainWindow, ui_drawing.Ui_MainWindow):

    def __init__(self, parent, image=None):
        super().__init__()
        self.setupUi(self)
        self.Parent = parent
        self.resetPicture.clicked.connect(lambda: self.labelimage.setPixmap(self.image_from_main))
        self.SaveChangedPic.clicked.connect(self.savepicture)

        if image:
            self.image_from_main = image
            self.labelimage.setPixmap(self.image_from_main)
        else:
            print('fail load picture')

    def savepicture(self):
        self.Parent.imagelabel.setPixmap(self.labelimage.pixmap())
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWidget()
    application.show()

    sys.exit(app.exec())