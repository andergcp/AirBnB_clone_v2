#!/usr/bin/python3
"""This module defines a class to manage db for hbnb AirBnb clone v2"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ
from models.state import State
from models.city import City
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in Databases"""
    __engine = None
    __session = None

    def __init__(self):
        user_db = environ.get('HBNB_MYSQL_USER')
        pass_db = environ.get('HBNB_MYSQL_PWD')
        host_db = environ.get('HBNB_MYSQL_HOST')
        _db = environ.get('HBNB_MYSQL_DB')

        self.__engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'
            .format(user_db, pass_db, host_db, _db), pool_pre_ping=True)

#        Session = sessionmaker(bind=self.__engine)
#        __session = Session()

        if environ.get('HBNB_ENV') == 'test':
#            result = session.query(State)
#            session.delete(result)
            Base.metada.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Return all objects"""
        my_dict = {}
        t = []
        if cls is not None:
            t = self.__session.query(cls).all()
        else:
            classes = [State, City, User, Place, Review, Amenity]
            for cl in classes:
                t.append(self.__session.query(cl).all())

            t = [x for y in t for x in y]

        for obj in t:
            my_dict['{}.{}'.format(obj.__class__.__name__, obj.id)] = obj

        return my_dict

    def new(self, obj):
        """add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create tables and current db session"""

        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine)
        Session = scoped_session(session_fact)
        self.__session = Session(expire_on_commit=False)
#        self.__session = sessionmaker(bind=self.__engine,expire_on_commit=False)
#        self.__session = self.__session()
#        Session = scoped_session(self.__session)
