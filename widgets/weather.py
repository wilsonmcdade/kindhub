"""
Weather Widget for Kindhub
Author: Wilson McDade
"""

from __main__ import app, enabled_widgets
from flask import render_template

@app.route('/weather')
def weather():
    return render_template('weather.html',widgets = enabled_widgets)
