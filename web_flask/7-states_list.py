#!/usr/bin/python3
"""Starts a Flask web application that listens on 0.0.0.0, port 5000"""

from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DB"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """To remove current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
