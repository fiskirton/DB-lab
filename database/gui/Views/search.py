from PyQt5 import QtWidgets, QtCore

from database.gui.ui.search import Ui_search
from database.gui.Controllers import search_controller


class SearchDialog(QtWidgets.QDialog):
    def __init__(self, headers, parent=None):
        super(SearchDialog, self).__init__(parent)

        self.ui = Ui_search()
        self.ui.setupUi(self)

        self.labels = headers

        search_controller.create_items(self)

    def accept(self):

        key, value = search_controller.extract(self)

        self.parent().table_model.add_search_data(key, value)

        self.clear()
        super().accept()

    def reject(self):
        self.clear()
        super().reject()

    def clear(self):

        self.ui.field_box.setCurrentIndex(0)
        self.ui.value_edit.setText('')
