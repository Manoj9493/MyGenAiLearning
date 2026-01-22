from classes.bookdata import bookdata
from classes.pydentic_book import BookRequest
from fastapi import Body, FastAPI, HTTPException, Path, Query, exceptions
from helper_functions.helperFunction import findBookId
from fastapi.middleware.cors import CORSMiddleware
from starlette import status

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (you can restrict later)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

book_data = [
    bookdata(1, "One Piece", "oda", 10, 2000),
    bookdata(2, "Demon Slayer", "Koyoharu Gotouge", 10, 2010),
    bookdata(3, "AOT", "Hajime Isayama", 10, 2012),
]


# Get Api's
@app.get("/", status_code=status.HTTP_200_OK)
async def getAllBooks():
    return [book.__dict__ for book in book_data]


@app.get("/book/{id}", status_code=status.HTTP_200_OK)
async def getBookById(id: int = Path(gt=0)):
    for book in book_data:
        if book.id == id:
            return book
    raise HTTPException(status_code=404, detail="Book Not found")


@app.get("/books/bookByRating/", status_code=status.HTTP_200_OK)
async def fetchBookByRating(rating: int = Query(gt=0, lt=11)):
    list_of_books = []
    for book in book_data:
        if book.rating == rating:
            list_of_books.append(book)
    return list_of_books


@app.get("/books/getBooksByPublishedYear", status_code=status.HTTP_200_OK)
async def fetchBookByPublishedYear(year: int):
    list_of_books = []
    for book in book_data:
        if book.published_year == year:
            list_of_books.append(book)

    return list_of_books


# Post Api's
@app.post("/books/createBook", status_code=status.HTTP_201_CREATED)
async def createBook(newbook: BookRequest):
    new_book = bookdata(**newbook.model_dump())
    new_book_with_id = findBookId(book_data=book_data, book=new_book)
    book_data.append(new_book_with_id)


# Put Api's
@app.put("/books/updateBook", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(id: int, updated_book: BookRequest):
    book_updated = False
    for i in range(len(book_data)):
        if book_data[i].id == id:
            new_book = bookdata(**updated_book.model_dump())
            book_data[i] = new_book
            book_updated = not book_updated
    if not book_updated:
        raise HTTPException(status_code=404, detail="Book id not found")


# Delete Api's
@app.delete("/books/deleteBook", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: int):
    book_deleted = False
    for book in range(len(book_data)):
        if book_data[book].id == id:
            book_data.pop(book)
            book_deleted = True
            break
    if not book_deleted:
        raise HTTPException(status_code=404, detail="Book not deleted")
