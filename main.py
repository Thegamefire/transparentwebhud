import sys, random
from PySide6 import QtCore, QtWidgets
import browser_window


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    # widget = MyWidget()
    # widget.resize(800, 600)
    # widget.show()

    browser = browser_window.BrowserWindow()
    browser.show()

    sys.exit(app.exec())