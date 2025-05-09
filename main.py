import argparse
import sys
import os

from PySide6 import QtWidgets

import settings
import ui
from browser_window import BrowserWindow

windows: list[BrowserWindow]


def run_gui(app: QtWidgets.QApplication, pages):
    ui.runGui(app, pages)


def run_cli(app: QtWidgets.QApplication):
    sys.exit(app.exec())


def main():
    arg_parser = argparse.ArgumentParser(
        description='transparentwebhud: place transparent browser windows on your screen')

    arg_parser.add_argument('-c', '--config', type=str, help='Config file to use', default=None)
    arg_parser.add_argument('--x11',
                            action='store_true',
                            help='Force application to use x11 (or xwayland) on Linux. This setting may prevent the application from starting on other operating systems.',
                            default=False)
    args = arg_parser.parse_args()

    if args.x11:
        os.environ['QT_QPA_PLATFORM'] = 'xcb'

    app = QtWidgets.QApplication()
    config = settings.Config(args.config if args.config else 'test/config1.json')  # todo: make default config
    windows = config.windows

    if args.config is None:
        run_gui(app, pages=windows)
    else:
        run_cli(app)


if __name__ == "__main__":
    main()
