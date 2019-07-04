from flask import Flask, render_template
from flaskr.feed_list import feeds
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/', methods=['GET'])
def index():
    index_ctx = [{"name": feed["name"], "link": "/feed/"+str(id)} for id, feed in feeds.items()]
    return render_template('index.html', feeds=index_ctx)
