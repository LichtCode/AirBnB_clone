#!/usr/bin/python3
"""
Module file_storage serializes and
deserializes JSON types
"""
import os
import json
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class for storing, serializing and deserializing data
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the __objects dictionary.
        It provides access to all the stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the object with the key
        <object class name>.id

        Args:
            object(obj): object to write
        """
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the __objects dictionary into JSON format
        and saves it to the file specified by __file_path.
        """
        all_obj = FileStorage.__objects
        obj_dict = {}
        for key in all_obj.keys():
            obj_dict[key] = all_obj[key].to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects only if the JSON
        file exists)
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        cls, obj_id = key.split(".")
                        instance = eval(cls)(**value)
                        self.new(instance)
                except Exception:
                    pass
