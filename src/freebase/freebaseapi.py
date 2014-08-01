import json
import logging

import urllib2
import urllib

api_key='AIzaSyD8dW6J4JSy2oZw5kPgP69-JCXNMKHlqjE'
api_urls = {'query':'https://www.googleapis.com/freebase/v1/search',
		'topic':'https://www.googleapis.com/freebase/v1/topic'}
def query(string):
	params = {'key':api_key, 'query':string}
	url = encoded_url(api_urls['query'], params)
	return json_from_url(url)

def encoded_url(url,params):
	encoded_parameters = urllib.urlencode(params)	
	return url + '?' + encoded_parameters

def most_likely_topic(string):
	result = query(string)
	if len(result['result']):
		return result['result'][0]
	else:
		return None

def json_from_url(url):
	request = urllib2.urlopen(url)
	return json.loads(request.read())

def get_topic(topic_id):
	params = {'key':api_key, 'filter':'commons'}
	url = encoded_url(api_urls['topic'] + topic_id, params)
	logging.info(url)
	return json_from_url(url)

def topic_summary(topic):
	desc_key = '/common/topic/description'
	if topic['property'][desc_key]:
		return topic['property'][desc_key]['values'][0]['value']
	else:
		return None

def pretty_topic_string(topic):
	buff = ''
	for property in topic['property']:
		buff += '====' + property + '===='
		for value in topic['property'][property]['values']:
			buff += value['text']
	return buff
