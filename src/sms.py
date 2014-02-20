import webapp2
import logging
import trh
import twilio.twiml
from modsms import getModule

class MainPage(trh.TwilioRequestHandler):
	def post(self):
		fromTwilio = self.valid()
		if not fromTwilio:
			self.response.set_staus(400, "Request failed validation")
		else:
			logging.info("SMS validated: %s" % (self.request.get("MessageSid")))
			resp = twilio.twiml.Response()
			resp.message("Denne funksjonen er ikke klar")
			self.response.headers['Content-Type'] = 'text/xml'
			self.response.write(str(resp))

class TestSMS(webapp2.RequestHandler):
	def get(self):
		#self.response.headers['Content-Type'] = 'text/xml'
		#resp = twilio.twiml.Response()
		sms = self.request.get("sms")
		module = getModule(sms)
		if module:
			self.response.write("SMS: <%s>" % (sms))
		else:
			print sms
			print module
			self.response.headers['Content-Type'] = 'text/xml'
			resp = twilio.twiml.Response()
			resp.message(u"Ukjent kodeord. Send HJELP for hjelp")
			self.response.write(str(resp))

application = webapp2.WSGIApplication([
    ('/sms', TestSMS),
], debug=True)
