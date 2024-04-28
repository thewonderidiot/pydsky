from qtpy.QtWidgets import QPushButton
from qtpy.QtCore import Qt

class Button(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)

    def press(self):
        self.setDown(True)
        self.pressed.emit()

    def release(self):
        self.setDown(False)
        self.released.emit()
