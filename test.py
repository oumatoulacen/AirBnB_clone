#!/usr/bin/python3
'''only tests'''

from models.base_model import BaseModel


m = BaseModel()

print(type(m.id) == str)
