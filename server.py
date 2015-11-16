from flask import Flask, render_template
from lxml import html
import requests
app = Flask(__name__)

@app.route('/')
def renderPage():
  return render_template("index.html")

@app.route('/webpage')
def scrapeUrl(url):
  page = requests.get(url)
  tree = html.fromstring(page.content)
  print tree

if __name__ == '__main__':
  app.run()