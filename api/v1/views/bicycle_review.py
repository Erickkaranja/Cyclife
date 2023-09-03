#!/usr/bin/python3
"""create's reviews http endpoints.
   GET, PUT, POST, DELETE.
"""

from flask import abort, jsonify, make_response, request

from api.v1.views import app_views
from models import storage
from models.bicycle import Bicycle
from models.review import Review
from models.user import User


@app_views.route(
    "/bicycle/<bicycle_id>/review", methods=["GET"], strict_slashes=False
)
def get_bicycle_review(bicycle_id):
    """http endpoint that returns reviews to a given bicycle."""
    obj_bicycle = storage.get(Bicycle, bicycle_id)
    if obj_bicycle is None:
        abort(404)
    return jsonify([review.to_dict() for review in obj_bicycle.reviews])


@app_views.route(
    "/bicycle/<bicycle_id>/review", methods=["POST"], strict_slashes=False
)
def post_review(bicycle_id):
    """http endpoint that creates a review to a given bicycle."""
    obj_bicycle = storage.get(Bicycle, bicycle_id)
    if obj_bicycle is None:
        abort(404)

    req_json = request.get_json()
    if req_json.get("user_id") is None:
        abort(400, "Missing user")
    if req_json.get("rating") is None:
        abort(400, "missing rating")
    if req_json.get("text") is None:
        abort(400, "missing text")

    user_id = req_json.get("user_id")
    user_id = storage.get(User, user_id)
    if user_id is None:
        abort(404)

    new_review = Review()
    for k, v in req_json.items():
        if k not in ["id", "created_at", "updated_at"]:
            setattr(new_review, k, v)
    storage.new(new_review)
    storage.save()
    return make_response(jsonify(new_review.to_dict()), 201)


@app_views.route("/review/<review_id>", methods=["GET"], strict_slashes=False)
def get_review(review_id):
    """http endpoint that returns review by id."""
    obj_review = storage.get(Review, review_id)
    if obj_review is None:
        abort(404)
    return jsonify(obj_review.to_dict())


@app_views.route("/review/<review_id>", methods=["PUT"], strict_slashes=False)
def update_review(review_id):
    """http endpoint that updates a review."""
    obj_review = storage.get(Review, review_id)
    if obj_review is None:
        abort(404)

    req_json = request.get_json()
    if req_json is None:
        abort(400, "Missing JSON")
    for k, v in req_json.items():
        if k not in ["id", "created_at", "updated_at", "bicycle_id"]:
            setattr(obj_review, k, v)
    storage.save()
    return make_response(jsonify(obj_review.to_dict()), 200)


@app_views.route(
    "/review/<review_id>", methods=["DELETE"], strict_slashes=False
)
def delete_review(review_id):
    """http request endpoint that delete's a review by id."""
    obj_review = storage.get(Review, review_id)
    if obj_review is None:
        abort(404)
    obj_review.delete()
    storage.save()
    return make_response(jsonify({}), 200)
