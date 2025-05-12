import sys

from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QApplication
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QAction


class TrayManager():
    def __init__(self, app:QApplication):
        self.app = app
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon("icon.png"))
        self.tray.setContextMenu(QMenu())
        self.tray.setVisible(True)
        self.add_actions()
        self.tray.activated.connect(self.__on_click)
        self.tray.contextMenu().addAction("Test World")

    def add_actions(self) -> None:
        exit_action = QAction("Exit")
        exit_action.triggered.connect(self.app.exit)
        self.tray.contextMenu().addAction(exit_action)

    def __on_click(self):
        print(self.tray.contextMenu().actions())
        if not self.tray.contextMenu().actions():
            self.add_actions()

class TrayIcon(QSystemTrayIcon):
    def __init__(self, app:QApplication):
        super().__init__()
        self.app = app
        self.setIcon(QIcon("icon.png"))
        self.setContextMenu(self.create_menu())
        self.contextMenu().addAction("Yow")
        self.setVisible(True)

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
        icon = TrayIcon(app)

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