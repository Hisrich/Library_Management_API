# LIBRARY MANAGEMENT API

## Project Overview
This is a RESTful API for managing books in an online library built using Flask. PostgreSQL is used for the database for this project. API rate limiting was implemented to protect the API from abuse

Live link is at [https://library-management-api-j0bg.onrender.com](https://library-management-api-j0bg.onrender.com)

Doc link at https://documenter.getpostman.com/view/38293019/2sAYQiCTxn


## Installation Instructions

### Prerequisites

Before setting up the project locally, ensure the following prerequisites installed:

- [Python](https://www.python.org/downloads/)
- [Flask](https://pypi.org/project/Flask/)
- Database System (Postgres)


### Installation Steps

1. Clone the repository:

        git clone https://github.com/Hisrich/Library_Management_API

2. Change into the parent directory:

        cd Library_Management_API

3. Set up a virtual environment:

        python -m venv venv

4. Activate your virtual environment:

        source venv/Scripts/activate

5. Install the Python dependencies:

        pip install -r requirements.txt

6. Create a .env file and set necessary secret keys below:
- API_TOKEN
- DATABASE

7. Run the Flask app

        python app.py


The API should now be running locally at [http://127.0.0.1:5000/api/v1/books](http://127.0.0.1:5000/api/v1/books)



## API ENDPOINTS

1. Get all books

        GET /api/v1/books

- Response Example:

        {
            "books": [
                {
                    "author": "Ben Frank",
                    "genre": "Mystery",
                    "id": 1,
                    "publication_date": "1994-09-16",
                    "title": "Emotional Intelligence"
                },
                {
                    "author": "Robert Kiyosaki",
                    "genre": "Finance",
                    "id": 2,
                    "publication_date": "2000-12-29",
                    "title": "Rich Dad Poor Dad"
                }
            ], 
            "pagination": {
                "current_page": 1,
                "per_page": 10,
                "total_pages": 1
                }
        }


2. Get a specific book

        GET /api/v1/books/{id}

- Response Example:

        "book":
                {
                    "author": "Ben Frank",
                    "genre": "Mystery",
                    "id": 1,
                    "publication_date": "1994-09-16",
                    "title": "Emotional Intelligence"
                }


3. Add a book

        POST /api/v1/books

- Response Example: 
   
        {
            "book_id": 5,
            "message": "Book added successfully"
        }


4. Update a book

        PUT /api/v1/books/{id}

- Response Example:

        {
            "message": "Book updated successfully"
        }


5. Delete a book

        DELETE /api/v1/books/{id}

- Response Example: 

        {
            "message": "Book successfully deleted"
        }


## CONTACT
For questions, reach out to:

- Email: addisinicholas@gmail.com
- GitHub: @hisrich