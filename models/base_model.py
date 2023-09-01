#!/usr/bin/python3
"""This module defines the base class of Cyclife project.
   All model class will inherit from the base class.
"""

import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime

Base = declarative_base()


class BaseModel:
    """base class for all cyclife models.
       Attributes:
           id(sqlalchemy string): represents the model id.
           created_at(sqlalchemy datetime): represent model creation time.
           updated_at(sqlalchemy datetime): represent model update time.
    """
    id = Column(String(60), nullable=False, primary_key=True,
                default=str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """creating a new model instance."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)

    def save(self):
        """updates updated_at instance when changed."""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """converts class instances to dictionary format."""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at']=self.created_at.isoformat()
        dictionary['updated_at']=self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    def delete(self):
        """deletes the current instance from storage."""
        from models import storage
        storage.delete(self)
