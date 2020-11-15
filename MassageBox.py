import sys, time

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QWidget, QLabel, QPushButton, QGraphicsPixmapItem
from PyQt5.QtCore import Qt
from Tools.scripts.which import msg


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x = 700
        self.y = int(self.x / 2)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Moja apka')
        self.setFixedSize(self.x, self.y)
#wyswietlanie napisu
        mylabel = QLabel('To jest okno glowne')
        mylabel.setAlignment(Qt.AlignHCenter)
        mylabel.setFont(QFont('Times', 20, QFont.Bold, True))
        self.setCentralWidget(mylabel)

        buttonMsg = QPushButton('Show message box', self)
        buttonMsg.resize(150, 25)
        buttonMsg.move( 350,  175)
        buttonMsg.clicked.connect(self.ShowMsgBox)
        self.show()
    def ShowMsgBox(self):
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('Czy chcesz wyjsc')
        msg.setWindowTitle('Message box')
        msg.setStandardButtons(QMessageBox.Yes| QMessageBox.No)
        msg.buttonClicked.connect(self.printStatus)

        runmsg = msg.exec_()
        print("Status", runmsg)

        choice = QMessageBox.question(self, 'Quit', 'Czy chcesz zobaczyc godzine?',
                                      (QMessageBox.Yes | QMessageBox.No))
        if choice == QMessageBox.Yes:

            print(time.localtime())






    def printStatus(self, status):
        print('Status przycisku',status.text())

    def ifExit(self, event):
        choice=QMessageBox.question(self, 'Quit', 'Czy chcesz zobaczyc godzine?', (QMessageBox.Yes | QMessageBox.No, QMessageBox.No))
        if choice == QMessageBox.Yes:

            print(time.localtime())








if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    app.exec()
