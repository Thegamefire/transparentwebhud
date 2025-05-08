import argparse
import sys

from PySide6 import QtWidgets

import settings
import ui
from browser_window import BrowserWindow

windows: list[BrowserWindow]


def run_gui(app: QtWidgets.QApplication):
    ui.runGui(app)


def run_cli(app: QtWidgets.QApplication):
    sys.exit(app.exec())


def main():
    arg_parser = argparse.ArgumentParser(
        description='transparentwebhud: place transparent browser windows on your screen')

    arg_parser.add_argument('-c', '--config', type=str, help='config file to use', default=None)

    args = arg_parser.parse_args()

    app = QtWidgets.QApplication()
    config = settings.Config(args.config if args.config else 'test/config1.json')  # todo: make default config
    windows = config.windows

    if args.config is None:
        run_gui(app)
    else:
        run_cli(app)


if __name__ == "__main__":
    main()
