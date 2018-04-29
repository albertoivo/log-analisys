#!/usr/bin/python3

from config import config

import psycopg2


def connect():
    """ What are the three most popular articles of all time? """

    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        cur.execute(open('popularArticles.sql', 'r').read())
        rows = cur.fetchall()

        print('\nWhat are the three most popular articles of all time?\n')
        for row in rows:
            print('\t"%s" - %s views' % (row[0], row[1]))

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    connect()
