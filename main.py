import argparse
import os
import sys

import colorama
from PySide6 import QtWidgets
from PySide6.QtGui import QGuiApplication
from colorama import Fore, Style

import settings
import ui
from browser_window import BrowserWindow

windows: list[BrowserWindow]


def run_gui(app: QtWidgets.QApplication, pages):
    ui.runGui(app, pages)


def run_cli(app: QtWidgets.QApplication):
    sys.exit(app.exec())


def main():
    colorama.just_fix_windows_console()

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

    if QGuiApplication.platformName() == 'wayland':
        print(f'{Style.DIM}[transparentwebhud] {Style.RESET_ALL}{Fore.YELLOW}WARNING: {Fore.RESET}You are using wayland, '
              f'so positioning and resizing windows via the gui or config file won\'t work. Use your desktop '
              f'environment/window manager\'s settings to automatically position and resize windows. Alternatively, '
              f'you can start the application with the --x11 flag, but this may prevent it from starting.',
              file=sys.stderr)

    config = settings.Config(args.config if args.config else settings.get_default_config())
    windows = config.windows

    if args.config is None:
        run_gui(app, pages=windows)
    else:
        run_cli(app)


if __name__ == "__main__":
    main()
