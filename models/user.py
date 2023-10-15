#!/usr/bin/bash
"""module containing class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User definition that inherits from BaseModel."""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
