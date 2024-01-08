#!/usr/bin/python3
'''state API index'''
from api.v1.views import app_views
from flask import jsonify, url_for, redirect, abort, request
from models import storage
from models.amenity import Amenity


methods_am = ['GET', 'POST', 'DELETE', 'PUT']


@app_views.route("/amenities", strict_slashes=False, methods=methods_am)
def amenity_api():
    # get and post
    if request.method == 'GET':
        am_dict = []
        for key, value in storage.all(Amenity).items():
            am_dict.append(value.to_dict())
        return jsonify(am_dict)
    if request.method == 'POST':
        data_json = request.get_json(force=True, silent=True)
        if not data_json:
            abort(400, "Not a JSON")
        if "name" not in data_json:
            abort(400, "Missing name")
        new_amen = Amenity(**data_json)
        new_amen.save()
        return jsonify(new_amen.to_dict()), 201


@app_views.route("/amenities/<amenity_id>", strict_slashes=False,
                 methods=methods_am)
def amenities_by_id(amenity_id):
    amen = storage.get(Amenity, amenity_id)
    if not amen:
        abort(404)

    if request.method == 'GET':
        return jsonify(amen.to_dict())

    elif request.method == 'DELETE':
        storage.delete(amen)
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
                amen.__dict__[key] = value
        amen.save()
        return jsonify(amen.to_dict()), 200
