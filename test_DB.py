from models.user import User
from datetime import datetime

new_instance = User(
    first_name='Ezz',
    last_name='Morgan',
    email='ezzmorgan94@gmail.com',
    password='ezz1144',
    user_name='emorg',
    date_of_birth=datetime(2004, 1, 1).date()
)

new_instance.save()

from models import storage

res = storage.all('User')
for i in res:
    print(i)
