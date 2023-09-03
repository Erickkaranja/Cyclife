#!/usr/bin/python3
"""implementation of user's endpoints.
   this include method POST, GET, PUT and DELETE.
"""

from flask import abort, jsonify, make_response, request

from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route("/user", methods=["GET"], strict_slashes=False)
def get_all_users():
    """http endpoint that returns all users in our database."""
    all_users = storage.all(User)
    if all_users is None:
        abort(404)
    return jsonify([user.to_dict() for user in all_users.values()])


@app_views.route("/user/<user_id>", methods=["GET"], strict_slashes=False)
def single_user(user_id):
    """Retrieves a User object"""
    obj = storage.get(User, user_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route("/user", methods=["POST"], strict_slashes=False)
def post_user():
    """http endpoint that create's a new user."""
    req_json = request.get_json()
    if req_json is None:
        abort(400, "Not a JSON")
    if req_json.get("email") is None:
        abort(400, "Missing email")
    if req_json.get("password") is None:
        abort(400, "missing password")

    new_user = User()
    for k, v in req_json.items():
        if k in ["email", "password", "first_name", "last_name"]:
            setattr(new_user, k, v)
    storage.new(new_user)
    storage.save()

    return make_response(jsonify(new_user.to_dict()), 201)


@app_views.route("/user/<user_id>", methods=["DELETE"], strict_slashes=False)
def delete_user(user_id):
    """http endpoint that delete's a user"""
    obj_user = storage.get(User, user_id)
    if obj_user is None:
        abort(404)
    obj_user.delete()
    storage.save()
    return jsonify({}, 200)


@app_views.route("/user/<user_id>", methods=["PUT"], strict_slashes=False)
def update_user(user_id):
    """http endpoint that update's a user endpoint."""
    obj_user = storage.get(User, user_id)
    if obj_user is None:
        abort(404)
    req_json = request.get_json()
    if req_json is None:
        abort(400, "Not a JSON")
    for k, v in req_json.items():
        if k not in ["id", "created_at", "updated_at"]:
            setattr(obj_user, k, v)
    storage.save()
    return make_response(jsonify(obj_user.to_dict()), 200)
