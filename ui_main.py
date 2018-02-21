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







        # #Création de la basse de données
        # self.db = QSqlDatabase.addDatabase("QSQLITE") ## Nous indiquons ici le driver avec lequel nous souhaitons travailler.
        # ## Les driver permettent de définir avec quel type de bases de données nous allons travailler.
        # ## Notez qu'il en existe un grand nombre et qu'il vous est même possible d'en personnaliser. Mais ceci sort du contexte actuel.
        # self.db.setDatabaseName('myBdd') ## Nous nommons ici notre base de données.
        # self.db.open() ## Commande permettant d'accéder à la base de données
        #
        # query = QSqlQuery()
        # query.exec_('''create table Contact (id INTEGER PRIMARY KEY,nom TEXT, prenom TEXT)''')
        # ## Création de la table Contact dans notre base de données ouverte.
        # self.db.commit() ## Enregistrement de la base de données
        # self.db.close() ## Fermeture de celle-ci


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


