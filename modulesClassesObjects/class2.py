#!/usr/bin/python

class ClassName:
    'Documentation class string'
    def enter(self):
        pass

defNewClass = ClassName();


#  will print doc string
# print defNewClass.__doc__


class Book:
    "Common class for all books"
    bookCount = 0

    def __init__(self, author, year):
        self.author = author
        self.year = year
        Book.bookCount += 1

    def displayId(self):
        print 'Total number of books: %d' % Book.bookCount

    def displayBook(self):
        print 'Author: ', self.author, ', Year:', self.year


book1 = Book("Proust", 1922)
book2 = Book("Joyce", 1950)

book1.displayId()
book1.displayBook()
book1.title = 'Hladanie strateneho casu'

# print hasattr(book1, 'title')
# print getattr(book1, 'title')
# print setattr(book1, 'title', 'Hladanie strateneho casu 2')
# print getattr(book1, 'title')
# print delattr(book1, 'title')
# print hasattr(book1, 'title')

#dictionary containing class namespace
print "book dict:", book1.__dict__
print "book doc", book1.__doc__

# not work in p2.7?
# print book1.__name__
print "module", book1.__module__
# print "bases: ", book1.__bases__

# book2.displayId()
# book2.displayBook()

# print __name__
