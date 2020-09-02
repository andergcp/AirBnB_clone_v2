#!/usr/bin/python3
'''
starts a Flask web application
'''
from flask import Flask
from flask import abort
from flask import render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    '''
    return Python + text(optional)
    '''
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<n>', strict_slashes=False)
def is_num(n):
    '''
    return Python + text(optional)
    '''
    try:
        n = int(n)
        return '%d is a number' % n
    except Exception:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def is_num_template(n):
    '''
    return Python + text(optional)
    '''
    try:
        n = int(n)
        return render_template('5-number.html', n=n)
    except Exception:
        abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def num_even_or_odd(n):
    '''
    return Python + text(optional)
    '''
    try:
        n = int(n)
        e_or_o = 'even' if n % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html', n=n, e_or_o=e_or_o)
    except Exception:
        abort(404)


if __name__ == '__main__':
    '''
    runs the function
    '''
    app.run(host='0.0.0.0', port=5000)
