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
        self.frameless = False
        self.always_on_top = False
        self.transparent = False
        self.mouse_transparent = False
        self.location = (0,0)

    def __str__(self):
        return f'(BrowserPage name="{self.title}" url="{self.url}")'

    def set_transparent(self, enabled=True):
        self.browser.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, on=enabled)
        self.browser.page().setBackgroundColor(QtGui.QColorConstants.Transparent)
        self.transparent = enabled

        # Reload frame to actuate changes
        self.browser.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint, on=not self.frameless)
        self.browser.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint, on=self.frameless)
        self.browser.show()

    def set_frame_enabled(self, enabled=True):
        self.browser.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint, on=not enabled)
        self.frameless = not enabled
        self.browser.show() #TODO: fix old windows frame bug when disabling at runtime

    def set_mouse_transparent(self, enabled=True):
        # self.browser.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, on=enabled)
        self.browser.setWindowFlag(QtCore.Qt.WindowType.WindowTransparentForInput, on=enabled)
        self.mouse_transparent = enabled
        self.browser.show()

    def set_always_on_top(self, enabled=True):
        self.browser.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, on=enabled)
        self.always_on_top = enabled
        self.browser.show()

    def move(self, x=None, y=None):
        x = x if x else self.browser.x()
        y = y if y else self.browser.y()
        self.location = (x,y)
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
        self.show_hide()

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

    def redraw(self):
        self.browser.hide()
        self.show_hide()