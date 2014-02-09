import config
import webapp2
import twilio
from twilio import twiml
from twilio.rest import TwilioRestClient
import logging
from twilio.util import RequestValidator

class MainPage(webapp2.RequestHandler):
	def post(self):
		self.response.headers['Content-Type'] = 'text/plain'
		#URL = self.request.url
		url = 'https://soppmiddag.appspot.com/sms'
		validator = RequestValidator(config.AUTH_TOKEN)
		params = {}
		for name in self.request.arguments():
			params[name] = self.request.get(name);

		logging.info(params)

		try:
			signature = self.request.headers["X-Twilio-Signature"]
			logging.info('X-Twilio-Signature: %s' % signature)
		except KeyError:
			signature = ''
			logging.info('X-Twilio-Signature: Missing')

		if (validator.validate(url, params, signature)):
			print "True"
		else:
			print "False"

application = webapp2.WSGIApplication([
    ('/sms', MainPage),
], debug=True)
