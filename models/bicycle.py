#!/usr/bin/python3

"""instanciates Bicycle module."""

from sqlalchemy import Column, Float, String

from models.base_model import Base, BaseModel


class Bicycle(BaseModel, Base):
    """Bicycle class.
    Attributes:
        __tablename__: sql table.
        model(sqlalchemy string): model description of a bicycle.
        brand(sqlalchemy string): brand description of a bicycle.
        price(sqlalchemy int): unit price of a bicycle.
        description(sqlalchemy string): bicycle description.
        image(sqlalchemy string): a url representing the bicycle's image.
    """

    __tablename__ = "bicycle"
    model = Column(String(60), nullable=False)
    brand = Column(String(60), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(60), nullable=False)
    image = Column(Float, nullable=False)
