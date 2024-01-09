#!/usr/bin/python3
"""
    Flask route that returns json response
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.user import User


method = ['PUT', 'GET', 'POST', 'DELETE']



@app_views.route('/users/', strict_slashes=False, methods=method)
def user_api():
    """ just a discription"""
    if request.method == 'GET':
        user = storage.all('User')
        user_to_list = []
        for key, value in user.items():
            user_to_list.append(value.to_dict())
        return jsonify(user_to_list)

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
#     """ just a discription"""
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
#                 state.__dict__[key] = value
#         state.save()
#         return jsonify(state.to_dict()), 200
