from PyQt5 import QtWidgets, QtCore

from database.gui.ui.starter import Ui_MainWindow
from database.gui.Views.create_table import CreateTableDialog
from database.gui.Views.main_window import MainWindow
from database.gui.Controllers.load_table_controller import load


class WelcomeWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.create_table_button.clicked.connect(
            self.create_table_dialog_show)

        self.ui.load_table_button.clicked.connect(self.load_table_dialog_show)

        self.filepath = None

    def create_table_dialog_show(self):

        self.hide()

        create_table_dialog = CreateTableDialog(self)
        create_table_dialog.exec_()

        self.check_filepath()

    def load_table_dialog_show(self):

        self.hide()

        load(self)

        self.check_filepath()

    def init_db(self):

        self.db_window = MainWindow(self.filepath)
        self.db_window.show()

    def check_filepath(self):
        if self.filepath:
            self.init_db()
        else:
            self.show()
