from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
import pyside2uic
app = QApplication()
import dene2
s = pyside2uic.compileUi("untitled.ui", dene2.write)
main_window = QUiLoader().load("untitled.ui")

app.exec_()
