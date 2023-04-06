#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import Basemodel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
#from models.place import place_amenity


class Amenity(BaseModel, Base):
    """ class Amenity Atributors:
        name: number of entries
    """
    _tablename_ = 'amenities'
    name = Column(String(128), nullable=False)
    #place_amenities = relationships('Place', secondary='place_amenity')
