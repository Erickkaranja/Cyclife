#!/usr/bin/python3
"""instantiates cart class module."""

from sqlalchemy import Column, Float, ForeignKey, String

from models.base_model import Base, BaseModel


class Cart(BaseModel, Base):
    """class defination of cart object.
    Attributes:
        user_id(sqlalchemy string): associated user id.
        bicycle_id(sqlalchemy string): associated bicycle id.
        quantity (sqlalchemy float): total cart price items.
    """

    __tablename__ = "cart"
    user_id = Column(String(60), ForeignKey("user.id"), nullable=False)
    bicycle_id = Column(String(60), ForeignKey("bicycle.id"), nullable=False)
    quantity = Column(Float, default=0)
