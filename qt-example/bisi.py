# -*- coding: utf-8 -*-

#
# Created: Sat Jul 28 12:30:20 2018
#      by: pyside2-uic  running on PySide2 5.11.1
#
# WARNING! All changes made in this file will be lost!
import random
from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    sayac = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(459, 377)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 230, 88, 27))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 100, 121, 51))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(220, 190, 87, 21))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.set_label_text)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.checkBox.toggle)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Tıkla", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Tıkla falan", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("MainWindow", "CheckBox", None, -1))

    def set_label_text(self):
        a= random.randint(0,1000)
        self.sayac = self.sayac+a
        self.label.setText(str(a))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

