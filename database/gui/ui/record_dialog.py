# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_record_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, new_record):
        new_record.setObjectName("new_record")
        new_record.resize(534, 367)
        new_record.setSizeGripEnabled(False)

        self.buttonBox = QtWidgets.QDialogButtonBox(new_record)
        self.buttonBox.setGeometry(QtCore.QRect(20, 330, 491, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.groupBox = QtWidgets.QGroupBox(new_record)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 501, 311))
        self.groupBox.setObjectName("groupBox")

        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 29, 481, 271))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.retranslateUi(new_record)
        self.buttonBox.accepted.connect(new_record.accept)
        self.buttonBox.rejected.connect(new_record.reject)
        QtCore.QMetaObject.connectSlotsByName(new_record)

    def retranslateUi(self, new_record):
        _translate = QtCore.QCoreApplication.translate
        new_record.setWindowTitle(_translate("new_record", "New record"))
        self.groupBox.setTitle(_translate("new_record", "Add new record"))
