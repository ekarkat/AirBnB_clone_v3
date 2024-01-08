#!/usr/bin/pyhon3
'''the blueprint for the API.'''
from flask import Flask, Blueprint
from flask import jsonify, url_for, redirect, abort, request
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.review import Review

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
# from api.v1.views.states import *
# from api.v1.views.cities import *
# from api.v1.views.amenities import *

""" Methods for state """
methods_state = ["GET", "POST"]


@app_views.route('/states/', strict_slashes=False, methods=methods_state)
def state_api():
    """ just a discription"""
    if request.method == 'GET':
        states = storage.all('State')
        states_to_dict_list = []
        for key, value in states.items():
            states_to_dict_list.append(value.to_dict())
        return jsonify(states_to_dict_list)

    if request.method == 'POST':
        data_json = request.get_json(force=True, silent=True)
        if not data_json:
            abort(400, "Not a JSON")
        if "name" not in data_json:
            abort(400, "Missing name")
        new_state = State(**data_json)
        new_state.save()
        return jsonify(new_state.to_dict()), 201


methods_state_id = ["GET", "DELETE", "PUT"]


@app_views.route('/states/<state_id>', strict_slashes=False,
                 methods=methods_state_id)
def state_by_id(state_id):
    # Retrieve a state
    state = storage.get('State', state_id)
    if not state:
        abort(404)

    if request.method == 'GET':
        return jsonify(state.to_dict())

    elif request.method == 'DELETE':
        # Delete a state
        storage.delete(state)
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
                state.__dict__[key] = value
        state.save()
        return jsonify(state.to_dict()), 200


""" Methods for cities """

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
        new_city = City(**data_json, state_id=state_id)
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


# """ Methods for amen """


# methods_am = ['GET', 'POST', 'DELETE', 'PUT']


# @app_views.route("/amenities", strict_slashes=False, methods=methods_am)
# def amenity_api():
#     # get and post
#     if request.method == 'GET':
#         am_dict = []
#         for key, value in storage.all(Amenity).items():
#             am_dict.append(value.to_dict())
#         return jsonify(am_dict)
#     if request.method == 'POST':
#         data_json = request.get_json(force=True, silent=True)
#         if not data_json:
#             abort(400, "Not a JSON")
#         if "name" not in data_json:
#             abort(400, "Missing name")
#         new_amen = Amenity(**data_json)
#         new_amen.save()
#         return jsonify(new_amen.to_dict()), 201


# @app_views.route("/amenities/<amenity_id>", strict_slashes=False,
#                  methods=methods_am)
# def amenities_by_id(amenity_id):
#     amen = storage.get(Amenity, amenity_id)
#     if not amen:
#         abort(404)

#     if request.method == 'GET':
#         return jsonify(amen.to_dict())

#     elif request.method == 'DELETE':
#         storage.delete(amen)
#         storage.save()
#         return jsonify({}), 200

#     elif request.method == 'PUT':
#         json_data = request.get_json(force=True, silent=True)
#         if not json_data:
#             abort(400, "Not a JSON")
#         for key, value in json_data.items():
#             if key == 'id' or key == 'created_at'\
#                     or key == 'updated_at':
#                 continue
#             else:
#                 amen.__dict__[key] = value
#         amen.save()
#         return jsonify(amen.to_dict()), 200
