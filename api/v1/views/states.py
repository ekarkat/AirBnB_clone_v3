#!/usr/bin/python3
'''state API index'''
from api.v1.views import app_views
from flask import jsonify, url_for, redirect, abort, request
from models import storage
from models.state import State


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

#     if request.method == 'POST':
#         data_json = request.get_json(force=True, silent=True)
#         if not data_json:
#             abort(400, "Not a JSON")
#         if "name" not in data_json:
#             abort(400, "Missing name")
#         new_state = State(**data_json)
#         new_state.save()
#         return jsonify(new_state.to_dict()), 201


# methods_state_id = ["GET", "DELETE", "PUT"]


# @app_views.route('/states/<state_id>', strict_slashes=False,
#                  methods=methods_state_id)
# def state_by_id(state_id):
#     # Retrieve a state
#     state = storage.get('State', state_id)
#     if not state:
#         abort(404)

#     if request.method == 'GET':
#         return jsonify(state.to_dict())

#     elif request.method == 'DELETE':
#         # Delete a state
#         storage.delete(state)
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
#                 setattr(state, key, value)
#         state.save()
#         return jsonify(state.to_dict()), 200
