# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'database/gui/ui/XML/search.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_search(object):
    def setupUi(self, search):
        search.setObjectName("search")
        search.resize(380, 210)
        self.buttonBox = QtWidgets.QDialogButtonBox(search)
        self.buttonBox.setGeometry(QtCore.QRect(20, 150, 340, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.field_label = QtWidgets.QLabel(search)
        self.field_label.setGeometry(QtCore.QRect(20, 50, 70, 30))
        self.field_label.setObjectName("field_label")
        self.value_label = QtWidgets.QLabel(search)
        self.value_label.setGeometry(QtCore.QRect(20, 100, 70, 30))
        self.value_label.setObjectName("value_label")
        self.field_box = QtWidgets.QComboBox(search)
        self.field_box.setGeometry(QtCore.QRect(100, 50, 240, 30))
        self.field_box.setObjectName("field_box")
        self.value_edit = QtWidgets.QLineEdit(search)
        self.value_edit.setGeometry(QtCore.QRect(100, 100, 240, 30))
        self.value_edit.setObjectName("value_edit")

        self.retranslateUi(search)
        self.buttonBox.accepted.connect(search.accept)
        self.buttonBox.rejected.connect(search.reject)
        QtCore.QMetaObject.connectSlotsByName(search)

    def retranslateUi(self, search):
        _translate = QtCore.QCoreApplication.translate
        search.setWindowTitle(_translate("search", "Search"))
        self.field_label.setText(_translate("search", "Field"))
        self.value_label.setText(_translate("search", "Value"))
