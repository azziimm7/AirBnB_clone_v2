#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This MEthod  return hnbnb route"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """This function return c is fun + some text"""
    return 'C' + text.replace('_', '')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
