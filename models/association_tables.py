"""
This module defines the association tables used
to handel the many-to-many relationships between
DataBase tables.
"""

from sqlalchemy import Table, ForeignKey, Column, String

from models.base_model import BaseModel


book_rate_jt = Table(
            'book_rate',
            BaseModel.metadata,
            Column(
                'rate_id', String(60),
                ForeignKey('rates.id'), primary_key=True
            ),
            Column(
                'book_id', String(60),
                ForeignKey('books.id'), primary_key=True
            )
        )

book_review_jt = Table(
            'book_review',
            BaseModel.metadata,
            Column(
                'review_id', String(60),
                ForeignKey('reviews.id'), primary_key=True
            ),
            Column(
                'book_id', String(60),
                ForeignKey('books.id'), primary_key=True
            )
        )

book_genre_jt = Table(
            'book_genre',
            BaseModel.metadata,
            Column(
                'genre_id', String(60),
                ForeignKey('genres.id'), primary_key=True
            ),
            Column(
                'book_id', String(60),
                ForeignKey('books.id'), primary_key=True
            )
        )

book_author_jt = Table(
            'book_author',
            BaseModel.metadata,
            Column(
                'author_id', String(60),
                ForeignKey('authors.id'), primary_key=True
            ),
            Column(
                'book_id', String(60),
                ForeignKey('books.id'), primary_key=True
            )
        )

book_publisher_jt = Table(
            'book_publisher',
            BaseModel.metadata,
            Column(
                'publisher_id', String(60),
                ForeignKey('publishers.id'), primary_key=True
            ),
            Column(
                'book_id', String(60),
                ForeignKey('books.id'), primary_key=True
            )
        )
