from PyQt5 import QtCore, QtWidgets

from database.environments import DATA_PATH


def load(widget):

    filepath = QtWidgets.QFileDialog.getOpenFileName(
        widget, 'Load table', DATA_PATH, "DB Files (*.db)")[0]

    if filepath:
        widget.filepath = filepath
