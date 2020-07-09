#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import database_creation as dc

###############################################################################

"""  """

###############################################################################

def main():

    database = dc.Database('', 'root', 'Metalspirit77+')
    database.create_the_database()
    database.disconnect()

    database = dc.Database('PGESTpizza', 'root', 'Metalspirit77+')
    database.fill_tables()
    database.disconnect()

    return

if __name__ == "__main__":

    main()