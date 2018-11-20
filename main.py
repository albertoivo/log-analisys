#!/usr/bin/python3

from dbaccesses import connect

sql_dict = {
    'sql/error.sql':
        'Which days more than 1% of requests resulted in errors?',
    'sql/popularArticles.sql':
        'What are the three most popular articles of all time?',
    'sql/popularAuthors.sql':
        'Who are the authors of most popular articles of all time?'}

def call_files():
    for sql in sql_dict.items():
        rows = connect(sql[0])
        print("\n{}\n".format(sql[1]))
        for row in rows:
            print("\t{} - {}".format(row[0], row[1]))

if __name__ == '__main__':
    call_files()
