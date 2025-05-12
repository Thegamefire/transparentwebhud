from PySide6.QtCore import QObject, Signal

class ObservableList(QObject):
    """A list that emits signals when modified."""
    item_added = Signal(object)  # emits the added item
    item_removed = Signal(object)  # emits the removed item
    list_changed = Signal()  # generic change signal

    def __init__(self, initial_data=None):
        super().__init__()
        self._data = list(initial_data) if initial_data else []

    def append(self, item):
        self._data.append(item)
        self.item_added.emit(item)
        self.list_changed.emit()

    def insert(self, index, item):
        self._data.insert(index, item)
        self.item_added.emit(item)
        self.list_changed.emit()

    def remove(self, item):
        self._data.remove(item)
        self.item_removed.emit(item)
        self.list_changed.emit()

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return repr(self._data)