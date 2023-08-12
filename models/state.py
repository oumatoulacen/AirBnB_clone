#!/usr/bin/python3
'''state class model'''

from models import storage
from models.base_model import BaseModel


class State(BaseModel):
    '''state class indicates the state'''

    name = ""
