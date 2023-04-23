#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Greetings, hbnb project"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text_c(text):
    """Displays 'C' followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return "C {}".format(escape(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
