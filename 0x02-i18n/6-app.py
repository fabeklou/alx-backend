#!/usr/bin/env python3

"""
This module contains a Flask application that renders a template.

Usage:
    - Run the application directly to start the Flask
        development server.
"""

from typing import List, Dict, Union
from flask import Flask, render_template, g
from flask_babel import Babel
from flask import request


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user(user_id: int) -> Union[Dict, None]:
    """
    Retrieve a user from the users dictionary based on the given user_id.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        Union[Dict, None]: The user dictionary if found, None otherwise.
    """
    return users.get(user_id, None)


@app.before_request
def before_request():
    """
    Function that is executed before each request.

    It retrieves the 'login_as' parameter from the request arguments and
    uses it to get the corresponding user using the 'get_user' function.
    The retrieved user is then stored in the global 'g' object as 'user'.

    Parameters:
        None

    Returns:
        None
    """
    user = request.args.get('login_as')
    if user:
        user = get_user(int(user))
    g.user = user


@babel.localeselector
def get_locale() -> Union[str, None]:
    """
    Get the preferred locale from the request arguments
    or the accept languages header.

    Returns:
        Union[str, None]: The preferred locale if it is valid,
            otherwise None.
    """
    # Locale from URL parameters
    lokl = dict(request.args).get('locale', None)
    if lokl in app.config['LANGUAGES']:
        return lokl

    # Locale from user settings
    if g.user:
        lokl = g.user.get('locale', None)
        if lokl in app.config['LANGUAGES']:
            return lokl
    
    # Locale from request header
    lokl = request.headers.get('locale', None)
    if lokl in app.config['LANGUAGES']:
        return lokl

    # return default
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home() -> str:
    """
    Renders the '0-index.html' template with a title
    variable set to 'Hello world'.

    Returns:
        The rendered template.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
