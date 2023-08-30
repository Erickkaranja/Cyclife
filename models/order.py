#!/usr/bin/python3
"""class order defination."""

from sqlalchemy import Column, Float, ForeignKey, String

from models.base_model import Base, BaseModel


class Order(BaseModel, Base):
    """instanciates class orders.
    Attributes:
        __tablename__(sqlalchemy object): represents sql class to be mapped
                      to.
        order_status(sqlalchemy string): represents an order's status.
        total_price(sqlalchemy Float): represent total price of orders.
        user_id(sqlalchemy string): represents a user's order.
        bicycle_id(sqlalchemy string): represents a user's bicycle order.
    """

    __tablename__ = "order"
    order_status = Column(String(60), nullable=False)
    total_price = Column(Float, default=0, nullable=False)
    user_id = Column(String(60), ForeignKey("user.id"), nullable=False)
    bicycle_id = Column(String(60), ForeignKey("bicycle.id"), nullable=False)
