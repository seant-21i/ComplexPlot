# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
import math
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    i = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(251, 292)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(False)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 231, 111))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 20, 211, 81))
        self.widget.setObjectName("widget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_RZ = QtWidgets.QLabel(self.widget)
        self.label_RZ.setObjectName("label_RZ")
        self.gridLayout_3.addWidget(self.label_RZ, 0, 0, 1, 1)
        self.label_IZ = QtWidgets.QLabel(self.widget)
        self.label_IZ.setObjectName("label_IZ")
        self.gridLayout_3.addWidget(self.label_IZ, 1, 0, 1, 1)
        self.label_PZ = QtWidgets.QLabel(self.widget)
        self.label_PZ.setObjectName("label_PZ")
        self.gridLayout_3.addWidget(self.label_PZ, 2, 0, 1, 1)
        self.label_MZ = QtWidgets.QLabel(self.widget)
        self.label_MZ.setObjectName("label_MZ")
        self.gridLayout_3.addWidget(self.label_MZ, 3, 0, 1, 1)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.gridLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_NRZ = QtWidgets.QLabel(self.widget)
        self.label_NRZ.setObjectName("label_NRZ")
        self.gridLayout_2.addWidget(self.label_NRZ, 0, 0, 1, 1)
        self.label_NIZ = QtWidgets.QLabel(self.widget)
        self.label_NIZ.setObjectName("label_NIZ")
        self.gridLayout_2.addWidget(self.label_NIZ, 1, 0, 1, 1)
        self.label_NPZ = QtWidgets.QLabel(self.widget)
        self.label_NPZ.setObjectName("label_NPZ")
        self.gridLayout_2.addWidget(self.label_NPZ, 2, 0, 1, 1)
        self.label_NMZ = QtWidgets.QLabel(self.widget)
        self.label_NMZ.setObjectName("label_NMZ")
        self.gridLayout_2.addWidget(self.label_NMZ, 3, 0, 1, 1)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.gridLayout_2)
        self.pb_plot = QtWidgets.QPushButton(self.centralwidget)
        self.pb_plot.setEnabled(False)
        self.pb_plot.setGeometry(QtCore.QRect(10, 190, 231, 23))
        self.pb_plot.setObjectName("pb_plot")
        self.pb_Clear = QtWidgets.QPushButton(self.centralwidget)
        self.pb_Clear.setEnabled(False)
        self.pb_Clear.setGeometry(QtCore.QRect(10, 220, 231, 23))
        self.pb_Clear.setObjectName("pb_Clear")
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 231, 53))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_Z = QtWidgets.QLabel(self.widget1)
        self.label_Z.setObjectName("label_Z")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_Z)
        self.le_Z = QtWidgets.QLineEdit(self.widget1)
        self.le_Z.setObjectName("le_Z")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_Z)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.pb_show = QtWidgets.QPushButton(self.widget1)
        self.pb_show.setObjectName("pb_show")
        self.gridLayout.addWidget(self.pb_show, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 251, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_plot = QtWidgets.QAction(MainWindow)
        self.actionSave_plot.setObjectName("actionSave_plot")
        self.actionSave_plot.setEnabled(False)
        self.actionSave_plot_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_plot_2.setObjectName("actionSave_plot_2")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionSave_plot)
        self.menuFile.addAction(self.actionSave_plot_2)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pb_show.clicked.connect(lambda: self.propiedades(self.newNumber()))
        self.pb_plot.clicked.connect(lambda: self.graficar(self.newNumber()))
        self.pb_Clear.clicked.connect(lambda: self.Clear())

        self.actionExit.triggered.connect(QtWidgets.qApp.exit)
        self.actionSave_plot_2.triggered.connect(lambda: self.savePlot())
        self.actionHelp.triggered.connect(lambda: self.ayuda())
        self.actionAbout.triggered.connect(lambda: self.acerdaDe())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Complex Number"))
        self.groupBox.setTitle(_translate("MainWindow", "Information"))
        self.label_RZ.setText(_translate("MainWindow", "Real part:"))
        self.label_IZ.setText(_translate("MainWindow", "Imaginary Part:"))
        self.label_PZ.setText(_translate("MainWindow", "Phase:"))
        self.label_MZ.setText(_translate("MainWindow", "Modulus:"))
        self.label_NRZ.setText(_translate("MainWindow", "-"))
        self.label_NIZ.setText(_translate("MainWindow", "-"))
        self.label_NPZ.setText(_translate("MainWindow", "-"))
        self.label_NMZ.setText(_translate("MainWindow", "-"))
        self.pb_plot.setText(_translate("MainWindow", "Plot"))
        self.pb_Clear.setText(_translate("MainWindow", "Clear"))
        self.label_Z.setText(_translate("MainWindow", "Complex Number:"))
        self.le_Z.setPlaceholderText(_translate("MainWindow", "x+yj"))
        self.pb_show.setText(_translate("MainWindow", "Show Info"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSave_plot.setText(_translate("MainWindow", "Save"))
        self.actionSave_plot_2.setText(_translate("MainWindow", "Save plot"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.statusbar.showMessage("Complex number of the form x+yj")

    def propiedades(self, z):
        rz = z.real
        iz = z.imag
        phase = math.atan(iz / rz)
        modulus = math.sqrt((math.pow(rz, 2)) + (math.pow(iz, 2)))
        print(f"Real part: {rz}")
        self.label_NRZ.setText(str(rz))
        print(f"Imaginary part: {iz}")
        self.label_NIZ.setText(str(iz))
        print(f"Modulus: {modulus}")
        self.label_NMZ.setText(str(modulus))
        print(f"\u03B8: {phase}")
        self.label_NPZ.setText(str(phase))
        plt.close()

    def graficar(self, z):
        rz = z.real
        iz = z.imag
        phase = math.atan(iz / rz)
        modulus = math.sqrt((math.pow(rz, 2)) + (math.pow(iz, 2)))
        limit = 0
        if abs(rz) >= abs(iz):
            limit = abs(rz)*2
        else:
            limit = abs(iz)*2
        ax = plt.subplot(1, 2, 1)
        plt.suptitle(z)
        plt.plot(rz, iz, 'b.')
        plt.plot(0, 0, 'r+')
        plt.grid(color='m', linestyle='dotted', linewidth=0.5)
        plt.xlabel("Real Part")
        plt.xlim(-limit, limit)
        plt.ylabel("Imaginary Part")
        plt.ylim(-limit, limit)
        ax.set_aspect('equal', adjustable='box')
        ax = plt.subplot(1, 2, 2, projection='polar')
        plt.polar(phase, modulus, 'b.')
        plt.show()

    def newNumber(self):
        z = complex(self.le_Z.text())
        self.pb_plot.setEnabled(True)
        self.pb_Clear.setEnabled(True)
        self.groupBox.setEnabled(True)
        return z

    def Clear(self):
        self.pb_plot.setEnabled(False)
        self.pb_Clear.setEnabled(False)
        self.groupBox.setEnabled(False)
        self.le_Z.clear()
        self.label_NRZ.setText("-")
        self.label_NIZ.setText("-")
        self.label_NMZ.setText("-")
        self.label_NPZ.setText("-")
        plt.close()

    def savePlot(self):
        self.i = self.i + 1
        name = "plot" + str(self.i) + ".png"
        plt.savefig(name)

    def ayuda(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle('Ayuda')
        msg.setText("Complex Number Grapher")
        msg.setDetailedText("You can use this tool to plot Complex Numbers and see its propierties")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def acerdaDe(self):
        msg = QMessageBox()
        msg.setWindowTitle("About")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Developed By Antonio Mejia")
        msg.setInformativeText("SEANT")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
