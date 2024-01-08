#!/usr/bin/python3
"""TAsk 9 model"""

from flask import Flask, render_template, url_for
from models.state import State
from models.city import City
from models.amenity import Amenity
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(error=None):
    # Tear down process
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    # return state template with dump direct uncreative way

    result_s = storage.all(State)
    result_a = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=result_s, amenities=result_a)


if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0", port=5000)
