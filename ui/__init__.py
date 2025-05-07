import sys
from PySide6 import QtWidgets
from ui.ui_mainwindow_companion import MainWindow

def runGui():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())