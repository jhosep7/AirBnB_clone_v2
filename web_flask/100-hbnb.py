#!/usr/bin/python3
""" intializing flask APP """
from flask import Flask, render_template
from models import storage, State, Amenity, Place
app = Flask(__name__)


@app.teardown_appcontext
def CloseDB(expt):
    """Close"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def Filter():
    """ Filters """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template('100-hbnb.html', **locals())


if __name__ == '__main__':
    storage.reload()
    app.run(host="0.0.0.0", port=5000)
