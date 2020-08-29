import sys

# from PyQt5 import QtCore
from PySide2 import QtWidgets
from PySide2.QtCore import Slot

import ui_drawing


class MyWidget(QtWidgets.QMainWindow, ui_drawing.Ui_MainWindow):

    def __init__(self, parent, image=None):
        super(MyWidget, self).__init__(parent=parent)
        self.setupUi(self)
        self.Parent = self.parent()
        self.resetPicture.clicked.connect(lambda: self.labelimage.setPixmap(self.image_from_main))
        self.SaveChangedPic.clicked.connect(self.savepicture)

        self.labelimage.signalPos.connect(self.printPos)

        if image:
            self.image_from_main = image
            self.labelimage.setPixmap(self.image_from_main)
        else:
            print('fail load picture')

    def savepicture(self):
        self.Parent.ui.imagelabel.setPixmap(self.labelimage.pixmap())
        if self.Parent.pixmap:
            self.Parent.pixmap = self.labelimage.pixmap()
        else:
            self.Parent.image = self.labelimage.pixmap()

        self.close()

    @Slot(list)
    def printPos(self, lst_pos):
        # lst_pos = [self.begin.x(), self.begin.y(), self.end.x(), self.end.y()]

        self.positin_label.setText(f"Mouse position. begin - {lst_pos[0]} {lst_pos[1]} "
                                   f"end - {lst_pos[2]} {lst_pos[3]}")

# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     application = MyWidget()
#     application.show()
#
#     sys.exit(app.exec_())
