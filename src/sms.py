import webapp2
import logging
import trh
import twilio.twiml
from smscommands import getModule

class sms(trh.TwilioRequestHandler):
	def post(self):
		if not self.valid():
			self.response.set_staus(400, "Request failed validation")
		else:
			logging.info("SMS validated: %s" % (self.request.get("MessageSid")))
			self.response.headers['Content-Type'] = 'text/xml'
			sms = self.request.get("Body")
			module = getModule(sms)
			if module:
				self.response.write(module.handle(sms))
			else:
				resp = twilio.twiml.Response()
				logging.info("Ukjent kodeord: %s" % (sms))
				resp.message("Ukjent kodeord. Send HJELP for hjelp.")
				self.response.write(str(resp))

application = webapp2.WSGIApplication([
	('/sms', sms),
], debug=True)
