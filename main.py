
import jinja2
import os
import webapp2
import datetime
import urllib2
import json
import time
import logging
from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class CheckIn(ndb.Model):
    name = ndb.StringProperty(required=True)
    location_atm = ndb.StringProperty(required=True)
    date_stamp = ndb.DateProperty(auto_now_add=True, required=True)
    time_stamp = ndb.TimeProperty(auto_now_add=True, required=True)

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
        now = datetime.datetime.fromtimestamp(time.time())
        day = datetime.date(year=now.year, month=now.month, day=now.day)
        check_in_query = CheckIn.query().order(CheckIn.date_stamp).filter(CheckIn.date_stamp == day)
        check_ins = check_in_query.fetch(limit=30)
        check_ins.append(check_in)
        for check_in in check_ins:
            boston_hour = check_in.time_stamp.hour-4
            minutes = check_in.time_stamp.minute
            if minutes < 10:
                zero = "0"
            else:
                zero = ""
            if boston_hour >= 13:
                am_pm = "PM"
                boston_hour=boston_hour-12
            elif boston_hour == 12:
                am_pm = "PM"
            else:
                am_pm = "AM"
            table_checkin = table_checkin + "<tr><td>" + check_in.name + "<td>" + check_in.location_atm + "<td>" + str(boston_hour) + ":" + str(zero) + str(minutes) + " "+ am_pm +"</td></tr>"
        my_checkins = {"checkin": table_checkin}
        template = jinja_environment.get_template('display.html')
        self.response.out.write(template.render(my_checkins))


class MenuHandlerHome(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('dab.html')
        self.response.out.write(template.render())


class MenuHandlerSignIn(webapp2.RequestHandler):
    def get(self):
        name = self.request.get('name')
        location_atm = self.request.get('location_atm')
        check_in = CheckIn(name=name, location_atm=location_atm)
        check_in.put()
        table_checkin = ""
        check_in_query = CheckIn.query().order(CheckIn.time_stamp)
        now = datetime.datetime.fromtimestamp(time.time())
        day = datetime.date(year=now.year, month=now.month, day=now.day)
        check_in_query = CheckIn.query().order(CheckIn.date_stamp).filter(CheckIn.date_stamp == day)
        check_ins = check_in_query.fetch(limit=30)
        for check_in in check_ins:
            boston_hour = check_in.time_stamp.hour-4
            minutes = check_in.time_stamp.minute
            if minutes < 10:
                zero = "0"
            else:
                zero = ""
            if boston_hour >= 13:
                am_pm = "PM"
                boston_hour=boston_hour-12
            elif boston_hour == 12:
                am_pm = "PM"
            else:
                am_pm = "AM"
            if check_in.name != "":
                table_checkin = table_checkin + "<tr><td>" + check_in.name + "<td>" + check_in.location_atm + "<td>" + str(boston_hour) + ":" + str(zero) + str(minutes) + " "+ am_pm +"</td></tr>"
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
