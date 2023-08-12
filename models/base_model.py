#!/usr/bin/python3
'''base module module'''
from datetime import datetime
import uuid
from models import storage
'''datetime and uuid modules'''


class BaseModel():
    '''the base class of all clases'''

    def __init__(self, *args, **kwargs):
        '''method to instantiate an instance'''

        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''prints and returns a represtentation string of the class'''

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''updates the public instance attribute updated_at'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of
        __dict__ of the instance'''

        dict_obj = {}
        dict_obj["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                dict_obj[k] = v.isoformat()
            else:
                dict_obj[k] = v

        return dict_obj
