import sys
from PySide6 import QtWidgets
import browser_window
import ui

def main(title, url):
    app = QtWidgets.QApplication([])

    browser = browser_window.BrowserWindow(title, url)

    # todo: set defaults somewhere else
    browser.set_transparent()
    browser.set_frame_enabled(False)
    browser.set_mouse_transparent()
    browser.set_always_on_top()
    browser.move(y=0)

    browser.show()

    sys.exit(app.exec())




if __name__ == "__main__":
    # todo: application should not be started from here
    #main(sys.argv[1], sys.argv[2])

    ui.runGui()


