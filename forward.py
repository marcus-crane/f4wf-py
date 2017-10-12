import configparser
import re
from base64 import b64encode

from flask import Flask, Response
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

def loadConfig():
  config = configparser.ConfigParser()
  config.read('config.ini')
  return config

def cfg(key, option):
  config = loadConfig()
  return config[key][option] 

def fetchFeed():
  r = requests.get('http://www.f4wradio.com/feed/wor.rss')
  return r.text

@app.route('/')
def index():
  return Response("Visit <a href='/wor.rss'>wor.rss</a>", mimetype="text/html")

@app.route('/wor.rss')
def updateFeedURLs():
  feed = fetchFeed()
  domain = cfg('server', 'domain')
  origin = "http://www.f4wradio.com"

  updatedFeed = re.sub(origin, domain, feed)
  return Response(updatedFeed, mimetype='text/xml')

@app.route('/podcast/<id>.mp3')
def fetchPodcast(id):
  username = cfg('account', 'username')
  password = cfg('account', 'password')
  url = 'http://www.f4wradio.com/podcast/{0}.mp3'.format(id)

  r = requests.get(url, auth=HTTPBasicAuth(username, password), stream=True)

  def bufferStream():
    for chunk in r.iter_content(chunk_size=128):
      yield chunk
  return Response(bufferStream(), mimetype='audio/mpeg')

if __name__ == "__main__":
  app.run(host='0.0.0.0')
