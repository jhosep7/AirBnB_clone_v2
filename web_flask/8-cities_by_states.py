#!/usr/bin/python3
""" intializing flask APP """
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.teardown_appcontext
def CloseDB(expt):
    """Close"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states():
    """cities"""
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    storage.reload()
    app.run(host="0.0.0.0", port=5000)
