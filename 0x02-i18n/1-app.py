#!/usr/bin/env python3

"""
This module contains a Flask application that renders a template.

Usage:
    - Run the application directly to start the Flask
        development server.
"""

from typing import List
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for the application.

    Attributes:
        LANGUAGES (List[str]): List of supported languages.
        DEFAULT_LOCALE (str): Default locale for the application.
        DEFAULT_TIMEZONE (str): Default timezone for the application.
    """

    LANGUAGES: List[str] = ['en', 'fr']
    DEFAULT_LOCALE: str = 'en'
    DEFAULT_TIMEZONE: str = 'UTC'


app.config.from_object(Config)


@app.route('/')
def home() -> str:
    """
    Renders the '0-index.html' template with a title
    variable set to 'Hello world'.

    Returns:
        The rendered template.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
