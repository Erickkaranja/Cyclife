#!/usr/bin/python3
"""implementation of different end points for our order object."""

from flask import abort, jsonify, make_response, request

from api.v1.views import app_views
from models import storage
from models.bicycle import Bicycle
from models.user import User
from models.order import Orders


@app_views.route(
    "/user/<user_id>/order", methods=["GET"], strict_slashes=False
)
def user_orders(user_id):
    """http endpoint that gets user's orders."""
    obj_user = storage.get(User, user_id)
    if obj_user is None:
        abort(404)
    return jsonify([order.to_dict() for order in obj_user.orders])


@app_views.route("/order/<order_id>", methods=["GET"], strict_slashes=False)
def get_order(order_id):
    """http endpoint that gets an order by id."""
    obj_order = storage.get(Orders, order_id)
    if obj_order is None:
        abort(404)
    return jsonify(obj_order.to_dict())


@app_views.route(
    "/user/<user_id>/order", methods=["POST"], strict_slashes=False
)
def post_order(user_id):
    """http endpoint that creates an order from a given user."""
    obj_user = storage.get(User, user_id)
    if obj_user is None:
        abort(404)

    req_json = request.get_json()
    if req_json.get("order_status") is None:
        abort(400, "Missing status")
    if req_json.get("total_price") is None:
        abort(400, "missing price")
    if req_json.get("bicycle_id") is None:
        abort(400, "missing bicycle item.")
    req_json["user_id"] = user_id
    bicycle_id = req_json.get("bicycle_id")
    bicycle_id = storage.get(Bicycle, bicycle_id)
    if bicycle_id is None:
        abort(404)

    new_order = Order()
    for k, v in req_json.items():
        if k not in ["id", "created_at", "updated_at"]:
            setattr(new_order, k, v)
    storage.new(new_order)
    storage.save()
    return make_response(jsonify(new_order.to_dict()), 201)


@app_views.route("/order/<order_id>", methods=["PUT"], strict_slashes=False)
def update_order(order_id):
    """http endpoint that updates an order."""
    obj_order = storage.get(Order, order_id)
    if obj_order is None:
        abort(404)

    req_json = request.get_json()
    if req_json is None:
        abort(400, "Missing JSON")
    for k, v in req_json.items():
        if k not in ["id", "created_at", "updated_at", "user_id"]:
            setattr(obj_order, k, v)
    storage.save()
    return make_response(jsonify(obj_order.to_dict()), 200)


@app_views.route(
    "/order/<order_id>", methods=["DELETE"], strict_slashes=False
)
def delete_order(order_id):
    """http endpoint that delete's order by id."""
    obj_order = storage.get(Order, order_id)
    if obj_order is None:
        abort(404)
    obj_order.delete()
    storage.save()
    return make_response(jsonify({}), 200)
