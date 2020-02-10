"""
Weather Widget for Kindhub
Author: Wilson McDade
"""

from __main__ import app, enabled_widgets
from flask import render_template
from geopy.geocoders import Nominatim

@app.route('/weather')
def weather():
    geolocator = Nominatim(user_agent="kindhub")
    given_loc = enabled_widgets['weather']['loc']
    if len(given_loc) > 1:
        location = geolocator.geocode(given_loc)
        long = location.longitude
        lat = location.latitude
        loc_coord = str(lat)[:7] + "," + str(long)[:7]
    return render_template('weather.html',widgets = enabled_widgets, loc = loc_coord, loc_name = given_loc)
