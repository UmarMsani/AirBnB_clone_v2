#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'  # Table name

    name = Column(String(128), nullable=False)  # Column representing name
    state_id = Column(String(60),
                      ForeignKey('states.id', ondelete='CASCADE'),
                      nullable=False)  # Foreign key to states.id
    state = relationship("State", back_populates="cities")
