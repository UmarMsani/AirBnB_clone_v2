#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import models
from os import getenv


class State(BaseModel):
    """ State class """
    __tablename__ = 'States'

    name = Column(String(128), nullable=False)

    cities = relationship(
            "City",
            backref="State",
            cascade="all, delete-orphan"
            )

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ Getter attribute for cities """
            cities_list = []
            for city in list(models.storage.all("City").values()):
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
