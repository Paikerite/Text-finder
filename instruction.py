import sys

from PySide2.QtWidgets import QMainWindow, QApplication
import instruction_ui as ins_ui


class Instruction(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()

        self.ui = ins_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.treeWidget.itemClicked.connect(self.chosen_item)
        count = self.ui.stackedWidget.count()
        print(f"Количество виджетов - {count}")
        for i in range(0, count):
            print(f"{i} - {self.ui.stackedWidget.widget(i)}")
        # print(self.ui.stackedWidget.indexOf(self.ui.page_begin))

    def chosen_item(self):
        tmp = self.ui.treeWidget.currentItem().text(0)

        print(f"Выбран - '{tmp}'")
        if tmp == "Загрузка картинки":
            self.ui.stackedWidget.setCurrentIndex(0)
        elif tmp == "Drag & Drop":
            self.ui.stackedWidget.setCurrentIndex(2)
        elif tmp == "Расположение инструментов":
            self.ui.stackedWidget.setCurrentIndex(8)
        elif tmp == "Размер":
            self.ui.stackedWidget.setCurrentIndex(3)
        elif tmp == "Положение картины":
            self.ui.stackedWidget.setCurrentIndex(4)
        elif tmp == "Обрезка по выделению":
            self.ui.stackedWidget.setCurrentIndex(1)
        elif tmp == "Об программе":
            self.ui.stackedWidget.setCurrentIndex(5)
        elif tmp == "Загрузка картины с помощью копирование":
            self.ui.stackedWidget.setCurrentIndex(7)
        elif tmp == "Выбор языка":
            self.ui.stackedWidget.setCurrentIndex(6)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = Instruction()
    application.show()

    sys.exit(app.exec_())
