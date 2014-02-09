import config
import webapp2
import twilio
from twilio import twiml
from twilio.rest import TwilioRestClient

from twilio.util import RequestValidator

class MainPage(webapp2.RequestHandler):
	def post(self):
		self.response.headers['Content-Type'] = 'text/plain'
		#URL = self.request.url
		url = 'https://soppmiddag.appspot.com/call'
		url = 'http://offle.hild1.no:1593'
		validator = RequestValidator(config.AUTH_TOKEN)
		params = {}
		for name in self.request.arguments():
			params[name] = self.request.get(name);

		#try:
		#	signature = self.request.headers["X-Twilio-Signature"]
		#except KeyError:
		signature = '78tKL7bCCcE4/6LqWbAluYCxYfk='

		if(validator.validate(url, params, signature)):
			self.response.write("Valid\n")
		else:
			self.response.write("Invalid\n")		

application = webapp2.WSGIApplication([
    ('/call', MainPage),
], debug=True)
