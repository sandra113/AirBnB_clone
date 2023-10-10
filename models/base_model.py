#!/usr/bin/python3
"""
Base class defining all common attributes for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """ This class defines all attributes/methods of other classes """

    def __init__(self):
        """ Object instantiation """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Returns a string representation of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__ """
        obj_dict = {}
        obj_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                obj_dict[key] = datetime.isoformat(value)
            else:
                obj_dict[key] = value
        return obj_dict
