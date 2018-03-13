#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# !/usr/bin/env python3
# -*- coding: utf-8 -*-



from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
import time

import sys
import os

import qtSqlTry
from Tpaine_manager import *


# To incorporate UI_view_SARAA inherit QDialog, and UI_view
class MainDialog(QDialog, qtSqlTry.Ui_Form):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)


class TpainClassManager(QWidget, DatabaseUtility, qtSqlTry.Ui_Form):
    def __init__(self, database, tablename):
        super().__init__(database, tablename)
        self.dbu = DatabaseUtility(database, tablename)
        self.model = QSqlTableModel()
        self.model.setTable("test1")
        self.UpdateTree()
        self.model.select()
        self.model.setHeaderData(1, Qt.Horizontal, u"pilot_1")
        self.model.setHeaderData(2, Qt.Horizontal, "datetime1")
        self.model.setHeaderData(3, Qt.Horizontal, "datetime2")
        self.tableView1.setModel(self.model)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        text = self.lineEditPilote.text()
        self.dbu.add_entry_to_table(text)
        self.UpdateTree()

    def UpdateTree(self):
        pass










        # col = self.dbu.get_columns()
        # table = self.dbu.get_columns()

        # for c in range(len(col)):
        #     self.treeWidget.headerItem().setText(c, col[c][0])
        #
        # self.treeWidget.clear()
        #
        # for item in range(len(table)):
        #     QTreeWidgetItem(self.treeWidget)
        #     for value in range(len(table[item])):
        #         self.treeWidget.topLevelItem(item).setText(value, str(table[item][value]))










        # @pyqtSlot()
        # def on_pushButton_clicked(self):
        #     self.insertion


if __name__ == '__main__':

    db = 'essai_tp_appel_classe'
    tablename = 'test2'
    try:
        app = QApplication(sys.argv)
        form = MainDialog()
        # LaBase()
        form.show()
        app.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error: ", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window....")
    except Exception:
        print(sys.exc_info()[1])
