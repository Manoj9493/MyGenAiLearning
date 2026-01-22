
from classes.bookdata import bookdata


def findBookId(book_data : list[bookdata], book : bookdata):
    if len(book_data) == 0:
        book.id = 1
    elif len(book_data) > 0:
        book.id = book_data[-1].id + 1
        
    return book