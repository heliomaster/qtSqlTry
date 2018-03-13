#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from datetime import datetime


class DatabaseUtility:
    def __init__(self, database, tablename):
        self.db = database
        self.tablename = tablename

        self.cnx = sqlite3.connect(self.db)

        self.cursor = self.cnx.cursor()

        # self.connect_to_database()
        self.create_table()

    # def connect_to_database(self):
    #     #TODO: try/except with error
    #     self.c = self.db

    def create_table(self):
        cmd = (
            "CREATE TABLE " + self.tablename + "( id INTEGER PRIMARY KEY,pilot_name TEXT,date_time1 TEXT,date_time2 TEXT)")
        self.run_command(cmd)

    def get_table(self):
        self.create_table()
        return self.run_command("SELECT * FROM {}".format(self.tablename))

    def get_columns(self):
        self.run_command("SELECT * FROM {}".format(self.tablename))
        return [i[0] for i in self.cursor.description]

    def run_command(self, cmd):
        try:
            self.cursor.execute(cmd)
        except sqlite3.Error as e:
            print("could not execute{}".format(e))
        try:
            msg = self.cursor.fetchall()
        except:
            msg = self.cursor.fetchone()
        return msg

    def add_entry_to_table(self, message):
        date_time1 = datetime.strftime("%d-%m-%y %H:%M")

        cmd = "INSERT INTO" + self.tablename + "(date_time1,message)"
        cmd += " VALUES ('%s','%s')" % (date_time1, message)
        self.run_command(cmd)

    def __del__(self):
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()


if __name__ == '__main__':
    db = 'essai_tp'
    tablename = 'test1'

    dbu = DatabaseUtility(db, tablename)
