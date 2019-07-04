from werkzeug.contrib.cache import SimpleCache
from flask import Flask, render_template, abort
from flaskr.feed_list import feeds
from flaskr.fetch import fetch_feed_and_parse
import logging

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
rss_template_cache = SimpleCache()

def get_rendered_template_for_feed(feed_id):
    template = rss_template_cache.get(feed_id)
    if template is None:
        data = fetch_feed_and_parse(feeds[feed_id]['rss_link'])
        if data is None:
            logging.error('Cannot render template for feed', feed_id)
            return abort(500)

        feed_ctx = {
            "name": data.feed.title,
            "link": data.feed.link,
            "items": data.entries,
        }
        template = render_template("feed.html", **feed_ctx)
        rss_template_cache.set(feed_id, template, timeout=2*60)
    return template

@app.route('/', methods=['GET'])
def index():
    index_ctx = [{"name": feed["name"], "link": "/feed/"+str(id)} for id, feed in feeds.items()]
    return render_template('index.html', feeds=index_ctx)
