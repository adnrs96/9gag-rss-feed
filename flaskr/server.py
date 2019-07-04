from flask import Flask, render_template
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

feeds = [
    {
        "name": "9GAG - Awesome",
        "rss_link": "https://9gag-rss.com/api/rss/get?code=9GAGAwesome&format=2",
        "link": "/feed/1",
    },
    {
        "name": "9GAG - Comic",
        "rss_link": "https://9gag-rss.com/api/rss/get?code=9GAGComic&format=2",
        "link": "/feed/2",
    },
    {
        "name": "9GAG - Dark Humor",
        "rss_link": "https://9gag-rss.com/api/rss/get?code=9GAGDarkHumor&format=2",
        "link": "/feed/3",
    },
    {
        "name": "9GAG - Fresh",
        "rss_link": "https://9gag-rss.com/api/rss/get?code=9GAGFresh&format=2",
        "link": "/feed/4",
    },

]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', feeds=feeds)
