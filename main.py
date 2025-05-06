import sys, random
from PySide6 import QtCore, QtWidgets
import browser_window


def main(title, url):
    app = QtWidgets.QApplication([])

    # widget = MyWidget()
    # widget.resize(800, 600)
    # widget.show()

    browser = browser_window.BrowserWindow(title, url)
    browser.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main("transparentwebhud", "localhost:8080")
