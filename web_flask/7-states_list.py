#!/usr/bin/python3
'''
starts a Flask web application
'''
from flask import Flask
from flask import abort
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(a):
    """Closes storage session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays states from storage and template"""
    states = [state for key, state in storage.all(State).items()]
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    '''
    runs the app
    '''
    app.run(host='0.0.0.0', port=5000)
