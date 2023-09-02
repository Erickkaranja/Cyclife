#!/usr/bin/python3

from flask import Blueprint
'''contains blueprints to our application and all imports to our objects.'''
app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')

from api.v1.views.bicycles import *
from api.v1.views.users import *
from api.v1.views.bicycle_review import *
from api.v1.views.orders import *
