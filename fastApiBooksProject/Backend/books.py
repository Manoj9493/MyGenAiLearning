from logging import log
from fastapi import Body, FastAPI


app = FastAPI()

Books = [
    {"title": "One Piece", "Author": "Oda", "chapter": "Wano"},
    {"title": "One Piece", "Author": "Oda", "chapter": "Enies lobbby"},
    {"title": "One Piece", "Author": "Oda", "chapter": "FisherMan"},
    {
        "title": "Demon Slayer",
        "Author": "Koyoharu Gotouge",
        "chapter": "Infinity Castle",
    },
    {
        "title": "Demon Slayer",
        "Author": "Koyoharu Gotouge",
        "chapter": "Entertainment District",
    },
    {"title": "Jujutsu kaisen", "Author": "Gege Akutami", "chapter": "Chapter 1"},
]

# Base
@app.get("/")
async def get_homepage():
    return {"Welcome to the Book Library"}

#enhancement
@app.get("/books")
async def get_all_books():
    return Books


#path parameters
@app.get("/books/{title}")
async def get_book_by_title(title: str):
    list_of_books = []
    for book in Books:
        if book.get("title").casefold() == title.casefold():
            list_of_books.append(book)
        
    return list_of_books

#Post Request
@app.post("/books/addbook")
async def add_book(newBook = Body()):
    Books.append(newBook)

#Put Request with Path Parameters
@app.put("/books/update_book/{title}")
async def update_book(title: str , updated_book = Body()):
    for i in range(len(Books)):
        if Books[i].get("title").casefold() == title.casefold():
            Books[i] = updated_book
            
#Put Request with Path Parameters
@app.put("/books/update_book/")
async def update_book(title: str , updated_book = Body()):
    for i in range(len(Books)):
        if Books[i].get("title").casefold() == title.casefold():
            Books[i] = updated_book
  
#Delete Request with Path Parameters          
@app.delete("/books/delete/")
async def delete_book(title:str):
    for i in range(len(Books)):
        if Books[i].get("title").casefold() == title.casefold():
            Books.pop(i)
        
