#!/usr/bin/python3
"""
    Flask route that returns json response
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.user import User


@app_views.route('/users/', methods=['GET', 'POST'])
def users_no_id(user_id=None):
    """
        just a discription
    """

    if request.method == 'GET':
        all_users = storage.all('User')
        all_users = [obj.to_dict() for obj in all_users.values()]
        return (all_users)
