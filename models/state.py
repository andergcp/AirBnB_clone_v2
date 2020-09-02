#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref="state", cascade="all, delete")

    else:
        @property
        def cities(self):
            """Gets cities related to state"""
            # instance_list = []
            # for key, obj in models.storage.all().items():
            #     if obj.__class__.__name__ == 'City':
            #         if obj.state_id == self.id:
            #             instance_list.append(obj)
            # return instance_list
            return [city for key, city in models.storage.all(City).items()
                    if city.state_id == self.id]
