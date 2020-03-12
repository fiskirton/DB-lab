from PyQt5 import QtWidgets, QtCore

from database.gui.ui.record_dialog import Ui_Dialog
from database.gui.Controllers import record_dialog_controller


class NewRecordDialog(QtWidgets.QDialog):
    def __init__(self, headers, filepath, parent=None):
        super(NewRecordDialog, self).__init__(parent)

        self.filepath = filepath

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.labels = headers
        self.fields = []

        record_dialog_controller.create_fields(self)

    def accept(self):

        data = record_dialog_controller.extract_as_dicts(self)

        response = self.parent().table_model.add_record(data)

        if response == 'ok':

            self.clear()
            super().accept()
        else:
            QtWidgets.QMessageBox.about(self, "Error", response)

    def reject(self):

        self.clear()

        super().reject()

    def clear(self):

        for field in self.fields:
            field.setText('')
