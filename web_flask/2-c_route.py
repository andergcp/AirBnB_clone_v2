#!/usr/bin/python3
'''
starts a Flask web application
'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def starts_app():
    '''
    return value
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_screen():
    '''
    return hbnb screen
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    '''
    return c + text
    '''
    return 'C %s' % text.replace('_', ' ')


if __name__ == '__main__':
    '''
    runs the function
    '''
    app.run(host='0.0.0.0', port=5000)
