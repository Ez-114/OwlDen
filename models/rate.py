"""
models.rate module.

This module defines the Rate class module in the models package
that inherits from the models.BaseModel class model.
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Rate(BaseModel):
    """
    Rate class.

    Blueprint for the Rate model.
    """

    __tablename__ = 'rates'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    rating_value = Column(Integer, nullable=False, default=0)

    user = relationship('User', back_populates='user_ratings')

    def __init__(self, *_, **kwargs):
        """Calls the super class init"""
        super().__init__(*_, **kwargs)
