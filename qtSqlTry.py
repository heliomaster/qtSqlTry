# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtSqlTry.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 373)
        self.lineEditPilote = QtWidgets.QLineEdit(Form)
        self.lineEditPilote.setGeometry(QtCore.QRect(20, 20, 113, 21))
        self.lineEditPilote.setObjectName("lineEditPilote")
        self.dateTimeEdit_1 = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit_1.setGeometry(QtCore.QRect(20, 60, 194, 24))
        self.dateTimeEdit_1.setTimeSpec(QtCore.Qt.UTC)
        self.dateTimeEdit_1.setObjectName("dateTimeEdit_1")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(20, 100, 194, 24))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.tableView1 = QtWidgets.QTableView(Form)
        self.tableView1.setGeometry(QtCore.QRect(20, 130, 371, 192))
        self.tableView1.setObjectName("tableView1")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 330, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.Calcul = QtWidgets.QPushButton(Form)
        self.Calcul.setGeometry(QtCore.QRect(160, 330, 110, 32))
        self.Calcul.setObjectName("Calcul")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.Calcul.setText(_translate("Form", "Calcul"))
