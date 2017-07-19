import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

RSS_FEEDS = {'sott': "https://www.sott.net/xml_engine/signs_rss",
             'bbc': "http://feeds.bbci.co.uk/news/rss.xml",
             'cnn': "http://rss.cnn.com/rss/edition.rss"}


@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = "sott"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])


if __name__ == '__main__':
    app.run(port=5001, debug=True)
