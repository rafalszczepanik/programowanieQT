import sys
from PyQt5.QtWidgets import QLabel,QHBoxLayout,QLineEdit,QGridLayout, QVBoxLayout,  QApplication, QWidget ,QPushButton
from  PyQt5.QtCore import  Qt

from MassageBox import MainWindow


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 600, 600)
        self.setFixedSize(300, 300)

        # 0 0 0 1 0 2
        # 1 0 1 1 1 2
        # 2 0 2 1 2 2

        imieLable = QLabel('Imie',self)
        nazwiskoLable = QLabel('Nazwisko', self)

        imieInput = QLineEdit(self)
        nazwiskoInput = QLineEdit(self)
        gridLayout = QGridLayout(self)


        gridLayout.addWidget(imieLable, 0, 0)
        gridLayout.addWidget(nazwiskoLable, 1 , 0)


        gridLayout.addWidget(imieInput, 0 , 1, 1, 2)
        gridLayout.addWidget(nazwiskoInput, 1, 1, 1, 2)

        buttooOk = QPushButton('Ok', self)
        buttooCancel = QPushButton('Cancel', self)
        buttooInfo = QPushButton('Cancel', self)

        gridLayout.addWidget(buttooOk, 2, 1)
        gridLayout.addWidget(buttooInfo, 2, 0)
        gridLayout.addWidget(buttooCancel, 2, 2)












        self.show()

def main():
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    app.exec()