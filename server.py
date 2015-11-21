#!/usr/bin/env python

from flask import Flask, render_template, request
from lxml import html
from flask import jsonify
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
  print(tags)
  return jsonify(tags)
  # for el in tree:
  #   print el.tag
  #   for el2 in el:
  #       print el2.tag
  # return ''
  # return tree

@app.route('/source',  methods =['POST'])
def getPageSource():
  return ''

def getTags(tree, tags):
  for el in tree:
    tag = el.tag
    if tag in tags:
      tags[tag] += 1
    else:
      tags[tag] = 1
    getTags(el, tags)

if __name__ == '__main__':
  app.run(debug=True)