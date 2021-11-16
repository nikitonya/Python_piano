from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QSound
from PyQt5 import QtGui
import sys


class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Virtual Piano")
        MainWindow.resize(1920, 1080)
        MainWindow.setWindowIcon(QtGui.QIcon("C:\\Users\\nikit\\Desktop\\Учёба\\5 семестр\\Курсовая работа\\Icon.jpg"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btn_do = QtWidgets.QPushButton(self.centralwidget)
        self.btn_do.setGeometry(QtCore.QRect(370, 610, 140, 441))
        self.btn_do.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_do.setObjectName("btn_do")
        self.sound_do = QSound("C:\\Users\\nikit\\Desktop\\Учёба\\5 семестр\\Курсовая работа\\Звуки нот\\doWAV.wav")
        self.btn_do.clicked.connect(self.sound_do.play)

        self.btn_re = QtWidgets.QPushButton(self.centralwidget)
        self.btn_re.setGeometry(QtCore.QRect(510, 610, 140, 441))
        self.btn_re.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_re.setObjectName("btn_re")
        self.sound_re = QSound("C:\\Users\\nikit\\Desktop\\Учёба\\5 семестр\\Курсовая работа\\Звуки нот\\reWAV.wav")
        self.btn_re.clicked.connect(self.sound_re.play)

        self.btn_mi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mi.setGeometry(QtCore.QRect(650, 610, 140, 441))
        self.btn_mi.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_mi.setObjectName("btn_mi")
        self.sound_mi = QSound("C:\\Users\\nikit\\Desktop\\Учёба\\5 семестр\\Курсовая работа\\Звуки нот\\miWAV.wav")
        self.btn_mi.clicked.connect(self.sound_mi.play)

        self.btn_fa = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fa.setGeometry(QtCore.QRect(790, 610, 140, 441))
        self.btn_fa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_fa.setObjectName("btn_fa")
        self.sound_fa = QSound("C:\\Users\\nikit\\Desktop\\Учёба\\5 семестр\\Курсовая работа\\Звуки нот\\faWAV.wav")
        self.btn_fa.clicked.connect(self.sound_fa.play)

        self.btn_sol = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sol.setGeometry(QtCore.QRect(930, 610, 140, 441))
        self.btn_sol.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_sol.setObjectName("btn_sol")
        self.sound_sol = QSound("C:\\Users\\nikit\\Desktop\\Учёба\\5 семестр\\Курсовая работа\\Звуки нот\\solWAV.wav")
        self.btn_sol.clicked.connect(self.sound_sol.play)

        self.btn_lya = QtWidgets.QPushButton(self.centralwidget)
        self.btn_lya.setGeometry(QtCore.QRect(1070, 610, 140, 441))
        self.btn_lya.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_lya.setObjectName("btn_lya")
        self.sound_lya = QSound("C:\\Users\\nikit\\Desktop\\Учёба\\5 семестр\\Курсовая работа\\Звуки нот\\lyaWAV.wav")
        self.btn_lya.clicked.connect(self.sound_lya.play)

        self.btn_si = QtWidgets.QPushButton(self.centralwidget)
        self.btn_si.setGeometry(QtCore.QRect(1210, 610, 140, 441))
        self.btn_si.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_si.setObjectName("btn_si")
        self.sound_si = QSound("C:\\Users\\nikit\\Desktop\\Учёба\\5 семестр\\Курсовая работа\\Звуки нот\\siWAV.wav")
        self.btn_si.clicked.connect(self.sound_si.play)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(770, 330, 521, 141))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(50)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Virtual Piano", "Virtual Piano"))
        self.btn_do.setText(_translate("Virtual Piano", "До"))
        self.btn_re.setText(_translate("Virtual Piano", "Ре"))
        self.btn_mi.setText(_translate("Virtual Piano", "Ми"))
        self.btn_fa.setText(_translate("Virtual Piano", "Фа"))
        self.btn_sol.setText(_translate("Virtual Piano", "Соль"))
        self.btn_lya.setText(_translate("Virtual Piano", "Ля"))
        self.btn_si.setText(_translate("Virtual Piano", "Си"))
        self.label.setText(_translate("Virtual Piano", "Piano"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
