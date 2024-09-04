"""
models.base_models Module.

This module defines the BaseModel class in the models package
that serves as a base class for all other models.

The BaseModel class provides common attributes and methods for other models,
including:
    - id: A unique identifier for each instance.
    - created_at: The timestamp when an instance is created.
    - updated_at: The timestamp when an instance is updated.
    - __str__: A method that provides a string representation of the instance.
    - save: A method to update the 'updated_at' timestamp.
    - to_dict: A method to generate a dictionary representation
                of the instance.

The BaseModel class uses the UUID python package to give its instances their
unique ids. It also uses the datetime package to give each instance
its timestamps.
"""


from copy import deepcopy
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import DeclarativeBase
from uuid import uuid4

from models import storage


class BaseModel(DeclarativeBase):
    """
    BaseModel class.

    The parent of all model classes. It defines all common
    attributes and methods for other model classes.
    """

    # Mark this class as an abstract class
    __abstract__ = True

    # Define common columns
    id = Column(String(60), primary_key=True, default=lambda: str(uuid4()))
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime,
                        default=datetime.now,
                        onupdate=datetime.now,
                        nullable=False)

    def __init__(self, *_, **kwargs):
        """
        BaseModel.__init__() Instance initialization method.

        It initializes a new BaseModel instance
        giving it its unique identifiers.
        """

        if kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.fromisoformat(val)
                if key != '__class__':
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = deepcopy(self.created_at)
            storage.new(self)

    def save(self):
        """
        BaseModel.save() Instance method.

        Updates the public instance attribute `updated_at` with the current
        new timestamp.
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        BaseModel.to_dict() Instance method.

        Creates the dictionary representation of the BaseModel instance,
        including:
            - all instance attributes.
            - the class name.
            - its timestamps in iso format

        Returns:
            dict: The created dictionary representation.
        """

        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()

        return instance_dict

    def __str__(self):
        """
        BaseModel.__str__() Instance method.

        Creates the string representation of the BaseModel instance.

        Returns:
            str: the created string representation.
        """

        return "[{}] ({}) {}".format(
                        self.__class__.__name__,
                        self.id,
                        self.__dict__
                    )
