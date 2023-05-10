#!/usr/bin/env python3
"""
This file contains a class FileStorage that deals with serialization
and deserialization of instances to a JSON file.
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """
    This class serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        
        with open(FileStorage.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                obj = {}
                data = json.load(file)
                for key, value in data.items():
                    obj[key] = eval(key.split('.')[0])(**value)
                FileStorage.__objects = obj
        except FileNotFoundError:
            pass
