from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets, QtGui
from PySide6.QtCore import Signal


class BrowserWindow(QtWebEngineWidgets.QWebEngineView):

    property_changed = Signal()

    def __init__(self, title, url):
        super().__init__()

        self.title = title
        self.set_title(title)
        self.url = url
        self.set_url(url)
        self.__enabled = True
        self.frameless = False
        self.always_on_top = False
        self.transparent = False
        self.mouse_transparent = False
        self.opacity = 1
        self.crop = (0,0,0,0)

    def __str__(self):
        return f'(BrowserPage name="{self.title}" url="{self.url}")'

    def set_transparent(self, enabled=True):
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, on=enabled)
        self.page().setBackgroundColor(QtGui.QColorConstants.Transparent)
        self.transparent = enabled

        # Reload frame to actuate changes
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint, on=not self.frameless)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint, on=self.frameless)
        self.show_hide()
        self.__on_change()

    def set_frame_enabled(self, enabled=True):
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint, on=not enabled)

        #Reload Mouse Transparency so it doesn't show old windows titlebar
        self.set_mouse_transparent(not self.mouse_transparent)
        self.set_mouse_transparent(not self.mouse_transparent)

        self.frameless = not enabled
        self.show_hide() #TODO: fix old windows frame bug when disabling at runtime
        self.__on_change()

    def set_mouse_transparent(self, enabled=True):
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, on=enabled)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowTransparentForInput, on=enabled)
        self.mouse_transparent = enabled
        self.show_hide()
        self.__on_change()

    def set_always_on_top(self, enabled=True):
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, on=enabled)
        self.always_on_top = enabled
        self.show_hide()
        self.__on_change()

    def set_opacity(self, opacity):
        self.setWindowOpacity(opacity)
        self.opacity = opacity
        self.show_hide()
        self.__on_change()

    def move_tuple(self, x=None, y=None):
        x = x if x else self.x()
        y = y if y else self.y()
        self.move(QtCore.QPoint(x, y))

    def set_size(self, width, height):
        size = self.size()
        size.setWidth(width)
        size.setHeight(height)
        self.resize(size)
        self.crop_page(*self.crop)


    def crop_page(self, top=0, bottom=0, left=0, right=0):
        self.crop = (top, bottom, left, right)
        if (top, bottom, left, right) == (0,0,0,0):
            self.setMask(QtGui.QRegion())
            self.show_hide()
            return
        width, height = self.get_size()
        clip = QtGui.QRegion(left, top, width-right-left, height-bottom-top)
        self.setMask(clip)
        self.set_frame_enabled(not self.frameless)
        self.show_hide()
        self.__on_change()


    def resizeEvent(self, event, /):
        super().resizeEvent(event)
        self.__on_change()
        return event

    def moveEvent(self, event, /):
        super().moveEvent(event)
        self.__on_change()
        return event

    def __on_change(self):
        self.property_changed.emit()

    def get_size(self) -> tuple:
        return self.size().toTuple()

    def get_location(self) -> tuple:
        return self.pos().toTuple()

    def set_title(self, title):
        self.title = title
        self.setWindowTitle(self.title)
        self.__on_change()

    def set_url(self, url):
        self.url = url
        self.load(self.url)
        self.__on_change()

    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, value):
        self.__enabled = value
        self.show_hide()
        self.__on_change()

    def show_hide(self):
        """shows window if enabled is true, else hide"""
        if self.enabled:
            self.show()
        else:
            self.hide()

