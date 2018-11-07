#!/usr/bin/python3

from config import config

import psycopg2


def connect(sql_file):

    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        cur.execute(open(sql_file, 'r').read())
        rows = cur.fetchall()

        # close the communication with the PostgreSQL
        cur.close()

        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    connect()
