# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtSqlTry.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(830, 462)
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
        self.tableView1.setGeometry(QtCore.QRect(30, 130, 711, 192))
        self.tableView1.setSortingEnabled(True)
        self.tableView1.setObjectName("tableView1")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 340, 392, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.Calcul = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Calcul.setObjectName("Calcul")
        self.horizontalLayout_2.addWidget(self.Calcul)
        self.pushButton_effacer = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_effacer.setToolTip("")
        self.pushButton_effacer.setWhatsThis("")
        self.pushButton_effacer.setObjectName("pushButton_effacer")
        self.horizontalLayout_2.addWidget(self.pushButton_effacer)
        self.calule_temps = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.calule_temps.setToolTip("")
        self.calule_temps.setObjectName("calule_temps")
        self.horizontalLayout_2.addWidget(self.calule_temps)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.Calcul.setText(_translate("Form", "Calcul"))
        self.pushButton_effacer.setText(_translate("Form", "Effacer"))
        self.calule_temps.setText(_translate("Form", "calculTemps"))
