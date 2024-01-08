#!/usr/bin/python3
# api index
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status_api():
    # Json status
    return jsonify({"status": "OK"})
