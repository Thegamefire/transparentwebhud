import json
import os
from typing import Any

import platformdirs

from browser_window import BrowserWindow

_config_dict = dict[str, Any]

DEFAULT_CONFIG = [{
    'title': 'transparentwebhud window',
    'url': 'https://example.com',
}]


class ConfigDefaults:
    TITLE = 'transparentwebhud window'
    URL = 'https://thegamefire.com'
    FRAMELESS = True
    TRANSPARENT = True
    CLICK_THROUGH = False
    ALWAYS_ON_TOP = True
    POSITION = [0, 0]
    SIZE = [640, 480]
    CROP = [0, 0, 0, 0]
    OPACITY = 1
    ENABLED = True


class Config:
    def __init__(self, config_file):
        with open(config_file) as f:
            self.config = json.load(f)
            self.windows: list[BrowserWindow] = []

        window_dict: _config_dict
        for window_dict in self.config:
            self.windows.append(get_browser_window(window_dict))


class ConfigBuilder:
    def __init__(self):
        self.windows: list[_config_dict] = []

    def add_window(self, window: BrowserWindow) -> None:
        self.windows.append({
            'title': window.title,
            'url': window.url,
            'transparent': window.transparent,
            'mouseTransparent': window.mouse_transparent,
            'frameless': window.frameless,
            'alwaysOnTop': window.always_on_top,
            'position': list(window.get_location()),
            'size': list(window.get_size()),
            'crop': list(window.crop),
            'enabled': window.enabled,
        })

    def get_config(self) -> list[_config_dict]:
        return self.windows

    def dump_json(self, file) -> None:
        with open(file, 'w+') as f:
            json.dump(self.windows, f, indent=4)


def get_browser_window(window_dict: _config_dict) -> BrowserWindow:
    window = BrowserWindow(
        window_dict.get('title', ConfigDefaults.TITLE),
        window_dict.get('url', ConfigDefaults.URL),
    )

    window.set_transparent(window_dict.get('transparent', ConfigDefaults.TRANSPARENT))
    window.set_frame_enabled(not window_dict.get('frameless', ConfigDefaults.FRAMELESS))
    window.set_mouse_transparent(window_dict.get('mouseTransparent', ConfigDefaults.CLICK_THROUGH))
    window.set_always_on_top(window_dict.get('alwaysOnTop', ConfigDefaults.ALWAYS_ON_TOP))
    pos = window_dict.get('position', ConfigDefaults.POSITION)
    window.move_tuple(pos[0], pos[1])
    size = window_dict.get('size', ConfigDefaults.SIZE)
    window.set_size(size[0], size[1])
    window.enabled = window_dict.get('enabled', ConfigDefaults.ENABLED)

    return window


def get_default_browser_window() -> BrowserWindow:
    return get_browser_window(DEFAULT_CONFIG[0])


def get_config_dir() -> str:
    """returns the config directory, and makes it if it doesn't exist"""
    path = platformdirs.user_config_dir('transparentwebhud', 'Thegamefire')
    if not os.path.isdir(path):
        os.makedirs(path)

    return path


def _generate_default_config(path: str) -> None:
    with open(path, 'x') as f:
        json.dump(DEFAULT_CONFIG, f)


def get_default_config() -> str:
    """returns the path of the default config, and generates it if it doesn't exist"""
    path = os.path.join(get_config_dir(), 'windows.json')
    if not os.path.isfile(path):
        _generate_default_config(path)

    return path
