import jinja2
import os
import webapp2
import urllib2
import json

from datetime import datetime

from google.appengine.ext import ndb

class CheckIn(ndb.Model):
    name = ndb.StringProperty()
    location_atm = ndb.StringProperty()
    time_stamp = ndb.DateTimeProperty(auto_now_add=True)
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = template = jinja_environment.get_template('dab.html')
        self.response.out.write(template.render())
    def post(self):
            name = self.request.get('name')
            location_atm = self.request.get('location_atm')
            check_in = CheckIn(name=name, location_atm=location_atm)
            check_in.put()
            self.redirect('/checkin')

class CheckInHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Check in:<br>')
        check_in_query = CheckIn.query().order(CheckIn.time_stamp).filter(CheckIn.time_stamp >= datetime.now().replace( hour=0 ))
        check_ins = check_in_query.fetch()
        for check_in in check_ins:
            self.response.write("<br>" + check_in.name + "<br>" + " - " + check_in.location_atm + "<br>" + str(check_in.time_stamp))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/checkin', CheckInHandler),
], debug=True)
