#!/usr/bin/python3
"""script to start a flask app on localhost
"""
from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(exc=None):
    """called on teardown of app contexts,
        for more info on contexts visit
        -> http://flask.pocoo.org/docs/1.0/appcontext/

	Storage.close() closes the sql scoped session or reloads file
            storage.
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def conditional_templating(id=None):
    """checking input data using templating"""
    return render_template('10-hbnb_filters.html',
                           states=storage.all("State").values(),
                           amenities=storage.all("Amenity").values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
