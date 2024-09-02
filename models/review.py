from models.base_model import BaseModel


class Review(BaseModel):
    """Reviews"""

    user_id = ""
    review_text = ""
    review_data = None
