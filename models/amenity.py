#!/usr/bin/python3
'''amenity class module'''

from models import storage
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''amenity class'''

    name = ""
