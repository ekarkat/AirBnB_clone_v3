#!/usr/bin/python3
'''Flask web application API
'''
from os import getenv
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    return {"error": "Not found"}, 404


host = getenv('HBNB_API_HOST', '0.0.0.0')
port = getenv('HBNB_API_PORT', 5000)
if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True)
