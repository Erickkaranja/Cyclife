#!/usr/bin/python3
"""
Flask route that handles bicycle endpoints, implements GET, POST, DELETE and
PUT requests.
"""
from flask import abort, jsonify, make_response, request

from api.v1.views import app_views
from models import storage
from models.bicycle import Bicycle


@app_views.route("/bicycle", methods=["GET"], strict_slashes=False)
def get_all_bicycles():
    """http endpoint that returns all bicycles on query."""
    all_bicycles = storage.all(Bicycle)
    return jsonify([bicycle.to_dict() for bicycle in all_bicycles.values()])


@app_views.route(
    "/bicycle/<bicycle_id>", methods=["GET"], strict_slashes=False
)
def get_bicycle_by_id(bicycle_id):
    """http endpoint that returns a bicycle by its id."""
    obj_bicycle = storage.get(Bicycle, bicycle_id)
    if obj_bicycle is None:
        abort(404)
    return jsonify(obj_bicycle.to_dict())


@app_views.route("/bicycle", methods=["POST"], strict_slashes=False)
def post_bicycle():
    """http endpoint that add's a new bicycle entity."""
    req_json = request.get_json()
    if req_json is None:
        abort(400, "Not a JSON")
    if req_json.get("model") is None:
        abort(400, "missing model")
    if req_json.get("brand") is None:
        abort(400, "missing brand")
    if req_json.get("price") is None:
        abort(400, "missing price")
    if req_json.get("description") is None:
        abort(400, "missing description")
    if req_json.get("image") is None:
        abort(400, "missing image")

    new_obj = Bicycle()
    for k, v in req_json.items():
        if k in ["model", "brand", "price", "description", "image"]:
            setattr(new_obj, k, v)
    storage.new(new_obj)
    storage.save()

    return make_response(jsonify(new_obj.to_dict()), 201)


@app_views.route(
    "/bicycle/<bicycle_id>", methods=["DELETE"], strict_slashes=False
)
def delete_bicycle(bicycle_id):
    """http endpoint that delete's bicycle by id."""
    obj_bicycle = storage.get(Bicycle, bicycle_id)
    if obj_bicycle is None:
        abort(404)
    obj_bicycle.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route(
    "/bicycle/<bicycle_id>", methods=["PUT"], strict_slashes=False
)
def update_bicycle(bicycle_id):
    """http endpoint that update's bicycle object."""
    obj_bicycle = storage.get(Bicycle, bicycle_id)
    if obj_bicycle is None:
        abort(400, "Not a JSON")

    req_json = request.get_json()
    if req_json is None:
        abort(404)

    for k, v in req_json.items():
        if k not in ["created_at", "updated_at", "id"]:
            setattr(obj_bicycle, k, v)
    storage.save()
    return make_response(jsonify(obj_bicycle.to_dict()), 200)
