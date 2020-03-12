from PyQt5 import QtCore, QtWidgets

from database.environments import DATA_PATH

from db import Table

import pickle


def add_edit_field(layout):
    field = QtWidgets.QLineEdit()
    layout.addWidget(field)

    return field


def save(widget):

    primaries_text = [field.text() for field in widget.primaries]
    commons_text = [field.text() for field in widget.commons]

    filename, ok = QtWidgets.QFileDialog.getSaveFileName(widget, 'Create DB',
                                                         DATA_PATH, 'DB Files (*.db)')

    if ok:

        filepath = filename + '.db'

        table = Table(primaries_text, commons_text)

        with open(filepath, 'wb') as new_file:
            pickle.dump(table, new_file)

        widget.parent().filepath = filepath
