import os

import src.freebase.FreebaseAPI as freebase

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
	qtopic = freebase.most_likely_topic(query_str)
	topic = freebase.get_topic(qtopic['mid'])
	brief = freebase.topic_summary(topic)
	template = JINJA_ENVIRONMENT.get_template('query.jinja')
	self.response.write(template.render(
		{'topic':qtopic, 'topic_id':qtopic['mid'], 
		'info':topic, 'brief':brief})) 
