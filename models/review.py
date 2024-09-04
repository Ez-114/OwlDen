"""
models.review Module.

This module define the Review class model in the models package that
inherits form the models.BaseModel class model.
"""

from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Reviews class.

    The blueprint of the review model.
    """

    __tablename__ = 'reviews'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    review_text = Column(Text, nullable=False)

    user = relationship('User', back_populates='usr_reviews')

    def __init__(self, *_, **kwargs):
        """Calls the super class init"""
        super().__init__(*_, **kwargs)
