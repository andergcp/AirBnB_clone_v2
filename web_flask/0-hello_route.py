#!/usr/bin/python3
'''
starts a Flask web application
'''
from flask import Flask
app = Flask(__name__)


@app.route('/')
def starts_app():
    '''
    return value
    '''
    return 'Hello HBNB!'


if __name__ == '__main__':
    '''
    runs the function
    '''
    app.run(host='0.0.0.0', port=5000)