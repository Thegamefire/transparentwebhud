import sys

from PySide6 import QtWidgets

import settings


def run(config_file) -> None:
    app = QtWidgets.QApplication([])

    config = settings.Config(config_file)
    for window in config.windows:
        window.show()

    sys.exit(app.exec())
