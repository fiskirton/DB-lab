from PyQt5 import QtWidgets, QtCore

from database.gui.Models.table_model import TableModel
from database.gui.Views.new_record import NewRecordDialog
from database.gui.Views.edit_record import EditRecordDialog
from database.gui.Views.search import SearchDialog
from database.gui.ui.main_window_ui import Ui_MainWindow
from database.Helpers.export import save_xlsx
from database.environments import DATA_PATH


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, filepath):
        super().__init__()

        self.filepath = filepath

        self.table_model = TableModel(filepath)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.table_view = self.ui.tableView
        self.table_view.setModel(self.table_model)

        self.new_record_dialog = NewRecordDialog(
            self.table_model.get_headers(), self.filepath, self)

        self.search_dialog = SearchDialog(self.table_model.get_headers(), self)

        self.ui.new_record_button.clicked.connect(self.new_record_dialog_show)
        self.ui.search_button.clicked.connect(self.search_dialog_show)
        self.ui.refresh_button.clicked.connect(self.refresh_data)
        self.ui.backup_button.clicked.connect(self.make_backup)
        self.ui.export_button.clicked.connect(self.export)

        self.table_view.keyPressEvent = self.keyPressEvent

    def new_record_dialog_show(self):
        self.new_record_dialog.show()

    def search_dialog_show(self):
        self.search_dialog.show()

    def refresh_data(self):
        self.table_model.reset()

    def make_backup(self):
        filepath, ok = QtWidgets.QFileDialog.getSaveFileName(
            self, "Make Backup", "DB Files (*.db)")
        if ok:
            TableModel.save_obj(filepath + '.db', self.table_model._table)

    def export(self):
        print(self.table_model.get_dv())
        filepath, ok = QtWidgets.QFileDialog.getSaveFileName(
            self, "Export", DATA_PATH, "Spreadsheets (*.xls *.xlsx)")
        if ok:
            save_xlsx(filepath, self.table_model.get_headers(),
                      self.table_model.get_dv())

    def keyPressEvent(self, e):

        if e.key() == QtCore.Qt.Key_D:
            self.table_model.delete_record(self.get_current())

        elif e.key() == QtCore.Qt.Key_E:
            if self.table_model._data_view:
                edit_record_dialog = EditRecordDialog(
                    self.table_model.get_headers(), self.filepath, self)
                edit_record_dialog.show()

    def get_current(self):
        selected_row_index = self.table_view.currentIndex()
        selcted_cell = self.table_view.model().data(
            self.table_view.model().index(selected_row_index.row(), 0))

        return selcted_cell
