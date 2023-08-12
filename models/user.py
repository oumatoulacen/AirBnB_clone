#!/usr/bin/python3
''' the user class module'''
from models import storage
from models.base_model import BaseModel


class User(BaseModel):
    '''user class'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
