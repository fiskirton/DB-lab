from PyQt5 import QtWidgets


def create_items(widget):

    for label in widget.labels:
        widget.ui.field_box.addItem(label)


def extract(widget):

    key, value = widget.ui.field_box.currentText(), widget.ui.value_edit.text()

    return key, value
