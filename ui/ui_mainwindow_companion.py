from typing import List

from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QStandardItemModel, QStandardItem

from browser_window import BrowserWindow
from ui.ui_mainwindow import Ui_MainWindow
from settings import get_default_browser_window, ConfigBuilder

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, pages):
        super(MainWindow, self).__init__()

        self.selected_page: BrowserWindow | None = None
        self.selected_page_index: int | None = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.set_screen_limits()

        self.pages: List[BrowserWindow] = pages

        self.pageListViewModel = QStandardItemModel(self.ui.listView)
        self.ui.listView.setModel(self.pageListViewModel)
        self.pageListViewModel.itemChanged.connect(self.__on_page_list_item_changed)
        self.load_pagelist()
        self.ui.listView.selectionModel().selectionChanged.connect(self.update_selected_page)
        self.ui.listView.setCurrentIndex(self.pageListViewModel.index(0,0))


        # Adding Listeners
        self.ui.nameInput.textChanged.connect(self.name_update)
        self.ui.urlInput.textChanged.connect(self.url_update)

        self.ui.xInput.valueChanged.connect(self.location_update)
        self.ui.yInput.valueChanged.connect(self.location_update)

        self.ui.widthInput.valueChanged.connect(self.size_update)
        self.ui.heightInput.valueChanged.connect(self.size_update)

        self.ui.cropTopInput.valueChanged.connect(self.crop_update)
        self.ui.cropBottomInput.valueChanged.connect(self.crop_update)
        self.ui.cropLeftInput.valueChanged.connect(self.crop_update)
        self.ui.cropRightInput.valueChanged.connect(self.crop_update)

        self.ui.opacitySlider.valueChanged.connect(self.opacity_update)

        self.ui.frameCheckBox.checkStateChanged.connect(self.window_properties_update)
        self.ui.alwaysOnTopCheckBox.checkStateChanged.connect(self.window_properties_update)
        self.ui.transparentCheckBox.checkStateChanged.connect(self.window_properties_update)
        self.ui.clickThroughCheckBox.checkStateChanged.connect(self.window_properties_update)

        self.ui.enabledCheckBox.checkStateChanged.connect(self.enabled_update)
        self.ui.deleteBtn.clicked.connect(self.delete_current_page)
        self.ui.newPageBtn.clicked.connect(self.new_page)


    def name_update(self):
        name = self.ui.nameInput.text()
        print(f'name changed to {name}')  # TODO add Functionality
        #self.load_pagelist()
        self.selected_page.set_title(name)

    def url_update(self):
        url = self.ui.urlInput.text()
        print(f'url changed to {url}')  # TODO add Functionality
        self.selected_page.set_url(url)

    def enabled_update(self):
        self.selected_page.enabled = self.ui.enabledCheckBox.isChecked()
        #self.load_pagelist()
        print("window toggle")

    def location_update(self):
        x = self.ui.xInput.value()
        y = self.ui.yInput.value()
        print(f'move window to {x}, {y}')  # TODO add Functionality
        self.selected_page.move_tuple(x, y)

    def size_update(self):
        width = self.ui.widthInput.value()
        height = self.ui.heightInput.value()

        self.selected_page.set_size(width, height)
        print(f'Change window size to {width}x{height}')  # TODO add Functionality

    def crop_update(self):
        crop_top = self.ui.cropTopInput.value()
        crop_bottom = self.ui.cropBottomInput.value()
        crop_left = self.ui.cropLeftInput.value()
        crop_right = self.ui.cropRightInput.value()

        self.selected_page.crop_page(crop_top, crop_bottom, crop_left, crop_right)

        self.ui.frameCheckBox.setDisabled(False)
        if (crop_top, crop_bottom, crop_left, crop_right) != (0, 0, 0, 0):
            self.ui.frameCheckBox.setChecked(False)
            self.ui.frameCheckBox.setDisabled(True)

        print(
            f'crop top: {crop_top} bottom: {crop_bottom} left: {crop_left} right: {crop_right}')  # TODO add Functionality

    def opacity_update(self):
        opacity = self.ui.opacitySlider.value() / 100

        print(f'change opacity to {opacity}')  # TODO add Functionality
        self.selected_page.set_opacity(opacity)

    def window_properties_update(self):
        frame_enabled = self.ui.frameCheckBox.isChecked()
        always_on_top = self.ui.alwaysOnTopCheckBox.isChecked()
        transparent = self.ui.transparentCheckBox.isChecked()
        click_through = self.ui.clickThroughCheckBox.isChecked()

        self.selected_page.set_frame_enabled(frame_enabled)
        self.selected_page.set_always_on_top(always_on_top)
        self.selected_page.set_transparent(transparent)
        self.selected_page.set_mouse_transparent(click_through)
        print(
            f'changed window properties: frame_enabled={frame_enabled} alwaysOnTop={always_on_top} transparent={transparent} clickThrough={click_through}')  # TODO add Functionality
        print(f'on page {self.selected_page}')

    def set_screen_limits(self):
        desktop = self.screen().virtualGeometry()
        self.ui.xInput.setMaximum(desktop.right())
        self.ui.xInput.setMinimum(desktop.left())
        self.ui.yInput.setMaximum(desktop.bottom())
        self.ui.yInput.setMinimum(desktop.top())

        self.ui.widthInput.setMaximum(desktop.width())
        self.ui.heightInput.setMaximum(desktop.height())

        print("set sizes to " + str((desktop.left(), desktop.right(), desktop.top(), desktop.bottom())))

    def update_values(self):
        print("updating values")
        self.block_ui_signals(True)
        self.ui.nameInput.setText(self.selected_page.title)
        self.ui.urlInput.setText(self.selected_page.url)

        self.ui.frameCheckBox.setChecked(not self.selected_page.frameless)
        self.ui.alwaysOnTopCheckBox.setChecked(self.selected_page.always_on_top)
        self.ui.transparentCheckBox.setChecked(self.selected_page.transparent)
        self.ui.clickThroughCheckBox.setChecked(self.selected_page.mouse_transparent)

        self.ui.xInput.setValue(self.selected_page.get_location()[0])
        self.ui.yInput.setValue(self.selected_page.get_location()[1])
        self.ui.widthInput.setValue(self.selected_page.get_size()[0])
        self.ui.heightInput.setValue(self.selected_page.get_size()[1])

        self.ui.enabledCheckBox.setChecked(self.selected_page.enabled)

        pageItem = self.pageListViewModel.item(self.selected_page_index)
        pageItem.setText(self.selected_page.title)
        pageItem.setCheckState(QtCore.Qt.CheckState.Checked if self.selected_page.enabled else QtCore.Qt.CheckState.Unchecked)

        self.block_ui_signals(False)

    def block_ui_signals(self, enabled):
        self.ui.nameInput.blockSignals(enabled)
        self.ui.urlInput.blockSignals(enabled)

        self.ui.xInput.blockSignals(enabled)
        self.ui.yInput.blockSignals(enabled)

        self.ui.widthInput.blockSignals(enabled)
        self.ui.heightInput.blockSignals(enabled)

        self.ui.cropTopInput.blockSignals(enabled)
        self.ui.cropBottomInput.blockSignals(enabled)
        self.ui.cropLeftInput.blockSignals(enabled)
        self.ui.cropRightInput.blockSignals(enabled)

        self.ui.opacitySlider.blockSignals(enabled)

        self.ui.frameCheckBox.blockSignals(enabled)
        self.ui.alwaysOnTopCheckBox.blockSignals(enabled)
        self.ui.transparentCheckBox.blockSignals(enabled)
        self.ui.clickThroughCheckBox.blockSignals(enabled)


    def load_pagelist(self):
        self.pageListViewModel.clear()
        for page in self.pages:
            page_list_item = QStandardItem(page.title)
            page_list_item.setCheckable(True)
            page_list_item.setCheckState(QtCore.Qt.CheckState.Checked if page.enabled else QtCore.Qt.CheckState.Unchecked)
            self.pageListViewModel.appendRow(page_list_item)

    def __on_page_list_item_changed(self, item:QStandardItem):
        print("pagelistitem changed")
        page_index = self.pageListViewModel.indexFromItem(item).row()
        page = self.pages[page_index]

        page.enabled = item.checkState() == QtCore.Qt.CheckState.Checked
        page.set_title(item.text())

    def select_page(self, index):
        if self.selected_page is not None:
            self.selected_page.property_changed.disconnect(self.update_values)
        print(f"pages: {self.pages}\n trying to select index: {index}")
        self.selected_page = self.pages[index]
        self.selected_page_index = index
        self.update_values()
        self.selected_page.property_changed.connect(self.update_values)

    def update_selected_page(self):
        print(f'selected indexes: '+str(self.ui.listView.selectedIndexes()))
        if self.pageListViewModel.rowCount()>0 and len(self.ui.listView.selectedIndexes())>0:
            page_index = self.ui.listView.selectedIndexes()[0].row()
            self.select_page(page_index)

    def delete_current_page(self):
        if (self.selected_page is not None):
            self.selected_page.enabled = False
            self.pages.remove(self.selected_page)
            self.pageListViewModel.removeRow(self.selected_page_index)
            self.selected_page = None
            self.selected_page_index = None
            self.update_selected_page()

    def new_page(self):
        self.pages.append(get_default_browser_window())
        self.load_pagelist()

        config_builder = ConfigBuilder()
        for page in self.pages:
            config_builder.add_window(page)

        print(config_builder.get_config())
        del config_builder
