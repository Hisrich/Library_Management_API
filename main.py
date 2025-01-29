# response = {
#         "books": [
#             {"id": book.id, "title": book.title, "author": book.author, "genre": book.genre, "publication_date": book.publication_date}
#             for book in books.items
#         ],
#         "pagination": {"page": page, "per_page": per_page, "total": books.total},
#     }