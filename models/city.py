#!/usr/bin/python3
'''city class module'''

from models import storage
from models.base_model import BaseModel


class City(BaseModel):
    '''city class indicates city'''

    state_id = ""
    name = ""
