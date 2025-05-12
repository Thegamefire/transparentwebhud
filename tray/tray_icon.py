import os, sys
from typing import List

from PySide6.QtWidgets import QSystemTrayIcon, QApplication, QMenu
from PySide6.QtGui import QIcon, QAction
from browser_window import BrowserWindow
from observable_list import ObservableList


class TrayIcon(QSystemTrayIcon):
    def __init__(self, q_app, config_ui, config_path, pages):
        super().__init__()
        self.pages:ObservableList = pages
        self.pages.list_changed.connect(self.load_pages)
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
        self.contextMenu().actions()[-1].triggered.connect(q_app.exit)

        self.setVisible(True)

    def load_pages(self):
        self.page_menu.clear()
        for page in self.pages:
            self.page_menu.addAction(page.title)
            self.page_menu.actions()[-1].setCheckable(True)
            self.page_menu.actions()[-1].setChecked(page.enabled)
            action = self.page_menu.actions()[-1]
            page.property_changed.connect(lambda: action.setChecked(page.enabled))
            self.page_menu.actions()[-1].triggered.connect(lambda: self.set_page_enabled(page, action.isChecked()))

    def set_page_enabled(self, page, enabled):
        print("Setting page mode to: "+str(enabled))
        page.enabled = enabled


if __name__=='__main__':
    class UiEmulator:
        def show(self):
            pass

    ui_emulator = UiEmulator()
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)
    tray = TrayIcon(app, ui_emulator, "icon.png", pages=ObservableList([BrowserWindow("Test", "https://example.com")]))
    sys.exit(app.exec())