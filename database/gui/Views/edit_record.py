from PyQt5 import QtWidgets, QtCore

from database.gui.ui.record_dialog import Ui_Dialog
from database.gui.Controllers import record_dialog_controller


class EditRecordDialog(QtWidgets.QDialog):
    def __init__(self, headers, filepath, parent=None):
        super(EditRecordDialog, self).__init__(parent)

        self.filepath = filepath

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.labels = headers
        self.fields = []

        self.current = self.parent().get_current()
        data = self.parent().table_model._table.find_record(
            self.labels[0], self.current)[1]

        record_dialog_controller.create_fields(self)
        record_dialog_controller.fill_selected(self, data)

        self.default_data = record_dialog_controller.extract_as_dicts(self)

    def accept(self):

        data = record_dialog_controller.extract_as_dicts(self)

        response = self.parent().table_model.edit_record(
            self.current, self.default_data, data)

        if response == 'ok':
            super().accept()

        else:
            QtWidgets.QMessageBox.about(self, "Error", response)
