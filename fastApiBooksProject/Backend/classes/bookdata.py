class bookdata :
    id : int
    name : str
    author : str
    rating : str
    published_year : int
    
    def __init__(self,id,name,author,rating,published_year) -> None:
        self.id = id
        self.name = name
        self.author = author
        self.rating = rating
        self.published_year = published_year
    
        