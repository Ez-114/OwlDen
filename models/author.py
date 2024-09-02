from models.base_model import BaseModel


class Author(BaseModel):
    """Author"""

    name = ""
    bio = ""
    date_of_birth = None
    date_of_death = None
