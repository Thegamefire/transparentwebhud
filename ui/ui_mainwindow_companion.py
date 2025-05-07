from PySide6 import QtWidgets
from ui.ui_mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Adding Listeners
        self.ui.urlInput.textChanged.connect(self.name_update)
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

    def name_update(self):
        name = self.ui.nameInput.text()
        print(f'name changed to {name}') # TODO add Functionality

    def url_update(self):
        url = self.ui.urlInput.text()
        print(f'url changed to {url}') # TODO add Functionality

    def location_update(self):
        x=self.ui.xInput.value()
        y = self.ui.yInput.value()
        print(f'move window to {x}, {y}') # TODO add Functionality

    def size_update(self):
        width = self.ui.widthInput.value()
        height = self.ui.heightInput.value()
        print(f'Change window size to {width}x{height}') # TODO add Functionality

    def crop_update(self):
        cropTop = self.ui.cropTopInput.value()
        cropBottom = self.ui.cropBottomInput.value()
        cropLeft = self.ui.cropLeftInput.value()
        cropRight = self.ui.cropRightInput.value()

        print(f'crop top: {cropTop} bottom: {cropBottom} left: {cropLeft} right: {cropRight}') # TODO add Functionality

    def opacity_update(self):
        opacity = self.ui.opacitySlider.value() /100

        print(f'change opacity to {opacity}')# TODO add Functionality

    def window_properties_update(self):
        frameless = not self.ui.frameCheckBox.isChecked()
        always_on_top = self.ui.alwaysOnTopCheckBox.isChecked()
        transparent = self.ui.transparentCheckBox.isChecked()
        click_through = self.ui.clickThroughCheckBox.isChecked()

        print(f'changed window properties: frameless={frameless} alwaysOnTop={always_on_top} transparent={transparent} clickThrough={click_through}')# TODO add Functionality