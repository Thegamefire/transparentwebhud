from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets, QtGui


class BrowserWindow():
    def __init__(self):
        super().__init__()

        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.browser.load("https://reactive.fugi.tech/group")
        self.set_transparent()
        self.browser.page().setBackgroundColor(QtGui.QColorConstants.Transparent)
        self.set_frame_enabled()
        self.set_mouse_transparent()
        self.set_always_on_top()
        self.move(y=0)

    def set_transparent(self, enabled=True):
        self.browser.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, on=enabled)
        self.browser.page().setBackgroundColor(QtGui.QColorConstants.Transparent)

    def set_frame_enabled(self, enabled=True):
        self.browser.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint, on=not enabled)

    def set_mouse_transparent(self, enabled=True):
        self.browser.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, on=enabled)

    def set_always_on_top(self, enabled=True):
        self.browser.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, on=enabled)

    def move(self, x=None, y=None):
        x = x if x else self.browser.x()
        y = y if y else self.browser.y()

        self.browser.move(QtCore.QPoint(x, y))

    def show(self):
        self.browser.show()