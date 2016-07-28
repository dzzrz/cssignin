
import jinja2
import os
import webapp2
import datetime
import urllib2
import json
import logging
import time
import logging
from google.appengine.ext import ndb
from datetime import datetime
import urllib2
import json

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class CheckIn(ndb.Model):
    name = ndb.StringProperty()
    location_atm = ndb.StringProperty(default="unknown")
    time_stamp = ndb.TimeProperty(auto_now_add=True)
    date_stamp = ndb.DateProperty(auto_now_add=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = template = jinja_environment.get_template('dab.html')
        self.response.out.write(template.render())
    def post(self):
        name = self.request.get('name')
        name_query = CheckIn.query().filter(CheckIn.name == name)
        for result in name_query.fetch():
            result.key.delete()
        location_atm = self.request.get('location_atm')
        check_in = CheckIn(name=name, location_atm=location_atm)
        check_in.put()
        table_checkin = ""
        check_in_query = CheckIn.query().order(CheckIn.date_stamp).filter(CheckIn.date_stamp >= datetime.today())
        check_ins = check_in_query.fetch(limit=30)
        check_ins.append(check_in)
        for check_in in check_ins:
            table_checkin = table_checkin + "<tr><td>" + check_in.name + "<td>" + check_in.location_atm + "<td>" + str(check_in.time_stamp)[11:16] + "</td></tr>"
        my_checkins = {"checkin": table_checkin}
        template = jinja_environment.get_template('display.html')
        self.response.out.write(template.render(my_checkins))


class MenuHandlerHome(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('dab.html')
        self.response.out.write(template.render())

class MenuHandlerSignIn(webapp2.RequestHandler):
    def get(self):
        table_checkin = ""
        check_in_query = CheckIn.query().order(CheckIn.date_stamp).filter(CheckIn.date_stamp >= datetime.today())
        check_ins = check_in_query.fetch(limit=30)
        for check_in in check_ins:
            table_checkin = table_checkin + "<tr><td>" + check_in.name + "<td>" + check_in.location_atm + "<td>" + str(check_in.time_stamp)[11:16] + "</td></tr>"
        my_checkins = {"checkin": table_checkin}
        template = jinja_environment.get_template('display.html')
        self.response.out.write(template.render(my_checkins))

class MenuHandlerGoogle(webapp2.RequestHandler):
    def get(self):
        template = template = jinja_environment.get_template('google.html')
        self.response.out.write(template.render())

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = template = jinja_environment.get_template('about.html')
        self.response.out.write(template.render())

class CalendarHandler(webapp2.RequestHandler):
    def get(self):
        template = template = jinja_environment.get_template('calendar.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/dab.html', MenuHandlerHome),
    ('/display.html', MenuHandlerSignIn),
    ('/google.html', MenuHandlerGoogle),
    ('/about.html', AboutHandler),
    ('/calendar.html', CalendarHandler)
], debug=True)
