#!/usr/bin/python3
"""Module containing class Review"""
from models.base_model import BaseModel
from models.place import Place
from models.User import User


class Review(BaseModel):
    """class Review definition"""

    place_id = ''
    user_id = ''
    text = ''
