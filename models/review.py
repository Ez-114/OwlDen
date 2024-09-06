"""
models.review Module.

This module define the Review class model in the models package that
inherits form the models.BaseModel class model.
"""

from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel
from models.association_tables import book_review_jt


class Review(BaseModel):
    """
    Reviews class.

    The blueprint of the review model.
    """

    __tablename__ = 'reviews'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    book_id = Column(String(60), ForeignKey('books.id'), nullable=False)
    review_text = Column(Text, nullable=False)

    user = relationship('User', back_populates='user_reviews')
    book = relationship(
            'Book',
            secondary=book_review_jt,
            back_populates='book_reviews'
        )

    def __init__(self, *_, **kwargs):
        """Calls the super class init"""
        super().__init__(*_, **kwargs)
