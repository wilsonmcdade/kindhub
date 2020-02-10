"""
XKCD comic widget for Kindhub
Author: Wilson McDade
"""
import xkcd
from __main__ import app, enabled_widgets
from flask import render_template

@app.route('/comic')
def comic():
    if enabled_widgets['comic']['mode'] == "random":
        comic = xkcd.getRandomComic()
    elif enabled_widgets['comic']['mode'] == "latest":
        comic = xkcd.getLatestComic()
    img = comic.getImageLink()
    alt_text = comic.getAltText()
    return render_template('xkcd.html',widgets=enabled_widgets,img=img,alt_text=alt_text)
