# This Python file uses the following encoding: utf-8
import sys
import random
from PySide6 import QtWidgets, QtCore


class RandomWord(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        # Innitializing a button
        self.button = QtWidgets.QPushButton("Click me!")
        # Innitializing a Label
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        # Create a box layout to hold the button and text
        self.layout = QtWidgets.QVBoxLayout(self)
        # Add text to the box layout
        self.layout.addWidget(self.text)
        # Add button to the box layout
        self.layout.addWidget(self.button)
        # method to call on button click has been clicked
        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":

    # It handles widget specific initialization, finalization.
    app = QtWidgets.QApplication([])

    widget = RandomWord()

    widget.resize(800, 800)
    widget.show()

    sys.exit(app.exec_())
