#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector as mc


###############################################################################

""" We create the class Database for more flexibity. Thanks to that we are less
independant from MySQL 8.0 """

###############################################################################


class Database():

    def __init__(self, db, user, pwd):
        self.host = "localhost"
        self.user = user
        self.password = pwd
        self.database = db
        self.connect = mc.connect(
            host=self.host, user=self.user, password=self.password,
            database=self.database)
        self.cursor = self.connect.cursor()

    def disconnect(self):
        self.connect.commit()
        self.connect.close()

    def create_the_database(self):

        """ We create the database in this methode thanks to the file
        'script_database_aliment.sql' """

        with open('script_database_aliment.sql', 'r') as sql:
            block = ""
            for line in sql:
                if line[0] == "\n":
                    continue
                elif line[0] == "-":
                    continue
                else:
                    if ";" in line:
                        block = block+line
                        self.cursor.execute(block)
                        block = ""

                    else:
                        block = block+line

        return

    def fill_tables(self):

        self.cursor.execute("""INSERT INTO category (name) VALUE('"""
                            + str(food) + """') """)

        self.cursor.execute("""SELECT id FROM category WHERE name = '"""
                            + str(food) + """' """)

        return

    def show_saved_food(self):

        """ This methode show all the substitutes saved by the client. """

        self.cursor.execute("""SELECT category, nutriscore, name, brand, store,
            quantity, url FROM save_food""")

        rows = self.cursor.fetchall()
        for value in rows:
            print("\n[{0} de nutriscore:'{1}', de nom:{2}, et de marque:{3}."
                  "\nMagasin:{4}, {5}, {6}]\n".format(value[0], value[1],
                   value[2], value[3], value[4], value[5], value[6]))

        return

###############################################################################
