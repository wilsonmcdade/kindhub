"""
gCal Widget for Kindhub
Author: Wilson McDade
"""

from __main__ import app, enabled_widgets
from flask import render_template, Blueprint

@app.route('/')
@app.route('/calendar')
def calendar():
    return render_template('calendar.html',widgets=enabled_widgets)
