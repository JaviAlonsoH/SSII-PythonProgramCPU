from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import matplotlib.pyplot as plt
import sys
import guiCode

#Prueba de pull

class MyWindow(QMainWindow, guiCode.Ui_Dialog):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

    def clicked(self):
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
#    MainWindow = QMainWindow()         # ---
    MainWindow = QWidget()              # +++
    ui = guiCode.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())