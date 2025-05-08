import argparse
import sys
from multiprocessing.resource_tracker import cleanup_noop

from PySide6 import QtWidgets
import browser_window
import cli
import ui


def run_gui():
    ui.runGui()


def run_cli(config_file):
    cli.run(config_file)


def main():
    arg_parser = argparse.ArgumentParser(
        description='transparentwebhud: place transparent browser windows on your screen')

    arg_parser.add_argument('-c', '--config', type=str, help='config file to use', default=None)

    args = arg_parser.parse_args()

    # arg_parser.add_argument('--)
    if args.config is None:
        run_gui()
    else:
        run_cli(args.config)


if __name__ == "__main__":
    main()
