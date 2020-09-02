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


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """Displays states from storage and template"""
    states = [state for key, state in storage.all(State).items()]
    cities = []
    for state in states:
        if environ.get('HBNB_TYPE_STORAGE') == 'db':
            cities += state.cities
        else:
            cities += state.cities()

    return render_template('8-cities_by_states.html', states=states, cities=cities)


if __name__ == '__main__':
    '''
    runs the app
    '''
    app.run(host='0.0.0.0', port=5000)
