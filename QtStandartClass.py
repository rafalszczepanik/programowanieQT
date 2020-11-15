import sys

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QGraphicsPixmapItem
from PyQt5.QtCore import Qt


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

        buttonOK = QPushButton('Print ok', self)
        buttonOK.resize(50, 25)
        buttonOK.move(self.x - 55, self.y - 30)
        buttonOK.clicked.connect(self.printOk)

        buttonRandom = QPushButton('Print random', self)
        buttonRandom.resize(150, 25)
        buttonRandom.move(self.x - 210, self.y - 30)
        buttonRandom.clicked.connect(self.printOk)
# wyswietlanie obrazu
        mylabel2=QLabel(self)
        image=QPixmap('11.jpg')

 #skalowanie
       # mylabel2.setScaledContents(True)

        mylabel2.setPixmap(image)
        mylabel2.setAlignment(Qt.AlignHCenter)
        self.setCentralWidget(mylabel2)

        self.show()

    def printOk(self):
        print('ok')

    def printRandom(self):
        print('Random')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    app.exec()
