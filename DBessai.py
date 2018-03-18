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

        # def lire(self):
        #     self.db.open()
        #     query = self.db.exec_("""select * from Contact""")
        #     while query.next():
        #         value = []
        #         record = query.record()
        #         for index in range(record.count()):
        #             value.append(str(record.value(index)))
        #         print(';'.join(value))













if __name__ == '__main__':
    LaBase()
