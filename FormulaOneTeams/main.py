# This Python file uses the following encoding: utf-8
import sys
from PySide6 import QtWidgets, QtCore


class FormulaOne(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.teams = [
            'McLaren Formula One',
            'RedBull Racing Formula One',
            'Mercedes Petronas Formula one Team',
            'Scuderia AlphaTauri Racing',
            'Scuderia Ferrari Racing Team',
            'Alpine Renault Formula One Team',
            'Williams Racing',
            'Alpha Romeo Racing',
            'Haas Formula One Team',
            'Aston Martin Formula One team'
        ]

        self.initialize_box()
        self.create_labels_list()
        x = self.initialize_buttons('Add Team')
        self.set_onclick_action(x, self.add_team)

    """ Create button Layouts """
    @QtCore.Slot()
    def initialize_buttons(self, action):
        self.button = QtWidgets.QPushButton(action)
        self.box.addWidget(self.button)
        return self.button

    """ On Button Click Method """
    @QtCore.Slot()
    def set_onclick_action(self, item, method):
        item.clicked.connect(method)

    """ Innitialize box Layout """
    @QtCore.Slot()
    def initialize_box(self):
        self.box = QtWidgets.QVBoxLayout(self)

    """ Create Labels """
    @QtCore.Slot()
    def create_labels_list(self):
        for i in self.teams:
            self.label = QtWidgets.QLabel(i, alignment=QtCore.Qt.AlignCenter)
            self.box.addWidget(self.label)

    @QtCore.Slot()
    def create_text_boxes(self, message):
        self.text_box = QtWidgets.QLineEdit(message)
        return self.text_box

    """ Add Team Function """
    @QtCore.Slot()
    def add_team(self):
        self.create_text_boxes('Enter')
        self.box.addWidget(self.text_box)
        self.save_button = QtWidgets.QPushButton('Save')
        self.box.addWidget(self.save_button)
        self.save_button.clicked.connect(self.save)

    @QtCore.Slot()
    def save(self):
        sender = self.text_box.text()
        self.teams.append(sender)
        self.box.insertWidget(len(self.teams), QtWidgets.QLabel(sender, alignment=QtCore.Qt.AlignCenter))

    @QtCore.Slot()
    def clearLayout(self):
        while self.box.count():
            child = self.box.takeAt(0)
            if child.widget():
                child.widget().deleteLater()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    my_widget = FormulaOne()

    my_widget.resize(800, 700)

    my_widget.show()

    sys.exit(app.exec_())
