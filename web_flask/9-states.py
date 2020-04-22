#!/usr/bin/python3
""" intializing flask APP """
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.teardown_appcontext
def CloseDB(expt):
    """Close"""
    storage.close()


@app.route('/states', strict_slashes=False, defaults={'id': None})
@app.route('/states/<id>', strict_slashes=False)
def states(id):
    """Route /states"""
    state = states = None
    if id:
        states = storage.all(State)
        i = "State." + id
        if i in states:
            state = states[i]
        else:
            state = None
        states = []
    else:
        states = list(storage.all(State).values())
    return render_template('9-states.html', **locals())


if __name__ == '__main__':
    storage.reload()
    app.run(host="0.0.0.0", port=5000)
