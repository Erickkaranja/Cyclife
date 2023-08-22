#!/usr/bin/python3
"""instantiates cart class module."""

from models.base_model import BaseModel
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy.orm import relationship


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
