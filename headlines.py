import feedparser

from flask import Flask


app = Flask(__name__)

RSS_FEEDS = {'sott': "https://www.sott.net/xml_engine/signs_rss",
             'bbc': "http://feeds.bbci.co.uk/news/rss.xml",
             'cnn': "http://rss.cnn.com/rss/edition.rss"}


@app.route("/")
@app.route("/<publication>")
def get_news(publication="sott"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return """<html>
        <body>
            <h1> Headlines </h1>
            <b>{0}</b> <br/>
            <i>{1}</i> <br/>
            <p>{2}</p> <br/>
        </body>
    </html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))


if __name__ == '__main__':
    app.run(port=5001, debug=True)
