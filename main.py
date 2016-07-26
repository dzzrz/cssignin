import jinja2
import os
import webapp2
from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class CheckIn(ndb.Model):
    name = ndb.StringProperty()
    location_atm = ndb.StringProperty()
    time_stamp = ndb.TimeProperty(auto_now_add=True)
    date_stamp = ndb.DateProperty(auto_now_add=True)

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

class CheckInHandler(webapp2.RequestHandler, ndb.Model):
    def get(self):
        self.response.write('Check in:<br>')
        check_in_query = CheckIn.query().order(CheckIn.time_stamp)
        check_ins = check_in_query.fetch()
        for check_in in check_ins:
            self.response.write("<br>" + check_in.name + "<br>" + " - " + check_in.location_atm + "<br>" + str(check_in.time_stamp) + " " + str(check_in.date_stamp))
            
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/checkin', CheckInHandler),
], debug=True)
