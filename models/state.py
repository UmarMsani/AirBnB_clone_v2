#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete-orphan')

    else:
        name = ""

    @property
    def cities(self):
        """Getter attribute to retrieve cities for this state"""
        from models import storage
        city_instances = storage.all('City')
        return [city for city in city_instances.values() if city.state_id == self.id]
