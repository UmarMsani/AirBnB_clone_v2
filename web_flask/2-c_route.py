#!/usr/bin/python3
"""
This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000.

Routes:
/: Displays “Hello HBNB!”
/hbnb: Displays “HBNB”
/c/<text>: Displays “C ” followed by the value of the text variable
(underscores replaced with spaces)
Uses the option strict_slashes=False in the route definitions.
"""

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!' when accessing the root route."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB' when accessing the /hbnb route."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Displays 'C ' followed by the value of the text variable."""
    text = escape(text).replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
