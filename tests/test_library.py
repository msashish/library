from library import __version__
from library.models import Book, Author, Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine


engine = create_engine('sqlite:///books-collection.db')
# Base.metadata.bind = engine
# use scoped_session() to handle creating a unique session for each thread
session = scoped_session(sessionmaker(bind=engine))


def test_book():
    books = session.query(Book).all()
    for book in books:
        print("Book name '{}' written by author {}".format(book.title, book.authors.name))


def test_author():
    authors = session.query(Author).all()
    for author in authors:
        print("Author '{}' aged {} has written books: {}".format(author.name, author.age,
                                                                 str(','.join(a.title for a in author.books))))


def test_book_join_author():
    print("Book     Genre    Author name    age ")
    print("------  ------   ------------   -----")
    for b, a in session.query(Book, Author).filter(Book.author == Author.name).all():
        print(b.title, b.genre, a.name, a.age)


if __name__ == "__main__":
    test_book()
    test_author()
    test_book_join_author()
