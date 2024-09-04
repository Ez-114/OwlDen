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

    email = Column(String(100), nullable=False, unique=True)
    user_name = Column(String(50), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    date_of_birth = Column(Date, nullable=True)
    last_login = Column(DateTime, default=datetime.now, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)

    ratings = relationship('Rate', back_populates='user')

    def __init__(self, *_, **kwargs):
        """Calls the super class init"""
        super().__init__(*_, **kwargs)
