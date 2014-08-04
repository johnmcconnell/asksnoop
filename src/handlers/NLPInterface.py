import os

import webapp2
import jinja2

import src.localapi as lapi

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.PackageLoader('assets','views'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Handler(webapp2.RequestHandler):
    def post(self):
	self.response.headers['Content-Type'] = 'text/html'
	template = JINJA_ENVIRONMENT.get_template('nlp.jinja')
	sentence = self.request.get('sentence')
	phrases = lapi.noun_phrases(sentence)
	self.response.write(template.render({'sentence':sentence,'phrases':phrases}))
