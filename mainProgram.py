from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import matplotlib.pyplot as plt
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI(self)

    def initUI(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1001, 740)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 471, 741))
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName("widget")
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setGeometry(QtCore.QRect(20, 70, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.spinBox.setFont(font)
        self.spinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox.setAutoFillBackground(False)
        self.spinBox.setObjectName("spinBox")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(270, 80, 91, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(270, 120, 91, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setGeometry(QtCore.QRect(270, 160, 91, 31))
        self.radioButton_3.setObjectName("radioButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 150, 171, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(80, 660, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(270, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(470, 0, 531, 481))
        self.graphicsView.setObjectName("graphicsView")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(470, 480, 531, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioButton.setText(_translate("Dialog", "RadioButton"))
        self.radioButton_2.setText(_translate("Dialog", "RadioButton"))
        self.radioButton_3.setText(_translate("Dialog", "RadioButton"))
        self.pushButton.setText(_translate("Dialog", "Generar simulación"))
        self.label.setText(_translate("Dialog", "Elige el tipo de algoritmo:"))
        self.label_2.setText(_translate("Dialog", "Número de procesos:"))

    def clicked(self):
        self.pushButton.setText("Funciona!")
        self.update()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
