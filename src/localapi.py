import json
import urllib2
import urllib

def noun_phrase(query):
	url = "http://localhost:8002/?" + urllib.urlencode({'query':query})
	request = urllib2.urlopen(url)
	return request.read()
