import json

import urllib
import urllib

api_urls = {'new':'www.reddit.com/new.json'}
def get_new_posts():
	request = urllib2.urlopen(api_urls['new'])
	return json.loads(request.read())
