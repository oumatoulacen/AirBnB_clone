#!/usr/bin/python3
'''place class module'''

from models.base_model import BaseModel
'''modules to use'''


class Place(BaseModel):
    '''place clace'''

    city_id = ""
    user_id = ""
    name = ""
    desciption = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = []
