# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'starter.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, welcome):
        welcome.setObjectName("welcome")
        welcome.resize(383, 200)
        self.centralwidget = QtWidgets.QWidget(welcome)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 381, 201))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create_table_button = QtWidgets.QPushButton(
            self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.create_table_button.sizePolicy().hasHeightForWidth())
        self.create_table_button.setSizePolicy(sizePolicy)
        self.create_table_button.setObjectName("create_table_button")
        self.horizontalLayout.addWidget(self.create_table_button)
        self.load_table_button = QtWidgets.QPushButton(
            self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.load_table_button.sizePolicy().hasHeightForWidth())
        self.load_table_button.setSizePolicy(sizePolicy)
        self.load_table_button.setObjectName("load_table_button")
        self.horizontalLayout.addWidget(self.load_table_button)
        welcome.setCentralWidget(self.centralwidget)

        self.retranslateUi(welcome)
        QtCore.QMetaObject.connectSlotsByName(welcome)

    def retranslateUi(self, welcome):
        _translate = QtCore.QCoreApplication.translate
        welcome.setWindowTitle(_translate("welcome", "Welcome"))
        self.create_table_button.setText(_translate("welcome", "Create"))
        self.load_table_button.setText(_translate("welcome", "Load"))
