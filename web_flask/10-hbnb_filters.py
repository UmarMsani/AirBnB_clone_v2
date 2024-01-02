#!/usr/bin/python3
"""Starts a Flask web application"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


"""Route to render the hbnb_filters page"""
@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


"""Teardown to remove the SQLAlchemy Session after each request"""
@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


"""Running the Flask app on 0.0.0.0 and port 5000"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
