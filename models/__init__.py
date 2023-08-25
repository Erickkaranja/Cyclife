#!/usr/bin/python3
"""a simple abstraction of db_storage."""

from models.engine.db_storage import DBStorage
storage = DBStorage()
storage = storage.reload()
