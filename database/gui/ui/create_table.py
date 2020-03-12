# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_table.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, create_table):
        create_table.setObjectName("create_table")
        create_table.resize(733, 453)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            create_table.sizePolicy().hasHeightForWidth())
        create_table.setSizePolicy(sizePolicy)
        create_table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.primary_layout_widget = QtWidgets.QWidget(create_table)
        self.primary_layout_widget.setGeometry(QtCore.QRect(10, 60, 351, 301))
        self.primary_layout_widget.setObjectName("primary_layout_widget")
        self.primary_layout = QtWidgets.QVBoxLayout(self.primary_layout_widget)
        self.primary_layout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.primary_layout.setContentsMargins(0, 0, 0, 0)
        self.primary_layout.setObjectName("primary_layout")
        self.common_layout_widget = QtWidgets.QWidget(create_table)
        self.common_layout_widget.setGeometry(
            QtCore.QRect(370, 60, 351, 301))
        self.common_layout_widget.setObjectName("common_layout_widget")
        self.common_layout = QtWidgets.QVBoxLayout(
            self.common_layout_widget)
        self.common_layout.setContentsMargins(0, 0, 0, 0)
        self.common_layout.setObjectName("common_layout")
        self.buttonBox = QtWidgets.QDialogButtonBox(create_table)
        self.buttonBox.setGeometry(QtCore.QRect(10, 420, 711, 27))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.primary_fields = QtWidgets.QLabel(create_table)
        self.primary_fields.setGeometry(QtCore.QRect(10, 20, 350, 40))
        self.primary_fields.setAlignment(QtCore.Qt.AlignCenter)
        self.primary_fields.setObjectName("primary_fields")
        self.common_fields = QtWidgets.QLabel(create_table)
        self.common_fields.setGeometry(QtCore.QRect(370, 20, 350, 40))
        self.common_fields.setAlignment(QtCore.Qt.AlignCenter)
        self.common_fields.setObjectName("common_fields")
        self.new_primary_field = QtWidgets.QPushButton(create_table)
        self.new_primary_field.setGeometry(QtCore.QRect(10, 370, 351, 27))
        self.new_primary_field.setObjectName("new_primary_field")
        self.new_common_field = QtWidgets.QPushButton(create_table)
        self.new_common_field.setGeometry(QtCore.QRect(370, 370, 351, 27))
        self.new_common_field.setObjectName("new_common_field")

        self.retranslateUi(create_table)
        self.buttonBox.accepted.connect(create_table.accept)
        self.buttonBox.rejected.connect(create_table.reject)
        QtCore.QMetaObject.connectSlotsByName(create_table)

    def retranslateUi(self, create_table):
        _translate = QtCore.QCoreApplication.translate
        create_table.setWindowTitle(_translate("create_table", "Create table"))
        self.primary_fields.setText(_translate("create_table", "Primaries"))
        self.common_fields.setText(_translate("create_table", "Commons"))
        self.new_primary_field.setText(
            _translate("create_table", "New primary field"))
        self.new_common_field.setText(
            _translate("create_table", "New common field"))
