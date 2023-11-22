#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import getenv


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'  # Table name

    name = Column(String(128), nullable=False)  # Column representing name

    cities = relationship("City", backref="state",
            cascade="all, delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ Getter attribute for cities """
            cities_list = []
            for city in list(models.storage.all("City").values()):
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
