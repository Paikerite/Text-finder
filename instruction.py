import sys

from PySide2.QtWidgets import QMainWindow, QApplication
import instruction_ui as ins_ui


class Instruction(QMainWindow):

    def __init__(self, parent):
        super().__init__()

        self.index = 0

        self.ui_ins = ins_ui.Ui_MainWindow()
        self.ui_ins.setupUi(self)

        self.ui_ins.pushButton_next.clicked.connect(self.next_page)
        self.ui_ins.pushButton_previous.clicked.connect(self.previous_page)

        print(f"count of widgets - {self.ui_ins.stackedWidget.count()}")

    def next_page(self):
        self.index += 1
        self.ui_ins.stackedWidget.setCurrentIndex(1)

    def previous_page(self):
        self.ui_ins.stackedWidget.setCurrentIndex(3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = Instruction()
    application.show()

    sys.exit(app.exec_())
