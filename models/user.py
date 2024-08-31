"""
models.user Module.

This module defines the User class model in the models package that
inherits from the models.BaseModel class model.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    User class.

    The blueprint of the user model.
    """

    email = ""
    user_name = ""
    password = ""
    first_name = ""
    last_name = ""
    date_joined = None
    date_of_birth = None
    last_login = None
    role = ""
