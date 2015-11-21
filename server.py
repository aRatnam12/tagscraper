#!/usr/bin/env python

from flask import Flask, render_template, request
from lxml import html, etree
from flask import jsonify
import urllib2
import requests
import os

app = Flask(__name__)

@app.route('/')
def renderPage():
  return render_template("index.html")

@app.route('/summary/', methods =['POST'])
def scrapeUrl():
  url = request.form['url']
  tags = {}
  page = requests.get(url)
  tree = html.fromstring(page.content)
  getTags(tree, tags)
  return jsonify(tags)

@app.route('/source/',  methods =['POST'])
def getPageSource():
  user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
  headers = { 'User-Agent' : user_agent }
  req = urllib2.Request(request.form['url'], None, headers)
  response = urllib2.urlopen(req)
  page = response.read()
  return page

def getTags(tree, tags):
  for el in tree:
    if el is not etree.Comment and el is not etree.PI:
      tag = str(el.tag)
      if tag in tags:
        tags[tag] += 1
      else:
        tags[tag] = 1
      getTags(el, tags)

if __name__ == '__main__':
  app.run(debug=True)