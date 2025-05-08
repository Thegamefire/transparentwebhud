import argparse
import sys

from PySide6 import QtWidgets

import settings
import ui
from browser_window import BrowserWindow

windows: list[BrowserWindow]


def run_gui():
    ui.runGui()


def run_cli(app: QtWidgets.QApplication):
    sys.exit(app.exec())


def main():
    arg_parser = argparse.ArgumentParser(
        description='transparentwebhud: place transparent browser windows on your screen')

    arg_parser.add_argument('-c', '--config', type=str, help='config file to use', default=None)

    args = arg_parser.parse_args()

    app = QtWidgets.QApplication()
    config = settings.Config(args.config)
    windows = config.windows

    if args.config is None:
        run_gui()
    else:
        run_cli(app)


if __name__ == "__main__":
    main()
