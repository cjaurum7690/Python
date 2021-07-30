# CJ Aurum -- Aurum Creative
# July 29, 2021
# Roll the Dice

import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(533, 312)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 10, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 60, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_num_dice = QtWidgets.QLabel(self.centralwidget)
        self.label_num_dice.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_num_dice.setFont(font)
        self.label_num_dice.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_num_dice.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_num_dice.setObjectName("label_num_dice")
        self.label_num_sides = QtWidgets.QLabel(self.centralwidget)
        self.label_num_sides.setGeometry(QtCore.QRect(10, 60, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_num_sides.setFont(font)
        self.label_num_sides.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_num_sides.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_num_sides.setObjectName("label_num_sides")
        self.label_results = QtWidgets.QLabel(self.centralwidget)
        self.label_results.setGeometry(QtCore.QRect(10, 140, 511, 121))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_results.setFont(font)
        self.label_results.setFrameShape(QtWidgets.QFrame.Box)
        self.label_results.setText("")
        self.label_results.setAlignment(QtCore.Qt.AlignCenter)
        self.label_results.setObjectName("label_results")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.roll())
        self.pushButton.setGeometry(QtCore.QRect(400, 10, 111, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 533, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DiceRoll"))
        self.label_num_dice.setText(_translate("MainWindow", "Number of Dice:"))
        self.label_num_sides.setText(_translate("MainWindow", "Number of Sides per Dice"))
        self.pushButton.setText(_translate("MainWindow", "Roll"))

    def roll(self):
        dice = ''
        output_list = []
        for die in range(1, (int(self.lineEdit.text()) + 1)):
            result = random.randint(1, int(self.lineEdit_2.text()))
            output_list.append(result)

        for i in output_list:
            dice += (str(i) + str('  '))

        self.label_results.setText(dice)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
