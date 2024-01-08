from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return ("Hello HbNB!")

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return ("HBNB")

@app.route("/c/<text>", strict_slashes=False)
def cc(text):
    return ("C {}".format(text.replace("_", ' ')))

@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    return("Python {}".format(text.replace('_', ' ')))


@app.route("/number/<int:n>", strict_slashes=False)
def numb(n):
    return ("{} is a number".format(n))






app.run(debug=True, host="0.0.0.0", port=5000)