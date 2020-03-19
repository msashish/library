# for creating foreign key relationship between the tables
from sqlalchemy.orm import sessionmaker

# to create engine that ties to physical location of DB
from sqlalchemy import create_engine

from library.models import Base, Book, Author

print("creating an empty database")
# create engine instance of DB pointing to a physical DB
engine = create_engine('sqlite:///books-collection.db')

# This will convert all new classes derived from Base into new tables in the database
Base.metadata.create_all(engine)

print("Loading 3 books to empty database")
# create a session instance for writing and reading from database
Base.metadata.bind = engine
session = sessionmaker(bind=engine)()

session.add(Book(title="Unknown", author="pi/2", genre="Mathematics"))
session.add(Book(title="I Know", author="None", genre="Mathematics"))
session.add(Book(title="Cradle of Life", author="God", genre="Everything"))

session.add(Author(name="pi/2", age=39))
session.add(Author(name="None", age=19))
session.add(Author(name="God", age=200))
session.add(Author(name="Ashish", age=30))
session.commit()
