"""
models.user Module.

This module defines the User class model in the models package that
inherits from the models.BaseModel class model.
"""

import enum
from sqlalchemy import Column, String, DateTime, Date, Enum
from sqlalchemy.orm import relationship
from datetime import datetime

from models.base_model import BaseModel


class UserRole(enum.Enum):
    """Contains User Roles as Enums"""
    USER = 'user'
    ADMIN = 'admin'


class User(BaseModel):
    """
    User class.

    The blueprint of the user model.
    """

    __tablename__ = 'users'

    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    user_name = Column(String(50), nullable=False, unique=True)
    date_of_birth = Column(Date, nullable=True)
    last_login = Column(DateTime, default=datetime.now, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)

    user_ratings = relationship('Rate', back_populates='user')
    user_reviews = relationship('Review', back_populates='user')

    def __init__(self, *_, **kwargs):
        """Calls the super class init"""
        super().__init__(*_, **kwargs)
