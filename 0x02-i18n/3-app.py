#!/usr/bin/env python3

"""
This module contains a Flask application that renders a template.

Usage:
    - Run the application directly to start the Flask
        development server.
"""

from typing import List, Union
from flask import Flask, render_template
from flask_babel import Babel
from flask import request


class Config:
    """
    Configuration class for the application.

    Attributes:
        LANGUAGES (List[str]): List of supported languages.
        DEFAULT_LOCALE (str): Default locale for the application.
        DEFAULT_TIMEZONE (str): Default timezone for the application.
    """

    LANGUAGES: List[str] = ['en', 'fr']
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """
    Get the best matching locale based on the user's accepted languages.

    Returns:
        Union[str, None]: The best matching locale as a string,
            or None if no match is found.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home() -> str:
    """
    Renders the '0-index.html' template with a title
    variable set to 'Hello world'.

    Returns:
        The rendered template.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
