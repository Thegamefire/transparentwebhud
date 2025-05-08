from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets, QtGui


class BrowserWindow:
    def __init__(self, title, url):
        super().__init__()

        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.title = title
        self.set_title(title)
        self.url = url
        self.set_url(url)
        self.__enabled = True

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

    def set_title(self, title):
        self.title = title
        self.browser.setWindowTitle(self.title)

    def set_url(self, url):
        self.url = url
        self.browser.load(self.url)

    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, value):
        self.__enabled = value

    def show_hide(self):
        """shows window if enabled is true, else hide"""
        if self.enabled:
            self.show()
        else:
            self.hide()

    def show(self):
        self.browser.show()

    def hide(self):
        self.browser.hide()
