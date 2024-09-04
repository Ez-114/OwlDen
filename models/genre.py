"""
models.genre module.

This module defines the Rate class module in the models package
that inherits from the models.BaseModel class model.
"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel
from models.association_tables import book_genre_jt


class Genre(BaseModel):
    """
    Genre class.

    Blueprint for the Genre model.
    """

    __tablename__ = 'genres'

    name = Column(String(60), nullable=False, unique=True)

    book = relationship(
                'Book',
                secondary=book_genre_jt,
                back_populates='book_genres'
            )

    def __init__(self, *_, **kwargs):
        """Calls the super class init"""
        super().__init__(*_, **kwargs)
