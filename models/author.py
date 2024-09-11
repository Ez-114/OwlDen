"""
models.author Module.

This module defines the Author class model in the models package that
inherits from the models.BaseModel class model.
"""

from sqlalchemy import Column, String, Text, Date
from sqlalchemy.orm import relationship

from models.base_model import BaseModel
from models.association_tables import book_author_jt


class Author(BaseModel):
    """
    Author class.

    Blueprint for the Author model.
    """

    __tablename__ = 'authors'

    name = Column(String(128), nullable=False, unique=True)
    bio = Column(Text, nullable=True)
    date_of_birth = Column(Date, nullable=True)
    date_of_death = Column(Date, nullable=True)

    book = relationship(
                'Book',
                secondary=book_author_jt,
                back_populates='book_authors'
            )

    def __init__(self, *_, **kwargs):
        """calls its super class' init method"""
        super().__init__(*_, **kwargs)
