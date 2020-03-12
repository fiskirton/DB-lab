from PyQt5 import QtWidgets, QtCore

from database.gui.ui.create_table import Ui_Dialog
from database.gui.Controllers import create_table_controller


class CreateTableDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CreateTableDialog, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.primaries, self.commons = [], []

        self.primaries.append(
            create_table_controller.add_edit_field(self.ui.primary_layout))

        self.ui.new_primary_field.clicked.connect(self.add_primary_field)
        self.ui.new_common_field.clicked.connect(self.add_common_field)

    def add_primary_field(self):
        field = create_table_controller.add_edit_field(self.ui.primary_layout)
        self.primaries.append(field)

    def add_common_field(self):
        field = create_table_controller.add_edit_field(self.ui.common_layout)
        self.commons.append(field)

    def accept(self):

        create_table_controller.save(self)

        super().accept()

    def reject(self):

        super().reject()
