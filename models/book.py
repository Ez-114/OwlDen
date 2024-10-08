"""
models.books moudle.

This module defines the Book class model in the models package that
inherits from the models.BaseModel class model.
"""

from sqlalchemy import Column, String, Text, Integer, Float, Date

from sqlalchemy.orm import relationship

from models.base_model import BaseModel
from models.association_tables import book_rate_jt
from models.association_tables import book_review_jt
from models.association_tables import book_genre_jt
from models.association_tables import book_author_jt
from models.association_tables import book_publisher_jt


class Book(BaseModel):
    """
    Book class.

    The blueprint of the user model.
    """

    __tablename__ = "books"

    title = Column(String(128))
    isbn = Column(String(13), unique=True)
    description = Column(Text)
    cover_image_url = Column(String(255))
    page_count = Column(Integer, default=0)
    average_rating = Column(Float(precision=2), default=0.00)
    publish_date = Column(Date)

    book_rates = relationship("Rate", back_populates="book")

    book_reviews = relationship("Review", back_populates="book")

    book_authors = relationship(
        "Author", secondary=book_author_jt, back_populates="book"
    )

    book_genres = relationship("Genre", secondary=book_genre_jt, back_populates="book")

    book_publishers = relationship(
        "Publisher", secondary=book_publisher_jt, back_populates="book"
    )

    def __init__(self, *_, **kwargs):
        """Calls its super class' init method"""
        super().__init__(*_, **kwargs)
