import webapp2
import logging
import trh
import twilio.twiml
from smscommands import getModule

class SMS(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/xml'
		sms = self.request.get("sms")
		module = getModule(sms)
		if module:
			self.response.write(module.handle(sms))
		else:
			resp = twilio.twiml.Response()
			logging.info("Ukjent kodeord: %s" % (sms))
			resp.message("Ukjent kodeord. Send HJELP for hjelp.")
			self.response.write(str(resp))

class MainPage(trh.TwilioRequestHandler):
	def post(self):
		if not self.valid():
			self.response.set_staus(400, "Request failed validation")
		else:
			logging.info("SMS validated: %s" % (self.request.get("MessageSid")))
			resp = twilio.twiml.Response()
			resp.message("Denne funksjonen er ikke klar")
			self.response.headers['Content-Type'] = 'text/xml'
			self.response.write(str(resp))

application = webapp2.WSGIApplication([
	('/sms', SMS),
], debug=True)
