import sys
from PyQt5 import QtWidgets
from ui import Ui_MainWindow  # импорт нашего сгенерированного файла

images_type = ['.jpg', '.png', 'jpeg']


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Buttonbegin)
        self.ui.pushButton_2.clicked.connect(self.Browsebutton)
        self.ui.pushButton_3.clicked.connect(self.Uploadbutton)

    def Uploadbutton(self):
        pass

    def Browsebutton(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(filter='Images (*.png *.xpm *.jpg *.jpeg)',
                                                         caption='Select image')
        self.ui.lineEdit.setText(filename[0])

    def Buttonbegin(self):
        print("Pressed")


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
