from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique = True, nullable = False)
    author = db.Column(db.String(80), unique = False, nullable = False)
    publisher = db.Column(db.String(80), unique = False, nullable = True)

    def __repr__(self):
        return f"{self.book_name} - {self.author}"
    
@app.route('/')
def index():
    return 'Hello'

@app.route('/books')
def get_books():
    books = Book.query.all()
    
    output = []
    for book in books:
        book_data = {'book name':book.book_name, 'author':book.author}
        output.append(book_data)
    return {'books': output}