import jinja2
import os
import webapp2
from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = template = jinja_environment.get_template('dab.html')
        html = template.render({})
        self.response.write(html)

	def post(self):
		self.response.write(name_process(self.request.get("name")))

app = webapp2.WSGIApplication([
    ('/', MainHandler) 
], debug=True)
