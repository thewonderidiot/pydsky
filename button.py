from PySide2.QtWidgets import QPushButton
from PySide2.QtCore import Qt

class Button(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)

    def press(self):
        self.setDown(True)
        self.pressed.emit()

    def release(self):
        self.setDown(False)
        self.released.emit()
