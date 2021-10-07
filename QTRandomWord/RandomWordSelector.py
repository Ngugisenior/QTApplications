# This Python file uses the following encoding: utf-8
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class RandomWordSelector(QtWidgets.QtWidget):
    def __init__(self):
        super().__init__()

        self.hello = ['hello', 'sasa', 'wimwega', 'uhoro']

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    widget = RandomWordSelector()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
