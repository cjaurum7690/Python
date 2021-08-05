# CJ Aurum -- Aurum Creative
# August 5, 2021
# Rock, Paper, Scissors, Lizard, Spock

from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets

image_path = 'YOUR LOCAL FOLDER WITH RPSLS IMAGES'
wins = 0
losses = 0
ties = 0



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.player_label = QtWidgets.QLabel(self.centralwidget)
        self.player_label.setGeometry(QtCore.QRect(140, 80, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player_label.setFont(font)
        self.player_label.setAlignment(QtCore.Qt.AlignCenter)
        self.player_label.setObjectName("player_label")
        self.cpu_label = QtWidgets.QLabel(self.centralwidget)
        self.cpu_label.setGeometry(QtCore.QRect(530, 80, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cpu_label.setFont(font)
        self.cpu_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cpu_label.setObjectName("cpu_label")
        self.cpu_image_label = QtWidgets.QLabel(self.centralwidget)
        self.cpu_image_label.setGeometry(QtCore.QRect(490, 120, 200, 200))
        self.cpu_image_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cpu_image_label.setLineWidth(2)
        self.cpu_image_label.setText("")
        self.cpu_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cpu_image_label.setObjectName("cpu_image_label")
        self.rock_choice = QtWidgets.QRadioButton(self.centralwidget, clicked=lambda: self.player_image(1))
        self.rock_choice.setGeometry(QtCore.QRect(50, 400, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rock_choice.setFont(font)
        self.rock_choice.setChecked(False)
        self.rock_choice.setObjectName("rock_choice")
        self.paper_choice = QtWidgets.QRadioButton(self.centralwidget, clicked=lambda: self.player_image(2))
        self.paper_choice.setGeometry(QtCore.QRect(180, 400, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.paper_choice.setFont(font)
        self.paper_choice.setObjectName("paper_choice")
        self.scissors_choice = QtWidgets.QRadioButton(self.centralwidget, clicked=lambda: self.player_image(3))
        self.scissors_choice.setGeometry(QtCore.QRect(330, 400, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.scissors_choice.setFont(font)
        self.scissors_choice.setObjectName("scissors_choice")
        self.lizard_choice = QtWidgets.QRadioButton(self.centralwidget, clicked=lambda: self.player_image(4))
        self.lizard_choice.setGeometry(QtCore.QRect(490, 400, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lizard_choice.setFont(font)
        self.lizard_choice.setObjectName("lizard_choice")
        self.spock_choice = QtWidgets.QRadioButton(self.centralwidget, clicked=lambda: self.player_image(5))
        self.spock_choice.setGeometry(QtCore.QRect(640, 400, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.spock_choice.setFont(font)
        self.spock_choice.setObjectName("spock_choice")
        self.play_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.play())
        self.play_button.setGeometry(QtCore.QRect(350, 450, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.play_button.setFont(font)
        self.play_button.setObjectName("play_button")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 520, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setText('Game Totals:\tWins: ' + str(wins) + '\tLosses: ' + str(losses) + '\tTies: ' + str(ties))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.reset_totals_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.reset())
        self.reset_totals_button.setGeometry(QtCore.QRect(690, 520, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reset_totals_button.setFont(font)
        self.reset_totals_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.reset_totals_button.setObjectName("reset_totals_button")
        self.game_label = QtWidgets.QLabel(self.centralwidget)
        self.game_label.setGeometry(QtCore.QRect(20, 10, 761, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.game_label.setFont(font)
        self.game_label.setFrameShape(QtWidgets.QFrame.Box)
        self.game_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.game_label.setLineWidth(2)
        self.game_label.setAlignment(QtCore.Qt.AlignCenter)
        self.game_label.setObjectName("game_label")
        self.player_image_label = QtWidgets.QLabel(self.centralwidget)
        self.player_image_label.setGeometry(QtCore.QRect(100, 120, 200, 200))
        self.player_image_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.player_image_label.setLineWidth(2)
        self.player_image_label.setText("")
        self.player_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.player_image_label.setObjectName("player_image_label")
        self.game_results_label = QtWidgets.QLabel(self.centralwidget)
        self.game_results_label.setGeometry(QtCore.QRect(60, 360, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.game_results_label.setFont(font)
        self.game_results_label.setText("")
        self.game_results_label.setAlignment(QtCore.Qt.AlignCenter)
        self.game_results_label.setObjectName("game_results_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.player_label.setText(_translate("MainWindow", "Player Selection"))
        self.cpu_label.setText(_translate("MainWindow", "CPU Selection"))
        self.rock_choice.setText(_translate("MainWindow", "Rock"))
        self.paper_choice.setText(_translate("MainWindow", "Paper"))
        self.scissors_choice.setText(_translate("MainWindow", "Scissors"))
        self.lizard_choice.setText(_translate("MainWindow", "Lizard"))
        self.spock_choice.setText(_translate("MainWindow", "Spock"))
        self.play_button.setText(_translate("MainWindow", "Play"))
        self.reset_totals_button.setText(_translate("MainWindow", "Reset"))
        self.game_label.setText(_translate("MainWindow", "Rock, Paper, Scissors, Lizard, Spock"))

    def player_image(self, player_choice):
        global player_selection
        player_selection = player_choice
        if player_selection == 1:
            self.player_image_label.setPixmap(QtGui.QPixmap(image_path + 'Rock.png'))
        if player_selection == 2:
            self.player_image_label.setPixmap(QtGui.QPixmap(image_path + 'Paper.png'))
        if player_selection == 3:
            self.player_image_label.setPixmap(QtGui.QPixmap(image_path + 'Scissors.png'))
        if player_selection == 4:
            self.player_image_label.setPixmap(QtGui.QPixmap(image_path + 'Lizard.png'))
        if player_selection == 5:
            self.player_image_label.setPixmap(QtGui.QPixmap(image_path + 'Spock.png'))

    def cpu_image(self, cpu_selection):
        if cpu_selection == 1:
            self.cpu_image_label.setPixmap(QtGui.QPixmap(image_path + 'Rock.png'))
        if cpu_selection == 2:
            self.cpu_image_label.setPixmap(QtGui.QPixmap(image_path + 'Paper.png'))
        if cpu_selection == 3:
            self.cpu_image_label.setPixmap(QtGui.QPixmap(image_path + 'Scissors.png'))
        if cpu_selection == 4:
            self.cpu_image_label.setPixmap(QtGui.QPixmap(image_path + 'Lizard.png'))
        if cpu_selection == 5:
            self.cpu_image_label.setPixmap(QtGui.QPixmap(image_path + 'Spock.png'))

    def play(self):
        global wins, losses, ties
        # Get CPU Random Selection
        cpu_selection = randint(1, 5)
        self.cpu_image(cpu_selection)

        # Determine if we won or lost
        if player_selection == 1:  # Rock
            if cpu_selection == 1:
                self.game_results_label.setText("It's A Tie!")
                ties += 1
            elif cpu_selection == 2:  # Paper
                self.game_results_label.setText("Paper Covers Rock! You Lose...")
                losses += 1
            elif cpu_selection == 3:  # Scissors
                self.game_results_label.setText("Rock Crushes Scissors!  You Win!!!")
                wins += 1
            elif cpu_selection == 4:  # Lizard
                self.game_results_label.setText("Rock Squashes Lizard!  You Win!!!")
                wins += 1
            elif cpu_selection == 5:  # Spock
                self.game_results_label.setText("Spock Vaporizes Rock!  You Lose...")
                losses += 1

        # If USer Picks Paper
        if player_selection == 2:  # Paper
            if cpu_selection == 2:
                self.game_results_label.setText("It's A Tie!")
                ties += 1
            elif cpu_selection == 1:  # Rock
                self.game_results_label.setText("Paper Cover Rock! You Win!!!")
                wins += 1
            elif cpu_selection == 3:  # Scissors
                self.game_results_label.setText("Scissors Cuts Paper! You Lose...")
                losses += 1
            elif cpu_selection == 4:  # Lizard
                self.game_results_label.setText("Lizard Eats Paper!  You Lose...")
                losses += 1
            elif cpu_selection == 5:  # Spock
                self.game_results_label.setText("Paper Disproves Spock.  You WIN!!!")
                wins += 1

        # If User Pics Scissors
        if player_selection == 3:  # Scissors
            if cpu_selection == 3:
                self.game_results_label.setText("It's A Tie!")
                ties += 1
            elif cpu_selection == 1:  # Rock
                self.game_results_label.setText("Rock Smashes Scissors! You Lose...")
                losses += 1
            elif cpu_selection == 2:  # Paper
                self.game_results_label.setText("Scissors Cuts Paper! You Win!!!")
                wins += 1
            elif cpu_selection == 4:  # Lizard
                self.game_results_label.setText("Scissors Decapitate Lizard!  You Win!!!")
                wins += 1
            elif cpu_selection == 5:  # Spock
                self.game_results_label.setText("Spock Smashes Scissors!  You Lose...")
                losses += 1

        if player_selection == 4:  # Lizard
            if cpu_selection == 4:
                self.game_results_label.setText("It's A Tie!")
                ties += 1
            elif cpu_selection == 1:  # Rock
                self.game_results_label.setText("Rock Crushes Lizard! You Lose...")
                losses += 1
            elif cpu_selection == 2:  # Paper
                self.game_results_label.setText("Lizard Eats Paper! You Win!!!")
                wins += 1
            elif cpu_selection == 3:  # Scissors
                self.game_results_label.setText("Scissors Decapitate Lizard!  You Lose...")
            elif cpu_selection == 5:  # Spock
                losses += 1
                self.game_results_label.setText("Lizard Poisons Spock!  You Win!!!")
                wins += 1

        if player_selection == 5:  # Spock
            if cpu_selection == 5:
                self.game_results_label.setText("It's A Tie!")
                ties += 1
            elif cpu_selection == 1:  # Rock
                self.game_results_label.setText("Spock Vaporizes Rock! You Win!!!")
                wins += 1
            elif cpu_selection == 2:  # Paper
                self.game_results_label.setText("Paper Disproves Spock!  You Lose...")
                losses += 1
            elif cpu_selection == 3:  # Scissors
                self.game_results_label.setText("Rock Smashes Scissors!  You Win!!!")
                wins += 1
            elif cpu_selection == 4:  # Lizard
                self.game_results_label.setText("Lizard Poisons Spock!  You Lose...")
                losses += 1

        self.updates(wins, losses, ties)

    def updates(self, wins, losses, ties):
        self.label_5.setText('Game Totals:\tWins: ' + str(wins) + '\tLosses: ' + str(losses) + '\tTies: ' + str(ties))

    def reset(self):
        global wins
        global losses
        global ties
        wins = 0
        losses = 0
        ties = 0
        self.updates(wins, losses, ties)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
