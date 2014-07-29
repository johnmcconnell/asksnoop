import os

import webapp2
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.PackageLoader('assets','views'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Handler(webapp2.RequestHandler):
    def get(self):
	self.response.headers['Content-Type'] = 'text/html'
	template = JINJA_ENVIRONMENT.get_template('mainpage.jinja')
	self.response.write(template.render({})) 
