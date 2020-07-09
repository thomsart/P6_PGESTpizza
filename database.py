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
        'database_structure.sql' """

        with open('database_structure.sql', 'r') as sql:
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

    def add_pizzeria(self):

        return

    def show_pizzeria(self):

        return

    def add_product(self):

        return
    
    def show_products(self):

        return

    def add_pizza_n_recepy(self):

        return
    
    def show_recepy(self):

        return

    def add_employe(self):

        return

    def show_employe(self):

        return

    def add_client(self):

        return
    
    def show_client(self):

        return

    def order_menu(self):

        return

    def show_menu(self):

        return


#############################################################################
