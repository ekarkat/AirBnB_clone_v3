#!/usr/bin/python3
"""TAsk 9 model"""

from flask import Flask, render_template
from models.state import State
from models.city import City
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(error=None):
    # Tear down process
    storage.close()


@app.route("/states/", strict_slashes=False)
@app.route('/states/<string:id>', strict_slashes=False)
def staes_cities_id(id=""):
    # return state template with dump direct uncreative way

    if not id:
        states = storage.all(State)
        sorted_s = dict(sorted(states.items(), key=lambda item: item[1].name))
        return render_template("9-states.html", states=sorted_s, id_value=0)
    states = storage.all(State)
    key_id = "State.{}".format(id)
    if key_id in states:
        the_state = states[key_id]
        return render_template("9-states.html", states=the_state, id_value=1)
    else:
        return render_template("9-states.html", id_value=-1)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
