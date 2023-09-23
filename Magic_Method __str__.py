#  What are "magic" methods?
#  Demonstating the __str__ magic method
#  __str__ should return a string object!


class Book:
    def __init__(self, author, title, price, book_id):
        self.author = author
        self.title = title
        self.price = price
        self.book_id = book_id

    # define the necessary method here
    def __str__(self):
        return "{} by {}. ${}. [{}].".format(self.title, self.author, self.price, self.book_id)


cook = Book('George Orwell', 1984, 13.59, 1956789)
print(cook)


#  What are "magic" methods?
#  __str__ vs __repr__
#  Both __repr__ and __str__ should return a string object!
