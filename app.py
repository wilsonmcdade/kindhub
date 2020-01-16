from flask import Flask
import xkcd

app = Flask(__name__)


@app.route('/')
def index():
    return xkcd.getLatestComic()


if __name__ == '__main__':
    ree = xkcd.getLatestComic()
    app.run()
