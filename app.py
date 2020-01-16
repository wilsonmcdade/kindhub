from flask import Flask, render_template
from xkcd import getLatestComic
import os

app = Flask(__name__)
calendar = os.environ.get("calendar")

@app.route('/')
@app.route('/calendar')
def calendar():
    return render_template('calendar.html',calendar=calendar)

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
    app.run(ip="0.0.0.0",port="8080")
