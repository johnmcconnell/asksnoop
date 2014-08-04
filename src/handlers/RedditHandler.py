import os

import src.freebase.FreebaseAPI as freebase
import src.Validator as validator
import src.localapi as lapi

import jinja2
import webapp2

import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.PackageLoader('assets','views'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Handler(webapp2.RequestHandler):
    def get(self):
	self.response.headers['Content-Type'] = 'text/html'
	queries = lapi.til()
	logging.info(queries)
	results = []
	for query_str in queries:
	    nouns = validator.nouns(query_str)
	    topics = []
	    names = []
	    for noun in nouns:
	        topic,name = validator.topic(noun)
	        topics.append(topic)
	        names.append(name)
	    score = validator.score(query_str, topics)
	    results.append({'title':query_str,'score':score})
	logging.info('RESULTS!!!')
	logging.info(results)
	template = JINJA_ENVIRONMENT.get_template('reddit.jinja')
	self.response.write(template.render({'results':results}))
