#!/usr/bin/python
""" holds class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """Representation of User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
