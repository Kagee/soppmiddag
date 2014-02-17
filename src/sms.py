import webapp2
import logging
import trh
import twilio.twiml

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

application = webapp2.WSGIApplication([
    ('/sms', MainPage),
], debug=True)
