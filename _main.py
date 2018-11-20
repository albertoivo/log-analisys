#!/usr/bin/python3

import sql_queries.error as error
import sql_queries.popularAuthors as authors
import sql_queries.popularArticles as articles

if __name__ == '__main__':
    articles.connect()
    authors.connect()
    error.connect()
