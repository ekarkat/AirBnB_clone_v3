#!/usr/bin/python3
'''state API index'''
from api.v1.views import app_views
from flask import jsonify, url_for, redirect, abort, request
from models import storage
from models.city import City


methods_city = ['GET', 'POST']


@app_views.route('/states/<state_id>/cities', strict_slashes=False,
                 methods=methods_city)
def state_cities(state_id):
    # Retrieve a state cities
    state = storage.get('State', state_id)
    if not state:
        abort(404)

    if request.method == 'GET':
        city_list = []
        for city in state.cities:
            city_list.append(city.to_dict())
        return jsonify(city_list)
    elif request.method == 'POST':
        data_json = request.get_json(force=True, silent=True)
        if not data_json:
            abort(400, "Not a JSON")
        if "name" not in data_json:
            abort(400, "Missing name")
        data_json["state_id"] = state_id
        new_city = City(**data_json)
        new_city.save()
        return jsonify(new_city.to_dict()), 201


methods_city_id = ['GET', 'PUT', 'DELETE']


@app_views.route('/cities/<city_id>', strict_slashes=False,
                 methods=methods_city_id)
def city_id(city_id):
    # city route
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    if request.method == 'GET':
        return jsonify(city.to_dict())

    elif request.method == 'DELETE':
        storage.delete(city)
        storage.save()
        return jsonify({}), 200

    elif request.method == 'PUT':
        json_data = request.get_json(force=True, silent=True)
        if not json_data:
            abort(400, "Not a JSON")
        for key, value in json_data.items():
            if key == 'id' or key == 'created_at'\
                    or key == 'updated_at':
                continue
            else:
                city.__dict__[key] = value
        city.save()
        return jsonify(city.to_dict()), 200
