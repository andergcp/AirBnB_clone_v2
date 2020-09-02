#!/usr/bin/python3
'''
starts a Flask web application
For displaying cities by state
'''
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from os import environ
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(a):
    """Closes storage session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def search_list():
    """Displays states from storage and template"""
    states = [state for key, state in storage.all(State).items()]
    cities = []
    amenities = [amenity for key, amenity in storage.all(Amenities).items()]
    for state in states:
        cities += state.cities()

    return render_template(
        '10-hbnb_filters.html', states=states,
        cities=cities, amenities=amenities)


if __name__ == '__main__':
    '''
    runs the app
    '''
    app.run(host='0.0.0.0', port=5000)
