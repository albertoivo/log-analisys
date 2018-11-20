#!/usr/bin/python3

from config import config
import psycopg2


def connect(sql_file):
    """
        Data Access to any SQL files. It connects to database,
        execute the query in 'sql_file' and fetches all rows.
    """

    conn = None
    try:
        # read connection parameters form the database.ini
        params = config()

        # connect to the PostgreSQL server with the database.ini info
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        cur.execute(open(sql_file, 'r').read())

        # Fetch all rows of a query result, returning them as a list of tuples
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
