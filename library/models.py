from sqlalchemy import Column, ForeignKey, Integer, String

# to get base from which to derive/attach all other classes
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationships

# create declarative_base instance
Base = declarative_base()


# create new classes here
class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    genre = Column(String(250))

    def __repr__(self):
        return "Title: {} by {}".format(self.title, self.author)
