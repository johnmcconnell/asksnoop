import json

import urllib2
import urllib

api_key='AIzaSyD8dW6J4JSy2oZw5kPgP69-JCXNMKHlqjE'
def query(string):
	encoded_parameters = urllib.urlencode( \
			{'query': query, 'key' : api_key} \
			)
	request = urllib2.urlopen('https://www.googleapis.com/freebase/v1/search?' + \
			encoded_parameters)
	return json.loads(request.read())
