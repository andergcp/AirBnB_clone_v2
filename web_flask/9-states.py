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


@app.route('/states', strict_slashes=False)
def states():
    """Displays states from storage and template"""
    states = [state for key, state in storage.all(State).items()]
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Displays states from storage and template by id"""
    state = [state for key, state in storage.all(
        State).items() if state.id == id]
    state = state[0] if len(state) > 0 else None
    cities = None
    if state:
        cities = []
        if environ.get('HBNB_TYPE_STORAGE') == 'db':
            cities += state.cities
        else:
            cities += state.cities()

    return render_template(
        '9-states.html', state=state, cities=cities)


if __name__ == '__main__':
    '''
    runs the app
    '''
    app.run(host='0.0.0.0', port=5000)
