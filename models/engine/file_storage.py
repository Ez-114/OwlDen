"""
models.engine.file_storage.py Module.

This module implements the FileStorage class that helps in storing
a persistent JSON file containing all data about the pre-defined objects
from their classes.
"""


import json
import os


class FileStorage:
    """
    FileStorage class.

    Serializes instances to a JSON file and
    deserializes JSON file to instances.

    Attributes:
        - __file_path (str): Path to the JSON file (ex: file.json)
        - __objects (dict): Stores all created objects by <class name>.id

    Methods:
        - all(): Returns the dictionary __objects
        - new(obj): Sets in __objects the obj with key <obj class name>.id
        - save(): Serializes __objects to the JSON file (path: __file_path)
        - reload(): Deserializes the JSON file to __objects
                (only if the JSON file (__file_path) exists;
                        otherwise, do nothing.)
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        FileStorage.all() Instance method.

        Returns:
            dict: the __objects dictionary
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        FileStorage.new() Instance method.

        Sets in __objects the obj with key [<obj class name>.id]
        """

        FileStorage.__objects.update({
                f'{obj.__class__.__name__}.{obj.id}': obj
            })

    def save(self):
        """
        FileStorage.save() Instance method.

        Serializes __objects to the JSON file (path: __file_path)
        """

        json_objects = FileStorage.__objects.copy()
        for obj_id, obj in json_objects.items():
            json_objects[obj_id] = obj.to_dict()

        # Open the file that will save our objects data
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') \
                as storage_file:

            json.dump(json_objects, storage_file)

    def reload(self):
        """
        FileStorage.reload() Instance method.

        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.)
        """
        from models.base_model import BaseModel
        from models.user import User

        classes_dict = {
            'BaseModel': BaseModel,
            'User': User
        }

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') \
                    as storage_file:

                loaded_objs = json.load(storage_file)

            # Now fill in the __objects dict with loaded objects
            for obj_id, obj_data in loaded_objs.items():
                FileStorage.__objects.update({
                        obj_id: classes_dict[obj_data['__class__']](**obj_data)
                    })
