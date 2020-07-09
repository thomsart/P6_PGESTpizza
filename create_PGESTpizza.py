#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import database_creation as dc

###############################################################################

""" In this file we create the database 'PGESTpizza' and fill it with some
datas to show the relevance of it's structure """

###############################################################################

def main():

    database = dc.Database('', 'root', 'Metalspirit77+')
    database.create_the_database()
    database.disconnect()

    return

if __name__ == "__main__":

    main()