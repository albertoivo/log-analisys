#!/usr/bin/python3

from config import config

import psycopg2


query = """
    SELECT a.title, count(a.title) AS quantity
      FROM log l, articles a
     WHERE substring(l.path, 10) = a.slug
  GROUP BY a.title
  ORDER BY quantity DESC
     LIMIT 3
"""


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
        cur.execute(query)
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
