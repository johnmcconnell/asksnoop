import json
import urllib2
import urllib
import logging

def noun_phrases(query):
	url = "http://localhost:8002/"
	data = urllib.urlencode({'query':query})
	request = urllib2.urlopen(url + "?" + data, data)
	return json.loads(request.read())['topics']

def til():
	url = "http://localhost:8002"
	request = urllib2.urlopen(url)
	return json.loads(request.read())['titles']

