from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.bicycle_review import *
from api.v1.views.bicycles import *
from api.v1.views.carts import *
from api.v1.views.index import *
from api.v1.views.orders import *
from api.v1.views.users import *
