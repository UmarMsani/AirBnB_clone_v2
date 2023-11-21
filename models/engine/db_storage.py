#!/usr/bin/python3
"""storage engineModule to create a mysql engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    __engine = None
    __session = None

    all_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}

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
        """Implement this method to query objects from the database"""
        obj_dict = {}
        cls = self.all_classes[cls]
        if cls is not None:
            objects = self.__session.query(cls).all()
        else:
            objects = self.__session.query(
                State, City, User, Amenity, Place, Review)
        for obj in objects:
            key = obj.__class__.__name__ + '.' + obj.id
            value = obj
            obj_dict[key] = value
        return obj_dict

    def new(self, obj):
        """Implement this method to add an object to the session"""
        self.__session.add(obj)
        self.__session.flush()

    def save(self):
        """Implement this method to commit changes to the session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Implement this method to delete an object from the session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Implement this method to create tables and the session"""
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call close on private session"""
        self.__session.close()
