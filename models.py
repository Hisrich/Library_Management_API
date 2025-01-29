from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    author = db.Column(db.String(100), nullable = False)
    genre = db.Column(db.String(50), nullable = False)
    publication_date = db.Column(db.String(10), nullable = False)
    availability = db.Column(db.String(20), default = "available")
    edition = db.Column(db.String(20), nullable = True)
    summary = db.Column(db.Text, nullable = True)