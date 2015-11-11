from flask import Flask
from lxml import html
import requests
app = Flask(__name__)

@app.route('/')
def scrapeUrl(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    print tree

if __name__ == '__main__':
    app.run()