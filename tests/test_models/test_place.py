#!/usr/bin/python3
import sys
import os
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place

""" Test case for Place """


class TestPlace(unittest.TestCase):
    """ Test case for Place """

    def test_init(self):
        """ Test case for class Place __init__ method"""
        obj = Place()
        my_dict = obj.to_dict()
        new_model = Place(**my_dict)
        self.assertIsInstance(obj, Place, msg=None)
        self.assertIsInstance(obj.id, str, msg=None)
        self.assertIsInstance(obj.created_at, datetime, msg=None)
        self.assertIsInstance(obj.updated_at, datetime, msg=None)
        self.assertEqual(obj.id, new_model.id)
        self.assertFalse(obj is new_model)

    def test_attributes(self):
        """Test for attributes"""
        obj = Place()
        self.assertEqual(obj.city_id, '')
        self.assertEqual(obj.user_id, '')
        self.assertEqual(obj.name, '')
        self.assertEqual(obj.description, '')
        self.assertEqual(obj.number_rooms, 0)
        self.assertEqual(obj.number_bathrooms, 0)
        self.assertEqual(obj.max_guest, 0)
        self.assertEqual(obj.price_by_night, 0.0)
        self.assertEqual(obj.latitude, 0.0)
        self.assertEqual(obj.longitude, 0.0)
        self.assertEqual(obj.amenity_id, [])

    def test_save(self):
        """ Test case for Place save method """
        obj = Place()
        original_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(original_updated_at, obj.updated_at, msg=None)

    def test_to_dict(self):
        """ Test case for Place to_dict method """
        obj = Place()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict, msg=None)
        self.assertIn('__class__', obj_dict, msg=None)
        self.assertEqual(obj_dict['__class__'], 'Place', msg=None)
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_str(self):
        """Test the __str__ method of Place."""
        obj = Place()
        my_str = str(obj)
        my_test = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
        self.assertEqual(my_str, my_test)


if __name__ == '__main__':
    unittest.main()
