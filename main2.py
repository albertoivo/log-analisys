#!/usr/bin/python3

from dbaccesses import connect

sql_files = {
    'error.sql':
        'Which days more than 1% of requests resulted in errors?',
    'popularArticles.sql':
        'What are the three most popular articles of all time?',
    'popularAuthors.sql':
        'Who are the authors of most popular articles of all time?'}

if __name__ == '__main__':
    for file in sql_files.items():
        rows = connect("sql/{}".format(file[0]))
        print("\n{}\n".format(file[1]))
        for row in rows:
            print('\t%s %% - %s' % (row[0], row[1]))
