#!/usr/bin/python
""" a class BaseModel that defines all common attributes/methods
    for other classes
"""
import uuid
from datetime import datetime


class BaseModel():
    """The BaseModel class from which future classes will be derived"""
    def __init__(self):
        """Initialization of the base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict


if __name__ == "__main__":
    pass
