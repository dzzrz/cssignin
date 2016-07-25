import jinja2
import os
import webapp2

#from google.appengine.ext import ndb

#class Checkin1(ndb.Model):
#    checkinName = ndb.StringProperty(required=True)

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = template = jinja_environment.get_template('dab.html')
        html = template.render({})
        self.response.write(html)

#class CheckinHandler(webapp2.RequestHandler):
#    def get(self):
#        self.response.write('Check in:<br>')
#        checkin_name_query = Checkin1.query()
#        current_check_in = checkin_name_query.fetch(limit=30)
#        for checkinName in current_check_in:
#            self.response.write(checkinName)
            #self.response.write(' ')
            #self.response.write(checkinName.checkinName)
            #self.response.write('<br>')

app = webapp2.WSGIApplication([
    ('/', MainHandler)#,
    #('/checkin', CheckinHandler),
], debug=True)
