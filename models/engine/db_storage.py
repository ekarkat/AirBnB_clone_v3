#!/usr/bin/python3
"""
Start link class to table in database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity
from sqlalchemy.orm import scoped_session
from os import getenv


class DBStorage():
    """Dbstorage Class"""
    __engine = None
    __session = None

    def __init__(self):
        """Init method"""

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""

        objs_dic = {}
        if not cls:
            result = self.__session.query(State).all()
            result.extend(self.__session.query(City).all())
            result.extend(self.__session.query(User).all())
            result.extend(self.__session.query(Place).all())
            result.extend(self.__session.query(Review).all())
            result.extend(self.__session.query(Amenity).all())
        else:
            result = self.__session.query(cls).all()

        for obj in result:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objs_dic[key] = obj

        return (objs_dic)

    def new(self, obj):
        """Add obj to database"""
        self.__session.add(obj)

    def save(self):
        """commit changes in database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def close(self):
        # close a session
        self.__session.close()
