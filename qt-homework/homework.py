# -*- coding: utf-8 -*-


#
# Created: Sun Jul 29 16:45:25 2018
#      by: pyside2-uic  running on PySide2 5.11.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 378)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.istekLine = QtWidgets.QLineEdit(self.centralwidget)
        self.istekLine.setObjectName("istekLine")
        self.verticalLayout.addWidget(self.istekLine)
        self.istekButton = QtWidgets.QPushButton(self.centralwidget)
        self.istekButton.setObjectName("istekButton")
        self.verticalLayout.addWidget(self.istekButton)
        self.cevapText = QtWidgets.QTextEdit(self.centralwidget)
        self.cevapText.setEnabled(True)
        self.cevapText.setObjectName("cevapText")
        self.cevapText.setReadOnly(True)
        self.verticalLayout.addWidget(self.cevapText)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.istekButton.setText(QtWidgets.QApplication.translate("MainWindow", "İstek Yap", None, -1))

