class Author:

    def __init__(self, author_num, name_last, name_first):

        self.num = author_num
        self.last = name_last
        self.first = name_first

    def __repr__(self):
        return f"{self.first} {self.last}"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        if type(self) == type(other):
            return self.first == other.first
        else:
            return NotImplemented

    def __lt__(self, other):
        if type(self) == type(other):
            return self.first < other.first


class Book:

    def __init__(self, book_code, title, price):
        self.book_code = book_code
        self.title = title
        self.price = price

    def __repr__(self):
        return f"{self.title}"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        if type(self) == type(other):
            return self.title == other.title
        else:
            return NotImplemented

    def __lt__(self, other):
        if type(self) == type(other):
            return self.title < other.title


class Publisher:

    def __init__(self, publisher_code, publisher_name):
        self.pub_code = publisher_code
        self.pub_name = publisher_name

    def __repr__(self):
        return f"{self.pub_name}"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        if type(self) == type(other):
            return self.pub_name == self.pub_name
        else:
            return NotImplemented

    def __lt__(self, other):
        if type(self) == type(other):
            return self.pub_name < self.pub_name


if __name__ == '__main__':

    pass
