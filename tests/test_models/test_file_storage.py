#!/usr/bin/python3
"""Module containing tests for class FileStorage."""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
import os


class TestFileStorage(unittest.TestCase):
    """Tests class for class FileStorageTests"""

    @classmethod
    def setUpClass(cls):
        """setting up the class instance of FileStorage"""
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """removing the storage file."""
        os.remove(cls.storage._FileStorage__file_path)

    @classmethod
    def setUp(self):
        """setting up the objects."""
        self.storage._FileStorage__objects = {}

    def test_attributes(self):
        """Tests for FileStorage's attributes"""
        self.assertEqual(self.storage._FileStorage__file_path, 'file.json')
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        """Tests for FIleStorage's all method."""
        my_dict = self.storage.all()
        objects = self.storage._FileStorage__objects
        self.assertIsInstance(my_dict, dict)
        self.assertEqual(my_dict, objects)

    def test_new(self):
        """Tests for the new method of FileStorage."""
        obj = BaseModel()
        pref = f'{obj.__class__.__name__}.{obj.id}'
        self.storage.reload()
        self.assertIsInstance(obj, BaseModel)
        self.assertIn(pref, self.storage.all().keys())

    def test_save(self):
        """Tests for the save method of FileStorage."""
        obj = BaseModel()
        pref = f'{obj.__class__.__name__}.{obj.id}'
        obj.name = "car"
        obj.save()
        self.storage.reload()
        my_dict = self.storage.all()
        self.assertTrue(my_dict[pref])

    def test_reload(self):
        """Tests for the reload method of FileStorage."""
        obj = BaseModel()
        obj.save()
        with open(self.storage._FileStorage__file_path, 'r') as my_file:
            my_dict = json.load(my_file)
        self.storage.reload()
        self.assertEqual(my_dict, self.storage.all())


if __name__ == '__main__':
    unittest.main()
