#!/usr/bin/python3
"""Create a flask app"""

from flask import Flask, render_template

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
    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    # Replace underscores with spaces
    return ("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def number_text(n):
    """Display number"""
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    # Render a template based on the variable n
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
