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

    def fill_tables(self, food, nb_pages):

        """ We take from Openfoodfact Api the 'food' we want and put it in a
        list of values in order to fill the table made for it in our database.
        For that we create a for loop in fonction of the number of pages
        'nb_page' of the product on the Api, and we put all datas in the table
        we want with the argument 'table'.It's allows us to not repet for
        exemple 20 times the same request. """

        self.cursor.execute("""INSERT INTO category (name) VALUE('"""
                            + str(food) + """') """)

        self.cursor.execute("""SELECT id FROM category WHERE name = '"""
                            + str(food) + """' """)

        id_cat = self.cursor.fetchone()[0]

        for i in range(nb_pages):

            """ We choose the food we want to put in the database by the argument
            'food' and the number of pages we want with 'nb_pages'. Be carefull
            to not take more than there are pages on the Api. """

            url = 'https://fr-en.openfoodfacts.org/category/' + str(food) + '/'
            + str(i) + '.json'
            response = requests.get(url)
            data = response.json()
            key = data.get("products")
            number_of_product = len(key)
            count = 0

            """ Now we do a while loop to browse and catch all the vallues which
            we need for our table. """

            while count < number_of_product:

                try:
                    product = key[count]
                    name = product['product_name']
                    brand = product['brands']
                    store = product['stores']
                    country = product['countries']
                    quantity = product['quantity']
                    nutriscore = product['nutriscore_grade']
                    url = product['url']
                    category = str(food)
                    product_list = [name, brand, store, country, quantity,
                                    nutriscore, url, category]
                    print(product_list)

                    """ We choose to not take product which don't have the
                    headers that we need. """

                except KeyError:
                    count += 1
                    continue

                count += 1

                """ Now the idea is to put the product_list into the table we
                choose. """

                self.cursor.execute("""INSERT INTO product(name, brand, store,
                    country, quantity,nutriscore, url, category)
                    VALUE(%s, %s, %s, %s, %s, %s, %s, %s)""", product_list)

        self.cursor.execute("""SELECT id FROM product WHERE category =
                            '"""+str(food)+"""' """)

        the_ids = self.cursor.fetchall()

        for el in the_ids:
            self.cursor.execute("""INSERT INTO product_category (id_product,
                                id_category) VALUES('"""+str(el[0])+"""',
                                '"""+str(id_cat)+"""')""")

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
