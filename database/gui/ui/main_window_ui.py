# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, database):

        # set main windows
        database.setObjectName("database")
        database.resize(860, 415)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            database.sizePolicy().hasHeightForWidth())
        database.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Droid Sans Mono for Powerline")
        font.setBold(True)
        font.setWeight(75)
        database.setFont(font)

        # set central widget
        # all other widgets will be placed here
        self.centralwidget = QtWidgets.QWidget(database)
        self.centralwidget.setObjectName("centralwidget")

        # set table view
        # main information will be placed here
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 675, 345))
        self.tableView.horizontalHeader().setDefaultSectionSize(675 / 4)
        self.tableView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableView.setEditTriggers(
            QtWidgets.QAbstractItemView.EditKeyPressed | QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableView.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        # self.header = QtWidgets.QHeaderView(
        #    QtCore.Qt.Horizontal, self.tableView)
        # self.tableView.setHorizontalHeader(self.header)
        # self.header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # set content spliters
        self.line_vertical = QtWidgets.QFrame(self.centralwidget)
        self.line_vertical.setGeometry(QtCore.QRect(685, 0, 20, 415))
        self.line_vertical.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_vertical.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_vertical.setObjectName("vertical split")

        self.line_horizontal = QtWidgets.QFrame(self.centralwidget)
        self.line_horizontal.setGeometry(QtCore.QRect(0, 355, 695, 20))
        self.line_horizontal.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_horizontal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_horizontal.setObjectName("horizontal split")

        # set horizontal layout for tip lables
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 370, 685, 40))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # set tip lables
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        # set vertical layout for option buttons
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(705, 10, 145, 170))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")

        # set option buttons
        self.new_record_button = QtWidgets.QPushButton(
            self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(
            self.new_record_button.sizePolicy().hasHeightForWidth())
        self.new_record_button.setSizePolicy(sizePolicy)
        self.new_record_button.setFont(font)
        self.new_record_button.setAutoFillBackground(False)
        self.new_record_button.setFlat(False)
        self.new_record_button.setObjectName("new_record_button")
        self.verticalLayout.addWidget(self.new_record_button)

        self.search_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(
            self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy)
        self.search_button.setDefault(False)
        self.search_button.setFlat(False)
        self.search_button.setObjectName("search_button")
        self.verticalLayout.addWidget(self.search_button)

        self.backup_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(
            self.backup_button.sizePolicy().hasHeightForWidth())
        self.backup_button.setSizePolicy(sizePolicy)
        self.backup_button.setDefault(False)
        self.backup_button.setFlat(False)
        self.backup_button.setObjectName("backup_button")
        self.verticalLayout.addWidget(self.backup_button)

        self.export_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(
            self.export_button.sizePolicy().hasHeightForWidth())
        self.export_button.setSizePolicy(sizePolicy)
        self.export_button.setDefault(False)
        self.export_button.setFlat(False)
        self.export_button.setObjectName("export_button")
        self.verticalLayout.addWidget(self.export_button)

        self.refresh_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(
            self.refresh_button.sizePolicy().hasHeightForWidth())
        self.refresh_button.setSizePolicy(sizePolicy)
        self.refresh_button.setDefault(False)
        self.refresh_button.setFlat(False)
        self.refresh_button.setObjectName("refresh_button")
        self.verticalLayout.addWidget(self.refresh_button)

        # place central widger with all nested widgets in main window
        database.setCentralWidget(self.centralwidget)

        self.retranslateUi(database)
        QtCore.QMetaObject.connectSlotsByName(database)

    def retranslateUi(self, database):
        _translate = QtCore.QCoreApplication.translate
        database.setWindowTitle(_translate("database", "Database"))
        self.label.setText(_translate(
            "database", "d - Delete selected record"))
        self.label_2.setText(_translate(
            "database", "e - Edit selected record"))
        self.new_record_button.setText(_translate("database", "New record"))
        self.search_button.setText(_translate("database", "Search"))
        self.backup_button.setText(_translate("database", "Make backup"))
        self.export_button.setText(_translate("database", "Export"))
        self.refresh_button.setText(_translate("database", "Refresh"))
