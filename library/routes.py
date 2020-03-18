from flask import render_template, request, redirect, url_for
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

from library import app
from library.models import Book, Base

# create a session instance for writing and reading from database
print("Inside routes")
engine = create_engine('sqlite:///books-collection.db')
# Base.metadata.bind = engine
# use scoped_session() to handle creating a unique session for each thread
session = scoped_session(sessionmaker(bind=engine))


# landing page
@app.route('/')
@app.route('/books')
def show_books():
    books = session.query(Book).all()
    return render_template("books.html", books=books)


@app.route('/books/new/',methods=['GET','POST'])
def new_book():
    if request.method == 'POST':
        book = Book(title=request.form['name'], author=request.form['author'], genre=request.form['genre'])
        session.add(book)
        session.commit()
        return redirect(url_for('show_books'))
    else:
        return render_template('newBook.html')


@app.route("/books/<int:book_id>/edit/", methods=['GET', 'POST'])
def edit_book(book_id):
    edited_book = session.query(Book).filter_by(id=book_id).one()
    if request.method == 'POST':
        if request.form['name']:
            edited_book.title = request.form['name']
            session.commit()
            return redirect(url_for('show_books'))
    else:
        return render_template('editBook.html', book=edited_book)


@app.route('/books/<int:book_id>/delete/', methods=['GET', 'POST'])
def delete_book(book_id):
    book_to_delete = session.query(Book).filter_by(id=book_id).one()
    if request.method == 'POST':
        session.delete(book_to_delete)
        session.commit()
        return redirect(url_for('show_books', book_id=book_id))
    else:
        return render_template('deleteBook.html', book=book_to_delete)

