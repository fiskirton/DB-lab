from PyQt5 import QtWidgets
from database.gui.Views import welcome
import sys


def main():

    app = QtWidgets.QApplication([])
    application = welcome.WelcomeWindow()
    application.show()

    sys.exit(app.exec_())


main()
