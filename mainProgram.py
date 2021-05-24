from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import guiCode


class MyWindow(QWidget, guiCode.Ui_Dialog):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        chart = Canvas(self)


    def loadPlot(self, widget_2):
        self.widget = FigureCanvas(self.ax)

    def clicked(self):
        self.update()

class Canvas(FigureCanvas):
    def __init__(self, parent=None, ):
        fig, self.ax = plt.subplots(figsize=(1, 2), dpi=200)
        super().__init__(fig)
        self.setParent(parent)

        """ Matplotlib Script """

        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)

        self.ax.plot(t, s)

        self.ax.set(xlabel='time (s)', ylabel='voltage (mV)')
        self.ax.grid()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())