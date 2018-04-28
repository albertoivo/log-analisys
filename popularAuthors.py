#!/usr/bin/python3

from config import config

import psycopg2


query = """
  SELECT author.name, count(author.name) AS Views
    FROM log l, articles a JOIN authors author ON author.id = a.author
   WHERE substring(l.path, 10) = a.slug
GROUP BY author.name
ORDER BY Views DESC
"""


def connect():
    """ Who are the authors of most popular articles of all time? """

    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        cur.execute(query)
        rows = cur.fetchall()

        print('\nWho are the authors of most popular articles of all time?\n')
        for row in rows:
            print ('\t%s - %s views' % (row[0], row[1]))

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    connect()
