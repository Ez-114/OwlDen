"""
Defines the Database storage module.

This module uses sqlalchemy to connect to a MySQL Database
server to handel storing, adding, deleting, & updating
data.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.base_model import BaseModel

from models.author import Author
from models.book import Book
from models.genre import Genre
from models.publisher import Publisher
from models.rate import Rate
from models.review import Review
from models.user import User


class DBstorage():
    """A storage class that interacts with the MySQL Server"""

    __engine = None
    __session = None
    __classes_dict = {
        'Author': Author, 'Book': Book,
        'Genre': Genre, 'Publisher': Publisher,
        'Rate': Rate, 'Review': Review,
        'User': User
    }

    def __init__(self):
        """Initializes the engine variable and apply environment configs"""

        self.__engine = create_engine(
            'sqlite:///:memory:', echo=True
        )

    def all(self, cls=None):
        """
        Retrives all entries/instances of a given class.
        If no class name is passed, all entries for all classes
        are retrieved.

        Args:
            cls (obj, optional) - the passed class name. Defaults to None.

        Returns:
            dict - dictionary containing all retrived entries in
                    the following format: {<cls_name>.<obj_id>: obj}
        """

        obj_dict = {}

        if cls and cls in self.__classes_dict:
            objects_q = self.__session.query(self.__classes_dict[cls]).all()

            for obj in objects_q:
                obj_key = f"{obj.__class__.__name__}.{obj.id}"
                obj_dict[obj_key] = obj

        elif cls is None:

            for class_name in self.__classes_dict.keys():
                objects_q = self.__session.query(
                                    self.__classes_dict[class_name]
                            ).all()

                for obj in objects_q:
                    obj_key = f"{obj.__class__.__name__}.{obj.id}"
                    obj_dict[obj_key] = obj

        return obj_dict

    def new(self, obj):
        """
        Adds new object to the session object to stage it for commiting.

        Args:
            obj (object) - the passed object
        """

        self.__session.add(obj)

    def save(self):
        """
        Save/Commit the new added object(s) to in the session object.
        """

        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes a given object.

        Args:
            obj (object, optional) - passed object.
        """

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reloads or init a session to process T-SQL statements
        """

        BaseModel.metadata.create_all(self.__engine)

        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()
