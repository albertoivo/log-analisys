#!/usr/bin/python3

from config import config

import psycopg2


query = """
SELECT
  ROUND(CAST(float8(SUM("404 NOT FOUND") * 100.0 / COUNT(*)) AS numeric), 2),
  COALESCE(to_char(TIME, 'Month DD, YYYY'), '')
  FROM (SELECT
      CASE
        WHEN status <> '200 OK' THEN 1
        ELSE 0 END AS "404 NOT FOUND",
      TIME
    FROM log) AS NOTFOUND
GROUP BY COALESCE(to_char(TIME, 'Month DD, YYYY'), '')
  HAVING (SUM("404 NOT FOUND") * 100.0 / COUNT(*)) >= 1.0
"""


def connect():
    """ Which days more than 1% of requests resulted in errors? """

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

        print('\nWhich days more than 1% of requests resulted in errors?\n')
        for row in rows:
            print ('\t%s %% - %s' % (row[0], row[1]))

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    connect()
