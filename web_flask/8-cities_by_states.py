#!/usr/bin/python3
"""Model 8"""
from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(error=None):
    # close session after every request
    storage.close()


@app.route("/cities_by_states/", strict_slashes=False)
def cities_by_states():
    # Return state and cities
    result_s = storage.all(State)
    sorted_s = dict(sorted(result_s.items(), key=lambda item: item[1].name))
    return render_template("8-cities_by_states.html", states=sorted_s)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
