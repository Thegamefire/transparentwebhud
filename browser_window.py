from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets, QtGui


class BrowserWindow():
    def __init__(self):
        super().__init__()

        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.browser.load("https://reactive.fugi.tech/group")
        self.browser.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.browser.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.browser.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.browser.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.browser.page().setBackgroundColor(QtGui.QColorConstants.Transparent)
        self.browser.show()

