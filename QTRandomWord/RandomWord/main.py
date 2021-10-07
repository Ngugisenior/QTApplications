# This Python file uses the following encoding: utf-8
import sys
import random
from PySide6 import QtWidgets, QtCore


class RandomWord(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

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

    # It handles widget specific initialization, finalization.
    app = QtWidgets.QApplication([])
    widget = RandomWord()

    widget.resize(800, 800)
    widget.show()

    sys.exit(app.exec_())
