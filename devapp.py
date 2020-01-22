from flask import Flask, render_template
from xkcd import getLatestComic
from config import config_reader
import os

app = Flask(__name__)

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/xkcd')
def xkcd():
    latest = getLatestComic()
    img = latest.getImageLink()
    alt_text = latest.getAltText()
    return render_template('xkcd.html',img=img,alt_text=alt_text)


if __name__ == '__main__':
    app.run()
