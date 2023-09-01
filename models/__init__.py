#!/usr/bin/python3
'''a simple data storage abstraction.'''
from models.engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()
