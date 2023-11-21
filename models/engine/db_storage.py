#!/usr/bin/python3
"""storage engineModule to create a mysql engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base, BaseModel

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        pass  """ Implement this method to query objects from the database """

    def new(self, obj):
        pass  """ Implement this method to add an object to the session """

    def save(self):
        pass  """ Implement this method to commit changes to the session """

    def delete(self, obj=None):
        pass  """ Implement this method to delete an object from the session """

    def reload(self):
        pass  """ Implement this method to create tables and the session """
