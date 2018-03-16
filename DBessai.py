#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtSql import *
from ui_main import MainDialog
from qtSqlTry import Ui_Form


class LaBase():
    def __init__(self):
        #super(LaBase,self).__init__()
        #Création de la basse de données
        self.db = QSqlDatabase.addDatabase("QSQLITE") ## Nous indiquons ici le driver avec lequel nous souhaitons travailler.
        ## Les driver permettent de définir avec quel type de bases de données nous allons travailler.
        ## Notez qu'il en existe un grand nombre et qu'il vous est même possible d'en personnaliser. Mais ceci sort du contexte actuel.
        self.db.setDatabaseName('pilote1')  ## Nous nommons ici notre base de données.

        self.db.open() ## Commande permettant d'accéder à la base de données

        query = QSqlQuery()
        query.exec_('''create table Contact (id INTEGER PRIMARY KEY,pilot_1 TEXT, datetime1 TEXT, datetime2 TEXT)''')
        query.exec_('''create table Contact1 (id INTEGER PRIMARY KEY,pilot_1 TEXT, datetime1 TEXT, datetime2 TEXT)''')
        ## Création de la table Contact dans notre base de données ouverte.
        self.db.commit() ## Enregistrement de la base de données
        self.db.close() ## Fermeture de celle-ci

    def Lire(self):
        index = 0
        query = QSqlQuery()
        query.exec_("select * FROM Contact")
        while query.next():
            ids = query.value(0)
            pil1 = query.value(1)
            pil2 = query.value(2)
        print(ids, pil1, pil2)


if __name__ == '__main__':
    LaBase()
