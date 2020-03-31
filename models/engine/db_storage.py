#!/usr/bin/python3
"""Class that allows to connect with a Database
"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.place import Place
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """Class for database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes storage"""
        from models.base_model import Base
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

    def all(self, cls=None):
        """cls Obj"""
        from models.state import State
        from models.city import City
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_list = [
            State,
            City,
            User,
            Place,
            Review,
            Amenity
        ]
        Lines = []
        if cls:
            Lines = self.__session.query(cls)
        else:
            for cls in class_list:
                Lines += self.__session.query(cls)
        return {type(v).__name__ + "." + v.id: v for v in Lines}

    def new(self, obj):
        """Adding Obj to db"""
        if not obj:
            return
        self.__session.add(obj)

    def save(self):
        """save in db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """create tables"""
        from models.base_model import Base
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.user import User
        from models.review import Review
        from models.place import Place
        from sqlalchemy.orm import sessionmaker, scoped_session
        from os import getenv

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Sect1 = scoped_session(session_factory)
        self.__session = Sect1()

    def close(self):
        """Thread specific storage"""
        self.__session.close()