import requests
from datetime import datetime

# Import your models
from models import storage
from models.book import Book
from models.author import Author
from models.genre import Genre
from models.publisher import Publisher

# Google Books API setup
API_KEY = 'AIzaSyCq1lkdI_rQf-zGnpO2rgl04KSqhvJ8JKo'
API_URL = "https://www.googleapis.com/books/v1/volumes"


def fetch_books_from_google(query):
    """Fetch books from Google Books API by search query."""
    params = {
        'q': query,
        'key': API_KEY,
        'maxResults': 10  # Limit the number of results to 10
    }
    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        books_data = response.json().get('items', [])
        return books_data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []

def add_book_to_db(book_data):
    """Add a book to the database."""
    volume_info = book_data['volumeInfo']

    # Extract relevant data
    title = volume_info.get('title')
    isbn_list = volume_info.get('industryIdentifiers', [])
    isbn = next((isbn['identifier'] for isbn in isbn_list if isbn['type'] == 'ISBN_13'), None)
    description = volume_info.get('description', 'No description available')
    cover_image_url = volume_info.get('imageLinks', {}).get('thumbnail', '')
    page_count = volume_info.get('pageCount', 0)
    average_rating = volume_info.get('averageRating', 0)

    # Add genre(s)
    genres = volume_info.get('categories', [])
    genre_objects = []
    for genre in genres:
        genre_obj = storage.session.query(Genre).filter_by(name=genre).first()
        if not genre_obj:
            genre_obj = Genre(name=genre)
            storage.session.add(genre_obj)
        genre_objects.append(genre_obj)

    # Add author(s)
    authors = volume_info.get('authors', [])
    author_objects = []
    for author in authors:
        author_obj = storage.session.query(Author).filter_by(name=author).first()
        if not author_obj:
            author_obj = Author(
                    name=author,
                    date_of_birth=datetime(2003, 1, 2).date()
                )
            storage.session.add(author_obj)
        author_objects.append(author_obj)

    # Add publisher
    publisher_name = volume_info.get('publisher', 'Unknown Publisher')
    publisher_obj = storage.session.query(Publisher).filter_by(name=publisher_name).first()
    if not publisher_obj:
        publisher_obj = Publisher(
                    name=publisher_name,
                    address="not defined",
                    website="not defined",
                    email="not defined"
                )
        storage.session.add(publisher_obj)

    # Check if the book already exists in the database
    existing_book = storage.session.query(Book).filter_by(isbn=isbn).first()
    if not existing_book:
        # Create a new Book object
        new_book = Book(
            title=title,
            isbn=isbn,
            description=description,
            cover_image_url=cover_image_url,
            page_count=page_count,
            average_rating=average_rating,
            publish_date=datetime(2004, 1, 1).date(),
            book_genres=genre_objects,  # Add many-to-many relationships
            book_authors=author_objects,
            book_publishers=[publisher_obj]
        )
        storage.session.add(new_book)

def populate_books(query):
    """Populate the database with books from Google Books API by query."""
    books = fetch_books_from_google(query)
    for book_data in books:
        add_book_to_db(book_data)
    storage.session.commit()

# Example usage: Fetch and store books related to "Python programming"
populate_books("Python programming")
