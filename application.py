"""
Author:  Emily Mullins
Date written: 11/19/2023
File: application.py
Short Desc: M04 Case Study
Will create a CRUD api for a book.
            
"""


#Importing flask, sqlalchemy
from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#Creating Book model. id as primary key.

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique = True, nullable = False)
    author = db.Column(db.String(80), unique = False, nullable = False)
    publisher = db.Column(db.String(80), unique = False, nullable = True)

    #represent object as string
    def __repr__(self):
        return f"{self.book_name} - {self.author}"

# default page
@app.route('/')
def index():
    return 'Hello'

#route for /books
@app.route('/books')
def get_books():
    books = Book.query.all()

    # store books
    output = []
    for book in books:
        book_data = {'book name':book.book_name, 'author':book.author}
        output.append(book_data)
    return {'books': output}

#route for books/id
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'book name':book.book_name, 'author': book.author, 
            'publisher':book.publisher}

# POST method for /books
@app.route('/books', methods = ['POST'])
def add_book():
    book = Book(book_name = request.json['author_name'], 
                author = request.json['author'],
                publisher = request.json['publisher']) 
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

# Delete method for /books/id
@app.route('/books/<id>', methods = ['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "deleted!"}
