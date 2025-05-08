import sys
from multiprocessing.resource_tracker import cleanup_noop

from PySide6 import QtWidgets
import browser_window
import cli
import ui


def run_gui():
    ui.runGui()


def run_cli():
    cli.run(sys.argv)


def main():
    if len(sys.argv) == 1:
        run_gui()
    else:
        run_cli()


if __name__ == "__main__":
    main()
