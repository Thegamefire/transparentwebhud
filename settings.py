import json
from typing import Any

from browser_window import BrowserWindow


class ConfigDefaults:
    TITLE = 'transparentwebhud window'
    URL = 'https://thegamefire.com'
    FRAMELESS = True
    TRANSPARENT = True
    CLICK_THROUGH = True
    ALWAYS_ON_TOP = True
    POS = [0, 0]
    WIDTH = 0
    HEIGHT = 0
    CROP = [0, 0, 0, 0]
    OPACITY = 1
    ENABLED = True


class Config:
    def __init__(self, config_file):
        with open(config_file) as f:
            self.config = json.load(f)
            self.windows: list[BrowserWindow] = []

        window_dict: dict[str, Any]
        for window_dict in self.config:
            if not window_dict.get('enabled', ConfigDefaults.ENABLED):
                continue

            window = BrowserWindow(
                window_dict.get('title', ConfigDefaults.TITLE),
                window_dict.get('url', ConfigDefaults.URL),
            )

            window.set_transparent(window_dict.get('transparent', ConfigDefaults.TRANSPARENT))
            window.set_frame_enabled(not window_dict.get('frameless', ConfigDefaults.FRAMELESS))
            window.set_mouse_transparent(window_dict.get('mouseTransparent', ConfigDefaults.TRANSPARENT))
            window.set_always_on_top(window_dict.get('alwaysOnTop', ConfigDefaults.ALWAYS_ON_TOP))
            pos = window_dict.get('pos', ConfigDefaults.POS)
            window.move(pos[0], pos[1])

            self.windows.append(window)
