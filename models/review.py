#!/usr/bin/python3
"""defines reviews class."""

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ForeignKey


class Review(BaseModel, Base):
    """instantiating class order.
       Attributes:
           __tablename__:
           user_id(sqlalchemy string): represents a user's id.
           bicycle_id(sqlalchemy string): represents bicycle's id being
                      reviewed.
           rating(sqlalchemy Integer): represents a bicycle review rating.
           text(sqlalchemy string): comments on product.
    """
    __tablename__ = "review"
    user_id = Column(String(60), ForeignKey("user.id"), nullable=False)
    bicycle_id = Column(String(60), ForeignKey("bicycle.id"), nullable=False)
    rating = Column(Integer, default=0, nullable=False)
    text = Column(String(1024))
