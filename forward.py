import configparser
import re
from base64 import b64encode

import requests
from requests.auth import HTTPBasicAuth

def loadConfig():
  config = configparser.ConfigParser()
  config.read('config.ini')
  return config

# def fetchFeed():
#   r = requests.get('http://www.f4wradio.com/feed/wor.rss')
#   return r.text

# def updateFeed():
#   feed = fetchFeed()
#   pattern = "http://www.f4wradio.com"
#   feedUpdate = re.sub(pattern, "http://f4w.thingsima.de", feed)

def generateStream(id):
  cfg = loadConfig()
  username = cfg['account']['username']
  password = cfg['account']['password']

  r = requests.get(f'http://www.f4wradio.com/podcast/{id}.mp3', auth=HTTPBasicAuth(username, password), stream=True)
  with open(f'{id}.mp3', 'wb') as podcast:
    for chunk in r.iter_content(chunk_size=128):
      podcast.write(chunk)

generateStream("100917wo")
