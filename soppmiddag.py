import config
import webapp2
import twilio
from twilio import twiml
from twilio.rest import TwilioRestClient

class MainPage(webapp2.RequestHandler):

	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('Hello, Anders Einar!\n')
		self.response.write("The twilio version is: " + twilio.__version__)
		client = TwilioRestClient(config.ACCOUNT_SID, config.AUTH_TOKEN)
		rv = client.sms.messages.create(to="+4791142170", from_="+4759440259", body="Hello Monkey!")
		self.response.write(str(rv))

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
