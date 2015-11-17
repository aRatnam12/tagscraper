#!/usr/bin/env python

from flask import Flask, render_template, request
from lxml import html
import requests
import os

app = Flask(__name__)

@app.route('/')
def renderPage():
  return render_template("index.html")

@app.route('/url/', methods =['POST'])
def scrapeUrl():
  print request.form['url']
  return ''
  # page = requests.get(url)
  # tree = html.fromstring(page.content)
  # print tree
  # return tree

if __name__ == '__main__':
  app.run(debug=True)