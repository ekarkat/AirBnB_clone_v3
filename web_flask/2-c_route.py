#!/usr/bin/python3
"""Create a flask app"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """ Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays HBNB!"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return ("C {}".format(text))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
