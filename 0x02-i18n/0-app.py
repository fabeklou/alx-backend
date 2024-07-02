#!/usr/bin/env python3

"""
This module contains a Flask application that renders a template.

Usage:
    - Run the application directly to start the Flask
        development server.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home() -> str:
    """
    Renders the '0-index.html' template with a title
    variable set to 'Hello world'.

    Returns:
        The rendered template.
    """
    title: str = 'Hello world'
    return render_template('0-index.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)
