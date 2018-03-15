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
        # appel de la classe du module dbessai
        self.LaBase = LaBase()

        self.model = QSqlTableModel()
        self.model.setTable("Contact1")
        self.model.select()
        self.model.setHeaderData(1, Qt.Horizontal, u"pilot_1")
        self.model.setHeaderData(2, Qt.Horizontal, "datetime1")
        self.model.setHeaderData(3, Qt.Horizontal, "datetime2")
        self.tableView1.setModel(self.model)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.insertion()
        # self.pushButton.clicked.connect(self.insertion)
        self.pushButton.clicked.connect(self.affiche)

    def insertion(self):
        self.LaBase.db.open()
        liste = [self.lineEditPilote.text(), self.dateTimeEdit_1.dateTime(), self.dateTimeEdit_2.dateTime()]
        self.model.setTable("Contact1")
        # self.model.select()
        # On insère une ligne supplémentaire qui sera remplie par la suite.
        # Si cette ligne de code est oubliée, c'est une modification qui sera effectuée
        self.model.insertRows(0, 1)
        # Nous créons une boucle permettant de rentrer les valeurs des QLineEdit dans notre base de données
        a = 0
        while a <= 2:
            ## setData() requiert en premier argument l'index de la ligne à créer, en deuxième la valeur.
            ## Ici dans le premier argument a+1 correspond à la deuxième colonne de notre table si a = 0.
            # On laisse la première colonne se remplir seule (clé automatique).
            ## Le premier argument de self.model.index peut prendre n'importe quelle valeur. Ceci ne change rien.
            self.model.setData(self.model.index(0, a + 1), liste[a])
            a += 1

        self.model.submitAll()
        self.LaBase.db.close()

    def Lecture(self):
        liste = []
        self.LaBase.db.open()
        self.model.setTable("Contact1")
        self.model.select()
        nb_row = self.model.rowCount()
        a = 0
        while a < nb_row:
            record = self.model.record(a)
            contact = [record.value("pilot_1"), record.value("datetime1"), record.value("datetime2")]
            liste.append(contact)
            a += 1
        self.LaBase.db.close()
        return liste

    def affiche(self):
        la_liste = self.Lecture()
        print(la_liste)

    def effacer(self):
        pass

    def calcultemps(self):
        le_resultat = self.Lecture()
        le_resultat[2]
        print(le_resultat)

    def Lire(self):
        self.LaBase.db.open()
        query = self.LaBase.db.exec_("""select * from Contact1""")
        while query.next():
            value = []
            record = query.record()
            for index in range(record.count()):
                value.append(str(record.value(index)))
            #return (';'.join(value))
            print(';'.join(value))
        self.LaBase.db.close()

    @pyqtSlot()
    def on_Calcul_clicked(self):
        print(self.Lire())
        #print(labasevar(self))









        # self.db.close()

        # @pyqtSlot()
        # def on_pushButton_clicked(self):
        #     self.insertion


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


