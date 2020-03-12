from PyQt5 import QtWidgets


def create_fields(widget):

    for label in widget.labels:
        field = QtWidgets.QLineEdit()
        widget.ui.formLayout.addRow(
            QtWidgets.QLabel(label), field)
        widget.fields.append(field)


def fill_selected(widget, data):

    for field, text in zip(widget.fields, data):
        field.setText(text)


def extract_as_dicts(widget):

    prim_data = {}
    comm_data = {}
    primaries = widget.parent().table_model.get_primaries()

    for label, field in zip(widget.labels, widget.fields):
        if label in primaries:
            prim_data[label] = field.text()
        else:
            comm_data[label] = field.text()

    print(prim_data, comm_data)
    data = [prim_data, comm_data]

    return data
