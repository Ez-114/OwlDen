from models.base_model import BaseModel


class Rate(BaseModel):
    """Rate"""

    user_id = ""
    rating_value = 0
    rating_data = None
