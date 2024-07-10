#!/usr/bin/python3
""" Base Model class module"""


import models
import uuid
from datetime import datetime

time_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel():
    """BaseModel class"""

    def __init__(self):
        """Initialize class"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """update the public instance attribute updated_at with the current
        datetime"""
        self.update_at = datetime.now()


    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the
        instance"""
        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = type(self).__name__
        dict_obj["created_at"] = self.created_at.strftime(time_format)
        dict_obj["updated_at"] = self.updated_at.strftime(time_format)
        return dict_obj

    def __str__(self):
        """Return print/str representation of the Base Model instance"""

        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
