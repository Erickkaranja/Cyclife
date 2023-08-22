#!/usr/bin/python3
"""class user module."""

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """instantiating user class.
       Attributes:
           __tablename__(sqlalchemy object): represent sql table name to be
                         mapped to.
           email(sqlalchemy string): represents a users email.
           password(sqlalchemy string): represent users password(hashed).
           first_name(sqlalchemy string): user's first name.
           last_name(sqlalchemy string): user's last name.
           carts(sqlalchemy relationship): user's cart.
           orders(sqlalchemy relationship): user's order.
           reviews(sqlalchemy relationship): user's review.
    """

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    carts = relationship('cart', backref="user", cascade="delete")
    orders = relationship('order', backref="user", cascade="delete")
    reviews = relationship('review', backref="user", cascade="delete")
