from models.base_model import BaseModel


class Book(BaseModel):
    """Book"""

    title = ""
    isbn = ""
    description = ""
    cover_image_url = ""
    page_count = 0
    average_rating = 0
    publish_date = None
