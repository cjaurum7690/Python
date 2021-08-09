# CJ Aurum -- Aurum Creative
# August 8, 2021
# Unit Converter


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5_ConvertDistance import Distance
from PyQt5_ConvertTemp import Temp
from PyQt5_ConvertWeight import Weight


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(782, 600)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(250, 10, 300, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.main_label.setFont(font)
        self.main_label.setFrameShape(QtWidgets.QFrame.Box)
        self.main_label.setLineWidth(2)
        self.main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label.setObjectName("main_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 80, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.distance_radioButton = QtWidgets.QRadioButton(self.centralwidget, clicked=lambda: self.fill_combo_box(1))
        self.distance_radioButton.setGeometry(QtCore.QRect(170, 120, 150, 30))
        self.distance_radioButton.setObjectName("distance_radioButton")
        self.temp_radioButton = QtWidgets.QRadioButton(self.centralwidget, clicked=lambda: self.fill_combo_box(3))
        self.temp_radioButton.setGeometry(QtCore.QRect(490, 120, 150, 30))
        self.temp_radioButton.setObjectName("temp_radioButton")
        self.weight_radioButton = QtWidgets.QRadioButton(self.centralwidget, clicked=lambda: self.fill_combo_box(2))
        self.weight_radioButton.setGeometry(QtCore.QRect(340, 120, 150, 30))
        self.weight_radioButton.setObjectName("weight_radioButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 160, 361, 351))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 321, 41))
        self.label_2.setObjectName("label_2")
        self.amount_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.amount_lineEdit.setGeometry(QtCore.QRect(100, 60, 161, 31))
        self.amount_lineEdit.setInputMask("")
        self.amount_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.amount_lineEdit.setObjectName("amount_lineEdit")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(20, 100, 321, 191))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.value_from_comboBox = QtWidgets.QComboBox(self.frame_3)
        self.value_from_comboBox.setGeometry(QtCore.QRect(50, 20, 221, 41))
        self.value_from_comboBox.setObjectName("value_from_comboBox")

        self.convert_button = QtWidgets.QPushButton(self.frame, clicked=lambda: self.unit_conversion())
        self.convert_button.setGeometry(QtCore.QRect(130, 310, 91, 31))
        self.convert_button.setObjectName("convert_button")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(400, 160, 361, 351))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.results_description_label = QtWidgets.QLabel(self.frame_2)
        self.results_description_label.setGeometry(QtCore.QRect(20, 10, 321, 41))
        self.results_description_label.setText("")
        self.results_description_label.setObjectName("results_description_label")
        self.results_values_label = QtWidgets.QLabel(self.frame_2)
        self.results_values_label.setGeometry(QtCore.QRect(20, 70, 321, 261))
        self.results_values_label.setText("")
        self.results_values_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.results_values_label.setObjectName("results_values_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_label.setText(_translate("MainWindow", "Unit Converter"))
        self.label.setText(_translate("MainWindow", "What would you like to convert?"))
        self.distance_radioButton.setText(_translate("MainWindow", "Distance"))
        self.temp_radioButton.setText(_translate("MainWindow", "Temperature"))
        self.weight_radioButton.setText(_translate("MainWindow", "Weight"))
        self.label_2.setText(_translate("MainWindow", "What value would you like to convert?"))
        self.amount_lineEdit.setText(_translate("MainWindow", "0"))
        self.convert_button.setText(_translate("MainWindow", "Convert"))


    def fill_combo_box(self, value):
        # Create an Combo box
        my_combo_distance = ["Miles", "Yards", "Feet", "Inches", "Kilometers", "Meters", "Centimeters"]
        my_combo_weight = ['Pounds', 'Ounces', 'US Tons', 'Kilograms', 'Grams', 'Stones']
        my_combo_temp = ['Fahrenheit', 'Celsius', 'Kelvin']

        # Add Items To The Combo Box
        if value == 1:
            self.value_from_comboBox.clear()
            self.value_from_comboBox.addItems(my_combo_distance)
        elif value == 2:
            self.value_from_comboBox.clear()
            self.value_from_comboBox.addItems(my_combo_weight)
        elif value == 3:
            self.value_from_comboBox.clear()
            self.value_from_comboBox.addItems(my_combo_temp)

    def unit_conversion(self):
        try:
            if self.distance_radioButton.isChecked():
                self.results_description_label.setText(
                    self.amount_lineEdit.text() + ' ' + self.value_from_comboBox.currentText() + ' is equivalent to: ')
                my_selection = Distance()
                response = my_selection.distance(self.amount_lineEdit.text(), self.value_from_comboBox.currentText())
                self.results_values_label.setText(response)
            elif self.weight_radioButton.isChecked():
                self.results_description_label.setText(
                    self.amount_lineEdit.text() + ' ' + self.value_from_comboBox.currentText() + ' is equivalent to: ')
                my_selection = Weight()
                response = my_selection.weight(int(self.amount_lineEdit.text()), self.value_from_comboBox.currentText())
                self.results_values_label.setText(response)
            elif self.temp_radioButton.isChecked():
                self.results_description_label.setText(
                    self.amount_lineEdit.text() + ' ' + self.value_from_comboBox.currentText() + ' is equivalent to: ')
                my_selection = Temp()
                response = my_selection.temperature(self.amount_lineEdit.text(), self.value_from_comboBox.currentText())
                self.results_values_label.setText(response)
        except ValueError:
            self.amount_lineEdit.clear()
            self.results_description_label.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
