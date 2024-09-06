from models.user import User
# from models.rate import Rate
# from models.book import Book
# from datetime import datetime

from models import storage

session = storage.session
q_res = session.query(User).all()

for entry in q_res:
    print(entry.first_name, entry.last_name)
