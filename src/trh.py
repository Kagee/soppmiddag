import config
import logging
import webapp2
from twilio.util import RequestValidator

class TwilioRequestHandler(webapp2.RequestHandler):
	"""Wrapper class for webapp2.RequestHandler that 
		implements valid() to validate that a 
		request comes from Twilio"""
	def valid(self):
		url = self.request.url
		logging.info("Validating url:" + url)
		validator = RequestValidator(config.AUTH_TOKEN)
		params = {}
		logging.info("Validating parameters: ")
		for name in self.request.arguments():
			params[name] = self.request.get(name);
			logging.info(name + ': ' + params[name])
		try:
			signature = self.request.headers["X-Twilio-Signature"]
			logging.info('Validating signature: %s' % signature)
		except KeyError:
			 logging.info('Could not find X-Twilio-Signature, validation will fail.')
		return validator.validate(url, params, signature)
