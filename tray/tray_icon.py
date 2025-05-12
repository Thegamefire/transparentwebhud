import os, sys
from typing import List

from PySide6.QtWidgets import QSystemTrayIcon, QApplication, QMenu
from PySide6.QtGui import QIcon, QAction
from browser_window import BrowserWindow


class TrayIcon(QSystemTrayIcon):
    def __init__(self, app, config_ui, config_path, pages):
        super().__init__()
        self.pages:List[BrowserWindow] = pages
        self.setIcon(QIcon("icon.png"))
        self.activated.connect(lambda: print("clicked"))

        # Creating Menu (For Some Reason Actions Don't get Shown if Created With QAction)
        self.setContextMenu(QMenu())
        self.contextMenu().addAction("Settings")
        self.contextMenu().actions()[-1].triggered.connect(config_ui.show)
        self.contextMenu().addAction("Open Config File")
        self.contextMenu().actions()[-1].triggered.connect(lambda: os.system(config_path))
        print(self.contextMenu().actions())

        self.page_menu = QMenu("Pages")
        self.load_pages()
        self.contextMenu().addMenu(self.page_menu)

        self.contextMenu().addAction("Exit")
        self.contextMenu().actions()[-1].triggered.connect(app.exit)

        self.setVisible(True)

    def load_pages(self):
        self.page_menu.clear()
        for page in self.pages:
            self.page_menu.addAction(page.title)
            self.page_menu.actions()[-1].setCheckable(True)
            self.page_menu.actions()[-1].setChecked(page.enabled)
            action = self.page_menu.actions()[-1]
            page.property_changed.connect(lambda: action.setChecked(page.enabled))
            self.page_menu.actions()[-1].triggered.connect(page.toggle)



if __name__=='__main__':
    class UiEmulator:
        def show(self):
            pass

    ui_emulator = UiEmulator()
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)
    tray = TrayIcon(app, ui_emulator, "icon.png", pages=[BrowserWindow("Test", "https://example.com")])
    sys.exit(app.exec())