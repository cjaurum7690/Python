# CJ Aurum -- Aurum Creative
# July 29, 2021 
# Password Generator for PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import string
from random import randint

class Ui_PasswordGenerator(object):
    def setupUi(self, PasswordGenerator):
        PasswordGenerator.setObjectName("PasswordGenerator")
        PasswordGenerator.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(PasswordGenerator)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.password())
        self.pushButton.setGeometry(QtCore.QRect(239, 130, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton.setObjectName("pushButton")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(50, 200, 281, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setScaledContents(False)
        self.label_1.setObjectName("label_1")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 20, 500, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(5)
        self.frame.setObjectName("frame")
        self.how_many_char_label = QtWidgets.QLabel(self.frame)
        self.how_many_char_label.setGeometry(QtCore.QRect(50, 10, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.how_many_char_label.setFont(font)
        self.how_many_char_label.setAlignment(QtCore.Qt.AlignCenter)
        self.how_many_char_label.setObjectName("how_many_char_label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(195, 50, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 245, 271, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 290, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 180, 490, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line.setFont(font)
        self.line.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 205, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 297, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(320, 253, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        PasswordGenerator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PasswordGenerator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        PasswordGenerator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PasswordGenerator)
        self.statusbar.setObjectName("statusbar")
        PasswordGenerator.setStatusBar(self.statusbar)

        self.retranslateUi(PasswordGenerator)
        QtCore.QMetaObject.connectSlotsByName(PasswordGenerator)

    def retranslateUi(self, PasswordGenerator):
        _translate = QtCore.QCoreApplication.translate
        PasswordGenerator.setWindowTitle(_translate("PasswordGenerator", "Password Generator"))
        self.pushButton.setText(_translate("PasswordGenerator", "Get Password"))
        self.label_1.setText(_translate("PasswordGenerator", "Using a set group of values:"))
        self.how_many_char_label.setText(_translate("PasswordGenerator", "How many characters for the password?"))
        self.label_2.setText(_translate("PasswordGenerator", "Using all letters, numbers, symbols:"))
        self.label_3.setText(_translate("PasswordGenerator", "Using the \'chr\' function:"))


    def password(self):
        options = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*()=+?'
        my_password1 = ''.join((random.choice(options) for i in range(int(self.lineEdit.text()))))
        self.lineEdit_2.setText(my_password1)

        letters = string.ascii_letters
        numbers = string.digits
        symbols = string.punctuation
        my_password2 = "".join(random.sample((letters+numbers+symbols), int(self.lineEdit.text())))
        self.lineEdit_3.setText(my_password2)

        my_password3 = ''
        for x in range(int(self.lineEdit.text())):
            my_password3 += str(chr(randint(33, 126)))
        self.lineEdit_4.setText(my_password3)

        self.lineEdit.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasswordGenerator = QtWidgets.QMainWindow()
    ui = Ui_PasswordGenerator()
    ui.setupUi(PasswordGenerator)
    PasswordGenerator.show()
    sys.exit(app.exec_())
