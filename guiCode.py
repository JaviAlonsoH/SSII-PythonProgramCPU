# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '\Users\Javi\PycharmProjects\pythonProject\venv\Scripts\gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1263, 891)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(37, 11, 527, 37))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(37, 54, 251, 800))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.lblAlg = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblAlg.setFont(font)
        self.lblAlg.setLineWidth(-1)
        self.lblAlg.setObjectName("lblAlg")
        self.btnFifo = QtWidgets.QRadioButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnFifo.setFont(font)
        self.btnFifo.setObjectName("btnFifo")
        self.btnSfj = QtWidgets.QRadioButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnSfj.setFont(font)
        self.btnSfj.setObjectName("btnSfj")
        self.btnRoundrobin = QtWidgets.QRadioButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnRoundrobin.setFont(font)
        self.btnRoundrobin.setObjectName("btnRoundrobin")
        self.checkBoxPrio = QtWidgets.QCheckBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBoxPrio.setFont(font)
        self.checkBoxPrio.setObjectName("checkBoxPrio")
        self.verticalLayout_3.addWidget(self.splitter)
        self.lineSeparator = QtWidgets.QFrame(self.groupBox)
        self.lineSeparator.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSeparator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSeparator.setObjectName("lineSeparator")
        self.verticalLayout_3.addWidget(self.lineSeparator)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.lblProc = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft Yi Baiti")
        font.setPointSize(25)
        font.setStrikeOut(False)
        self.lblProc.setFont(font)
        self.lblProc.setAlignment(QtCore.Qt.AlignCenter)
        self.lblProc.setObjectName("lblProc")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditTimeArr = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditTimeArr.setObjectName("lineEditTimeArr")
        self.gridLayout.addWidget(self.lineEditTimeArr, 1, 1, 1, 1)
        self.lblTimeExe = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblTimeExe.setFont(font)
        self.lblTimeExe.setObjectName("lblTimeExe")
        self.gridLayout.addWidget(self.lblTimeExe, 2, 0, 1, 1)
        self.lblNameProc = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblNameProc.setFont(font)
        self.lblNameProc.setObjectName("lblNameProc")
        self.gridLayout.addWidget(self.lblNameProc, 0, 0, 1, 1)
        self.NameProc = QtWidgets.QLineEdit(self.layoutWidget)
        self.NameProc.setObjectName("NameProc")
        self.gridLayout.addWidget(self.NameProc, 0, 1, 1, 1)
        self.lblTimeArr = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblTimeArr.setFont(font)
        self.lblTimeArr.setObjectName("lblTimeArr")
        self.gridLayout.addWidget(self.lblTimeArr, 1, 0, 1, 1)
        self.lineEditTimeExe = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditTimeExe.setObjectName("lineEditTimeExe")
        self.gridLayout.addWidget(self.lineEditTimeExe, 2, 1, 1, 1)
        self.lblProcSaved = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblProcSaved.setFont(font)
        self.lblProcSaved.setObjectName("lblProcSaved")
        self.btnAddProc = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.btnAddProc.setFont(font)
        self.btnAddProc.setObjectName("btnAddProc")
        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.btnGenSim = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnGenSim.setFont(font)
        self.btnGenSim.setIconSize(QtCore.QSize(16, 25))
        self.btnGenSim.setObjectName("btnGenSim")
        self.gridLayout_2.addWidget(self.btnGenSim, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(294, 54, 958, 451))
        self.widget.setObjectName("widget")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(290, 521, 961, 331))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777175))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "Simulador de Planificación de Procesos"))
        self.groupBox.setTitle(_translate("Dialog", "Parameters"))
        self.lblAlg.setText(_translate("Dialog", "Elige el tipo de algoritmo:"))
        self.btnFifo.setText(_translate("Dialog", "First In First Out (FIFO)"))
        self.btnSfj.setText(_translate("Dialog", "SJF (Shortest Job First)"))
        self.btnRoundrobin.setText(_translate("Dialog", "Round Robin"))
        self.checkBoxPrio.setText(_translate("Dialog", "Prioridad"))
        self.lblProc.setText(_translate("Dialog", "Añadir Procesos"))
        self.lblTimeExe.setText(_translate("Dialog", "Tiempo de ejecución:"))
        self.lblNameProc.setText(_translate("Dialog", "Nombre del proceso:"))
        self.lblTimeArr.setText(_translate("Dialog", "Tiempo de llegada:"))
        self.lblProcSaved.setText(_translate("Dialog", "Procesos guardados:"))
        self.btnAddProc.setText(_translate("Dialog", "Añadir Proceso"))
        self.btnGenSim.setText(_translate("Dialog", "Generar Simulacion"))