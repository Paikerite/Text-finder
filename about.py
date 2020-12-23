import sys

from PySide2.QtWidgets import QMainWindow, QApplication, QWidget

from about_ui import Ui_Form


class AboutProgram(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = AboutProgram()
    application.show()

    sys.exit(app.exec_())
