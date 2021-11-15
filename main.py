from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):  # Наследуем всё от класса QmainWindow
    def __init__(self):  # Базовая настройка чтобы констуктор был как и у родительского класса
        super(Window, self).__init__()

        self.setWindowTitle("Пианино")
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Это просто текст немаленький")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()  # метод для подстраивания ширины объекта под его содержимое

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Нажми на меня")
        self.btn.setFixedWidth(200)  # ширина для самой кнопки
        self.btn.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText("Вторая надпись")
        self.new_text.move(100,50)
        self.new_text.adjustSize()

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()
