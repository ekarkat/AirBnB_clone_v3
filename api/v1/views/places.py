#!/usr/bin/python3
"""
    Flask route that returns json response
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.place import Place


method = ['PUT', 'GET', 'POST', 'DELETE']


@app_views.route('/cities/<city_id>/places', strict_slashes=False,
                 methods=method)
def place_api(city_id):
    """ just a discription"""
    if request.method == 'GET':
        city = storage.get('City', city_id)
        place_list = []
        for place in city.places:
            place_list.append(place.to_dict())
        return jsonify(place_list)

    if request.method == 'POST':
        city = storage.get('City', city_id)
        if city is None:
            abort(404)
        data = request.get_json(force=True, silent=True)
        if not data:
            abort(400, "Not a JSON")
        if "user_id" not in data:
            abort(400, "Missing user_id")
        user = storage.get(User, data["user_id"])
        if not user:
            abort(404)
        if "name" not in data:
            abort(400, "Missing name")
        place = Place(city_id=city.id, **data)
        place.save()
        return jsonify(place.to_dict()), 201


@app_views.route('/places/<place_id>', strict_slashes=False,
                 methods=method)
def place_by_id(place_id):
    """ just a discription"""
    place = storage.get('Place', place_id)
    if not place:
        abort(404)

    if request.method == 'GET':
        return jsonify(place.to_dict())

    elif request.method == 'DELETE':
        # Delete a state
        storage.delete(place)
        storage.save()
        return jsonify({}), 200

    elif request.method == 'PUT':
        json_data = request.get_json(force=True, silent=True)
        if not json_data:
            abort(400, "Not a JSON")
        for key, value in json_data.items():
            if key == 'id' or key == 'created_at' or key == 'city_id'\
                    or key == 'updated_at' or key == 'user_id':
                continue
            else:
                setattr(place, key, value)
        place.save()
        return jsonify(place.to_dict()), 200
