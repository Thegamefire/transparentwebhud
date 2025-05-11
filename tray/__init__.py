import sys

from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QApplication
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QAction


class TrayManager():
    def __init__(self, app:QApplication):
        self.app = app
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon("icon.png"))
        self.tray.setContextMenu(self.create_menu())
        self.tray.setVisible(True)

    def create_menu(self) -> QMenu:
        menu = QMenu()
        option1 = QAction("Hello World!")
        quit = QAction("Exit")
        quit.triggered.connect(self.app.quit)
        menu.addAction(option1)
        menu.addAction(quit)
        return menu

class TrayIcon(QSystemTrayIcon):
    def __init__(self, app:QApplication):
        super().__init__()
        self.app = app
        self.setIcon(QIcon("icon.png"))
        self.setContextMenu(self.create_menu())

    def create_menu(self) -> QMenu:
        menu = QMenu()
        option1 = QAction("Hello World!")
        quit = QAction("Exit")
        quit.triggered.connect(self.app.quit)
        menu.addAction(option1)
        menu.addAction(quit)
        return menu


    def on_exit(self):
        pass

if __name__=='__main__':
    def test1():
        app = QtWidgets.QApplication([])
        app.setQuitOnLastWindowClosed(False)
        icon = TrayManager(app)

        sys.exit(app.exec())
    def test2():
        app = QApplication([])
        app.setQuitOnLastWindowClosed(False)

        # Adding an icon
        icon = QIcon("icon.png")

        # Adding item on the menu bar
        tray = QSystemTrayIcon()
        tray.setIcon(icon)
        tray.setVisible(True)

        # Creating the options
        menu = QMenu()
        option1 = QAction("Geeks for Geeks")
        option2 = QAction("GFG")
        menu.addAction(option1)
        menu.addAction(option2)

        # To quit the app
        quit = QAction("Quit")
        quit.triggered.connect(app.quit)
        menu.addAction(quit)

        # Adding options to the System Tray
        tray.setContextMenu(menu)

        sys.exit(app.exec())

    test1()