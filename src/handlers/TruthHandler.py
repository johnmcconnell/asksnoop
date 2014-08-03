import os

import src.freebase.FreebaseAPI as freebase
import src.Validator as validator

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.PackageLoader('assets','views'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Handler(webapp2.RequestHandler):
    def post(self):
	self.response.headers['Content-Type'] = 'text/html'
	query_str = self.request.get('query')
	noun = validator.noun(query_str)
	topic,name = validator.topic(noun)
	score = validator.score(query_str,topic)
	template = JINJA_ENVIRONMENT.get_template('truth.jinja')
	self.response.write(template.render(
		{'query':query_str, 'topic':name, 
			'score':score, 'noun':noun}))

