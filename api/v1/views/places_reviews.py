#!/usr/bin/python3
"""
    Flask route that returns json response
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.review import Review


method = ['PUT', 'GET', 'POST', 'DELETE']


@app_views.route('/places/<place_id>/reviews', strict_slashes=False,
                 methods=method)
def review_api(place_id):
    """ just a discription"""
    if request.method == 'GET':
        review = storage.get('Place', place_id)
        if review is None:
            abort(404)
        review_list = []
        reviews = review.reviews
        for review in reviews:
            review_list.append(review.to_dict())
        return jsonify(review_list)

    # if request.method == 'POST':
    #     review = storage.get('City', city_id)
    #     if review is None:
    #         abort(404)
    #     data = request.get_json(force=True, silent=True)
    #     if not data:
    #         abort(400, "Not a JSON")
    #     if "user_id" not in data:
    #         abort(400, "Missing user_id")
    #     user = storage.get(User, data["user_id"])
    #     if not user:
    #         abort(404)
    #     if "name" not in data:
    #         abort(400, "Missing name")
    #     review = Place(city_id=review.id, **data)
    #     review.save()
    #     return jsonify(review.to_dict()), 201


@app_views.route('/reviews/<review_id>', strict_slashes=False,
                 methods=method)
def review_by_id(review_id):
    """ just a discription"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)

    if request.method == 'GET':
        return jsonify(review.to_dict())

    elif request.method == 'DELETE':
        # Delete a state
        storage.delete(review)
        storage.save()
        return jsonify({}), 200

    elif request.method == 'PUT':
        json_data = request.get_json(force=True, silent=True)
        if not json_data:
            abort(400, "Not a JSON")
        for key, value in json_data.items():
            if key == 'id' or key == 'created_at' or key == 'place_id'\
                    or key == 'updated_at' or key == 'user_id':
                continue
            else:
                setattr(review, key, value)
        review.save()
        return jsonify(review.to_dict()), 200
