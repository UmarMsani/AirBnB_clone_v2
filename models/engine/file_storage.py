#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary or filtered list of models
        currently in storage
        """
        if cls is None:
            return self.__objects
        elif type(cls) == str:
            return {key: obj for key, obj in self.__objects.items()
                    if obj.__class__.__name__ == cls}
        else:
            return {key: obj for key, obj in self.__objects.items()
                    if obj.__class__ == cls}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                "BaseModel": BaseModel, "User": User, "Place": Place,
                "State": State, "City": City, "Amenity": Amenity,
                "Review": Review
                }
        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    cls_name = val['__class__']
                    self.__objects[key] = classes[cls_name](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects"""
        if obj is None:
            return
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects.pop(key, None)

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()
