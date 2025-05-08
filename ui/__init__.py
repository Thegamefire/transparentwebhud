import sys
from PySide6 import QtWidgets
from ui.ui_mainwindow_companion import MainWindow


def runGui(app: QtWidgets.QApplication, webpages):
    window = MainWindow(webpages)
    window.setWindowTitle('WebHUD - Config')
    window.show()
    sys.exit(app.exec())
