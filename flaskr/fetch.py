from flaskr.feed_list import feeds

import feedparser
import logging

def fetch_feed_and_parse(url: str):
    data = feedparser.parse(url)
    if data.get('status', None) != 200:
        logging.error('Cannot fetch feed from', url)
        return None
    return data
