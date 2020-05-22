import sys

from PySide2.QtWidgets import QMainWindow, QApplication
import instruction_ui as ins_ui


class Instruction(QMainWindow):

    def __init__(self, parent):
        super().__init__()

        self.index = 0

        self.ui_ins = ins_ui.Ui_MainWindow()
        self.ui_ins.setupUi(self)

        self.ui_ins.ButtonGroup_pages.buttonClicked[int].connect(self.on_button_clicked_pages)

        print(f"count of widgets - {self.ui_ins.stackedWidget.count()}")

    def on_button_clicked_pages(self, id):
        for button in self.ui_ins.ButtonGroup_pages.buttons():
            if button is self.ui_ins.ButtonGroup_pages.button(id):
                self.ui_ins.stackedWidget.setCurrentIndex(id)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = Instruction()
    application.show()

    sys.exit(app.exec_())
