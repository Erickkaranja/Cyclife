#!/usr/bin/python3
"""class user module."""

from sqlalchemy import Column, String

from models.base_model import Base, BaseModel


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

    __tablename__ = "user"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
