#!/usr/bin/env python3
# -*- coding: utf-8 -*-



from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
import time

import sys
import os

import qtSqlTry
from DB_manager import tableModelQtsqlTry
from DBessai import *



#To incorporate UI_view_SARAA inherit QDialog, and UI_view
class MainDialog(QDialog, qtSqlTry.Ui_Form):

    def __init__(self,parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.LaBase = LaBase()

        self.model = QSqlTableModel()
        self.model.setTable("Contact")
        self.model.select()
        self.model.setHeaderData(1, Qt.Horizontal, u"pilot_1")
        self.model.setHeaderData(2, Qt.Horizontal, "datetime1")
        self.model.setHeaderData(3, Qt.Horizontal, "datetime2")

        self.tableView1.setModel(self.model)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.lineEditPilote.text()











if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        form = MainDialog()
        #LaBase()
        form.show()
        app.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error: ", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window....")
    except Exception:
        print(sys.exc_info()[1])


