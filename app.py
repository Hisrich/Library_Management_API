from flask import Flask, request, jsonify
from models import db, Book
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)

API_TOKEN = os.getenv("API_TOKEN")
DATABASE = os.getenv("DATABASE")

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = API_TOKEN
db.init_app(app)


limiter = Limiter(get_remote_address, app=app, default_limits=["100 per minute"])


@app.route("/api/v1/books", methods =["GET"])
@limiter.limit("100 per minute")
def all_books():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    books = Book.query.paginate(page=page, per_page=per_page)
    response = {
        "books": [
            {"id": book.id, "title": book.title, "author": book.author, "genre": book.genre, "publication_date": book.publication_date}
            for book in books.items
        ],
        "pagination": {
            "current_page": page, "per_page": per_page, "total_pages": books.pages
        }
    }

    return jsonify(response), 200


@app.route("/api/v1/books/<int:id>", methods=["GET"])
@limiter.limit("100 per minute")
def get_book(id):
    book = Book.query.get_or_404(id)
    response = {
        "book":{
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "publication_date": book.publication_date,
            "availability": book.availability,
            "edition": book.edition,
            "summary": book.summary
        }
    }
    return jsonify(response), 200


@app.route("/api/v1/books", methods=["POST"])
@limiter.limit("100 per minute")
def add_book():
    data = request.json
    required_fields = ["title", "author", "genre", "publication_date"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    
    book = Book(
        title = data["title"],
        author = data["author"],
        genre = data["genre"],
        publication_date = data["publication_date"],
        availability = data.get("availability", "available"),
        edition = data.get("edition"),
        summary = data.get("summary")
    )
    
    db.session.add(book)
    db.session.commit()

    return jsonify({"message": "Book added successfully", "book_id": book.id}), 201


@app.route("/api/v1/books/<int:id>", methods=["PUT"])
@limiter.limit("100 per minute")
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.json
    for key in ["title", "author", "genre", "publication_date", "availability", "edition", "summary"]:
        if key in data:
            setattr(book, key, data[key])
    db.session.commit()
   
    return jsonify({"message": "Book updated successfully"}), 200


@app.route("/api/v1/books/<int:id>", methods=["DELETE"])
@limiter.limit("100 per minute")
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()

    return jsonify({"message": "Book successfully deleted"}), 200





if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)