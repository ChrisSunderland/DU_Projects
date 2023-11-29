import mysql.connector
from henryInterfaceClasses import Author, Book, Publisher
import os
from dotenv import load_dotenv


class HenryDAO:

    def __init__(self):

        load_dotenv()

        # create connection
        self.db = mysql.connector.connect(
            user='root',
            # enter your own MySQL server password, database information here
            passwd=os.getenv('mysql_db_password'),
            database= os.getenv('mysql_db_name'),
            host= os.getenv('mysql_db_host'))

        self.cursor = self.db.cursor()

    def close(self):
        self.db.commit()
        self.db.close()

    def getAuthorData(self):

        query = 'SELECT distinct(HENRY_WROTE.AUTHOR_NUM), AUTHOR_LAST, AUTHOR_FIRST ' \
                'FROM HENRY_AUTHOR JOIN HENRY_WROTE ' \
                'ON HENRY_AUTHOR.AUTHOR_NUM = HENRY_WROTE.AUTHOR_NUM'

        self.cursor.execute(query)

        authors = []

        for row in self.cursor:
            author_info = Author(row[0], row[1], row[2])
            authors.append(author_info)

        authors = sorted(authors, key=lambda x: x.first)

        return authors

    def getAuthorBooks(self, author_num):

        books_query = 'SELECT HENRY_BOOK.BOOK_CODE, TITLE, PRICE ' \
                      'FROM HENRY_AUTHOR JOIN HENRY_WROTE ' \
                      'ON HENRY_AUTHOR.AUTHOR_NUM = HENRY_WROTE.AUTHOR_NUM ' \
                      'JOIN HENRY_BOOK ' \
                      'ON HENRY_WROTE.BOOK_CODE = HENRY_BOOK.BOOK_CODE ' \
                      'WHERE HENRY_AUTHOR.AUTHOR_NUM = {}'.format(author_num)

        self.cursor.execute(books_query)

        books = []

        for row in self.cursor:
            book_info = Book(row[0], row[1], row[2])
            books.append(book_info)

        books = sorted(books, key=lambda x: x.title)

        return books

    def getBookAvailability(self, book_code):

        book_info_query = 'SELECT BRANCH_NAME, ON_HAND ' \
                          'FROM HENRY_BOOK JOIN HENRY_INVENTORY ' \
                          'ON HENRY_BOOK.BOOK_CODE = HENRY_INVENTORY.BOOK_CODE ' \
                          'JOIN HENRY_BRANCH ' \
                          'ON HENRY_INVENTORY.BRANCH_NUM = HENRY_BRANCH.BRANCH_NUM ' \
                          'WHERE HENRY_BOOK.BOOK_CODE = \'{}\''.format(book_code)

        self.cursor.execute(book_info_query)

        branch_info = []
        copies = []

        for row in self.cursor:
            branch_info.append(row[0])
            copies.append(str(row[1]))

        return branch_info, copies

    def getCategories(self):

        category_query = 'SELECT DISTINCT(TYPE) FROM HENRY_BOOK'
        self.cursor.execute(category_query)
        categories = [row[0] for row in self.cursor]

        return sorted(categories)

    def getBooksbyCategory(self, category):

        query = f"SELECT BOOK_CODE, TITLE, PRICE " \
                f"FROM HENRY_BOOK " \
                f"WHERE TYPE = '{category}'"

        self.cursor.execute(query)

        books_by_category = []

        for row in self.cursor:
            book_info = Book(row[0], row[1], row[2])
            books_by_category.append(book_info)

        books_by_category = sorted(books_by_category, key=lambda x: x.title)

        return books_by_category

    def getPublishers(self):

        query = 'SELECT DISTINCT(HENRY_PUBLISHER.PUBLISHER_CODE), PUBLISHER_NAME ' \
                'FROM HENRY_PUBLISHER JOIN HENRY_BOOK ' \
                'ON HENRY_PUBLISHER.PUBLISHER_CODE = HENRY_BOOK.PUBLISHER_CODE'

        self.cursor.execute(query)
        publishers = [Publisher(row[0], row[1]) for row in self.cursor]
        publishers = sorted(publishers, key=lambda x: x.pub_name)

        return publishers

    def getBooksbyPublisher(self, publisher_code):

        query = f"SELECT BOOK_CODE, TITLE, PRICE " \
                "FROM HENRY_BOOK " \
                f"WHERE PUBLISHER_CODE = '{publisher_code}'"

        self.cursor.execute(query)

        books_by_publisher = []

        for row in self.cursor:
            book_info = Book(row[0], row[1], row[2])
            books_by_publisher.append(book_info)

        books_by_publisher = sorted(books_by_publisher, key=lambda x: x.title)

        return books_by_publisher


if __name__ == '__main__':

    pass
