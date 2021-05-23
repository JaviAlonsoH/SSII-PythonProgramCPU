from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import guiCode


class MyWindow(QMainWindow, guiCode.Ui_Dialog):
    def __init__(self, parent=None):
        super(MyWindow, guiCode.Ui_Dialog, self).__init__(parent)
        self.setupUi(self)

        sc = Canvas(self, width=5, height=4, dpi=100)
        sc.axes.barh([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

    def loadPlot(self, widget_2):
        wdg = self.parent().splitter.widget()

    def clicked(self):
        self.update()

class Canvas(FigureCanvas):
    def __init__(self, parent=None, ):
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=200)
        super().__init__()
        self.setParent(parent)

        """ Matplotlib Script """

        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)

        self.ax.plot(t, s)

        self.ax.set(xlabel='time (s)', ylabel='voltage (mV)',
                    title='About as simple as it gets, folks')
        self.ax.grid()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QWidget()

    ui = guiCode.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())