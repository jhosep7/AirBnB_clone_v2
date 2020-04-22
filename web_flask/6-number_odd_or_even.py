#!/usr/bin/python3
""" starts a Flask web application2: """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def StartAPI():
    """ Start on port :5000 """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display /hbnb """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def CisFun(text):
    """ change _ for """
    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def PythonIsCool(text="is cool"):
    """ change _ for """
    return ("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def IfNumInt(n):
    """ Shows if num is int """
    return ("{:d} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def OddAndEven(n):
    """ Shows HTMl depending if even or odd """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
