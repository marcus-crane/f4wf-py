import configparser
import re
from base64 import b64encode

from flask import Flask, Response
import requests
from requests.auth import HTTPBasicAuth

def loadConfig():
  config = configparser.ConfigParser()
  config.read('config.ini')
  return config

app = Flask(__name__)

@app.route('/')
def fetchPodcast():
  cfg = loadConfig()
  username = cfg['account']['username']
  password = cfg['account']['password']

  r = requests.get('http://www.f4wradio.com/podcast/100517wo.mp3', auth=HTTPBasicAuth(username, password), stream=True)
  
  def bufferStream():
    for chunk in r.iter_content(chunk_size=128):
      yield chunk
  return Response(bufferStream(), mimetype='audio/mpeg')



# def fetchFeed():
#   r = requests.get('http://www.f4wradio.com/feed/wor.rss')
#   return r.text

# def updateFeed():
#   feed = fetchFeed()
#   pattern = "http://www.f4wradio.com"
#   feedUpdate = re.sub(pattern, "http://f4w.thingsima.de", feed)
