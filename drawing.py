import sys

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from ui import ui_drawing
import main


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = ui_drawing.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_2.setPixmap(main.MyWindow.image)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.show()


    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(100, 10, 10, 40)) # 100, 10, 10, 40
        qp.setBrush(br)
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        self.ui.positin_label.setText(f"Mouse position. begin - {self.begin.x()} {self.begin.y()} end - {self.end.x()} {self.end.y()}")
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()

#app = QtWidgets.QApplication([])
#application = MyWidget()
#application.show()

#sys.exit(app.exec())
