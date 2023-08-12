#!/usr/bin/python3
'''the review class module'''

from models import storage
from models.base_model import BaseModel


class Review(BaseModel):
    '''rewview class'''

    place_id = ""
    user_id = ""
    text = ""
