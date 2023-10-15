#!/usr/bin/python3
"""Module defining class FileStorage."""
import json


class FileStorage:
    """The class serializes instances to a JSON file,

    deserializes JSON file to instances."""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    @classmethod
    def new(cls, obj):
        """sets in __objects the obj with key 'obj_class_name.id'"""
        cls.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """Serializes __objects to JSON file '__file_path'"""
        my_obj = {}
        for key, value in FileStorage.__objects.items():
            try:
                my_obj[key] = value.to_dict()
            except AttributeError:
                my_obj[key] = value

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as j_file:
            json.dump(my_obj, j_file)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as j_str:
                my_dict = json.load(j_str)
            for key, value in my_dict.items():
                FileStorage.__objects[key] = value
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
