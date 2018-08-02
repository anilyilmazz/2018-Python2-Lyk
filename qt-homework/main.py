from PySide2 import QtCore, QtWidgets
from homework import Ui_MainWindow
import requests

class CustomWindow(Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.cevap =""
        self.cevaplar=[]

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        QtCore.QObject.connect(self.istekButton, QtCore.SIGNAL("clicked()"),self.istek)

    def istek(self):
        self.cevap = requests.post("http://51.15.49.65:8080/",data={"data":self.istekLine.text()}).text
        self.cevapText.setText(self.cevap)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CustomWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
