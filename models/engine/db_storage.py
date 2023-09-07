#!/usr/bin/python3
"""creates a mysql database engine."""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.base_model import Base
from models.bicycle import Bicycle
from models.cart import Cart
from models.order import Orders
from models.review import Review
from models.user import User


class DBStorage:
    """instanciating class DBStorage.
    Attributes:
        engine(private class attribute)
        session(private class attribute)
    """

    __engine = None
    __session = None

    def __init__(self):
        """initializes class DBStorage constructor"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                os.getenv("CYCLIFE_MYSQL_USER"),
                os.getenv("CYCLIFE_MYSQL_PWD"),
                os.getenv("CYCLIFE_MYSQL_HOST"),
                os.getenv("CYCLIFE_MYSQL_DB"),
            ),
            pool_pre_ping=True,
            echo=True,  # debug purposes
        )
        # Drop database if on test environment
        if os.getenv("CYCLIFE_ENV", "") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """if cls is None returns all database objects else,
        returns cls objects set.
        """
        if cls is None:
            objs = self.__session.query(Bicycle).all()
            objs.extend(self.__session.query(Cart).all())
            objs.extend(self.__session.query(Orders).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(User).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {
            "{}.{}".format(type(obj).__name__, obj.id): obj for obj in objs
        }

    def new(self, obj):
        """creates a new object in the current session."""
        self.__session.add(obj)

    def save(self):
        """saves objects in the current session."""
        try:
            self.__session.commit()
        except Exception as e:
            print(e)
            self.__session.rollback()

    def reload(self):
        """create's all tables in the database and initializes a
        new session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def delete(self, obj=None):
        """deletes an object from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.close()

    def get(self, cls, id):
        """
        Retrieve a single object
        Arguments:
           cls: Class object
           id: String representing the object ID
        Returns:
           Object or None
        """
        objects = self.all(cls)
        if objects:
            return objects.get(f"{cls.__qualname__}.{id}", None)
