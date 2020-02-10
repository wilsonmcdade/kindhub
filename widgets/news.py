"""
News Widget for Kindhub
Author: Wilson McDade
"""

from __main__ import app, enabled_widgets
from flask import render_template

@app.route('/news')
def news():
    return render_template('news.html',widgets=enabled_widgets)

