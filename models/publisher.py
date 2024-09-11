"""
models.publisher Module.

This module defines the Author class model in the models package that
inherits from the models.BaseModel class model.
"""

from sqlalchemy import Column, String, Text, Date
from sqlalchemy.orm import relationship

from models.base_model import BaseModel
from models.association_tables import book_publisher_jt

class Publisher(BaseModel):
    """
    Publisher class.

    Blueprint for the Publisher model.
    """

    __tablename__ = 'publishers'

    name = Column(String(128), nullable=False, unique=True)
    address = Column(String(128))
    website = Column(String(255))
    email = Column(String(128))

    book = relationship(
                'Book',
                secondary=book_publisher_jt,
                back_populates='book_publishers'
            )

    def __init__(self, *_, **kwargs):
        """calls its super class' init method"""
        super().__init__(*_, **kwargs)
