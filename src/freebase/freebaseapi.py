import json

import urllib2
import urllib

api_key='AIzaSyD8dW6J4JSy2oZw5kPgP69-JCXNMKHlqjE'
api_urls = {'query':'https://www.googleapis.com/freebase/v1/search?'}
def query(string):
	url = encoded_query_url(string)
	request = urllib2.urlopen(url)
	return json.loads(request.read())

def encoded_query_url(query):
	encoded_parameters = urllib.urlencode( \
			{'query': query, 'key' : api_key} \
			)	
	return api_urls['query'] + encoded_parameters
