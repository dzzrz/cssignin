import jinja2
import os
import webapp2
import datetime
import urllib2
import json
from datetime import datetime
from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class CheckIn(ndb.Model):
    name = ndb.StringProperty()
    location_atm = ndb.StringProperty()
    time_stamp = ndb.DateTimeProperty(auto_now_add=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = template = jinja_environment.get_template('dab.html')
        self.response.out.write(template.render())
    def post(self):
        contactinfo = '83257704342'
        name = self.request.get('name')
        location_atm = self.request.get('location_atm')
        check_in = CheckIn(name=name, location_atm=location_atm)
        check_in.put()
        my_checkins = {"checkin": "<tr><td> + carl + </td></tr> "}
        table_checkin = ""
        check_in_query = CheckIn.query().order(CheckIn.time_stamp).filter(CheckIn.time_stamp >= datetime.now().replace( hour=0 ))
        check_ins = check_in_query.fetch(limit=30)
        check_ins.append(check_in)
        for check_in in check_ins:
            table_checkin = table_checkin + "<tr><td>" + check_in.name + "<td>" + str(contactinfo) + "<td>" + check_in.location_atm + "<td>" + str(check_in.time_stamp) + "</td></tr>"
        my_checkins = {"checkin": table_checkin}
        if CheckIn.name is "Brenda":
            print contactinfo[0]
        else:
            print contactinfo[1]
        template = jinja_environment.get_template('display.html')
        self.response.out.write(template.render(my_checkins))

class MenuHandlerHome(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('dab.html')
        self.response.out.write(template.render())

class MenuHandlerSignIn(webapp2.RequestHandler):
    def get(self):
        contactinfo = '83257704342'
        my_checkins = {"checkin": "<tr><td> + carl + </td></tr> "}
        table_checkin = ""
        check_in_query = CheckIn.query().order(CheckIn.time_stamp).filter(CheckIn.time_stamp >= datetime.now().replace( hour=0 ))
        check_ins = check_in_query.fetch(limit=30)
        for check_in in check_ins:
            table_checkin = table_checkin + "<tr><td>" + check_in.name + "<td>" + str(contactinfo) + "<td>" + check_in.location_atm + "<td>" + str(check_in.time_stamp) + "</td></tr>"
        my_checkins = {"checkin": table_checkin}
        if CheckIn.name is "Brenda":
            print contactinfo[0]
        else:
            print contactinfo[1]
        template = jinja_environment.get_template('display.html')
        self.response.out.write(template.render(my_checkins))

class MenuHandlerGoogle(webapp2.RequestHandler):
    def get(self):
        template = template = jinja_environment.get_template('google.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/dab.html', MenuHandlerHome),
    ('/display.html', MenuHandlerSignIn),
    ('/google.html', MenuHandlerGoogle)
], debug=True)
