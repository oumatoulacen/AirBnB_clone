#!/usr/bin/python3
'''amenity class module'''

from models import storage
from models.base_model import BaseModel
'''modules to use'''


class Amenity(BaseModel):
    '''amenity class'''

    name = ""
