#!/usr/bin/python3
""" Base Model class module"""


import models
import uuid
from datetime import datetime

time_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel():
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialize class"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == ":updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Return print/str representation of the Base Model instance"""

        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ of the
        Base Model instance"""
        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = type(self).__name__
        dict_obj["created_at"] = self.created_at.strftime(time_format)
        dict_obj["updated_at"] = self.updated_at.strftime(time_format)
        return dict_obj

    def save(self):
        """Update the public instance attribute updated_at with the current
        datetime"""
        self.updated_at = datetime.now()
