#!/usr/bin/python3
"""User module inherits from the BaseModel"""
from models/base_model import BaseModel


class User(BaseModel):
    """User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
