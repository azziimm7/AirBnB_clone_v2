#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String 
from sqlalchemy.orm import relationship
import os

Storage_type = os.environ.get('HBHBNB_TYPE_STORAGE')

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

@property
def cities(self):
    if storage_type != 'db':
        temp = models.storage.all()
        list_temp = []
        out = []
        for key in temp:
            cities = key.replace('.', ' ')
            city = shlex.split(city)
                if city[0] == 'City':
                    list_temp.append(temp[key])
        for i in list_temp:
            if i.state_id == self.id:
                out.append(i)
        return out
     else:
            return [city for city in self.cities]
