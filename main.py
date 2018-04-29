#!/usr/bin/python3

import error as error
import popularAuthors as authors
import popularArticles as articles

if __name__ == '__main__':
    articles.connect()
    authors.connect()
    error.connect()
