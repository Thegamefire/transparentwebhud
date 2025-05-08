import sys

from PySide6 import QtWidgets

import settings


def run(args: list[str]) -> None:
    app = QtWidgets.QApplication([])

    config = settings.Config(args[1])
    print(config)  # todo -d
    for window in config.windows:
        window.show()

    sys.exit(app.exec())
