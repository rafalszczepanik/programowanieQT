import sys
from PyQt5.QtWidgets import QLabel,QHBoxLayout, QVBoxLayout,  QApplication, QWidget ,QPushButton
from  PyQt5.QtCore import  Qt

from MassageBox import MainWindow


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 600, 600)
        self.setFixedSize(600, 600)

        label1 = QLabel('Label 01', self)
        label2 = QLabel('Label 02', self)





        #label1.move(50, 50)
       # label1.setAlignment(Qt.AlignHCenter)
        #label2.move(50, 50)

        verticalBox = QVBoxLayout()
        verticalBox.addStretch(1)
        verticalBox.addWidget(label1)
        verticalBox.addWidget(label2)

        horizontalBox = QHBoxLayout()
        horizontalBox.addStretch(1)
        horizontalBox.addWidget(QLabel('h 1 lable'))
        horizontalBox.addWidget(QLabel('h 1 lable'))
        horizontalBox.addWidget(QLabel('h 1 lable'))
        horizontalBox.addWidget(QPushButton('But 1'))
        horizontalBox.addWidget(QPushButton('But 2'))
        horizontalBox.addWidget(QPushButton('But 3'))


        #horizontalBox.addLayout(verticalBox)
        verticalBox.addLayout(horizontalBox)



        self.setWindowTitle('Aplikacja Qt widget')
        self.setLayout(verticalBox)
       # self.setLayout(horizontalBox)
        self.show()
def main():
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec()