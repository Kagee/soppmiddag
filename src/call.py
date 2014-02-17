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
			logging.info("Call validated: %s" % (self.request.get("CallSid")))
			resp = twilio.twiml.Response()
			resp.say("Denne funksjonen er ikke klar", voice="alice", language="nb-NO")
			self.response.headers['Content-Type'] = 'text/xml'
			self.response.write(str(resp))

application = webapp2.WSGIApplication([
    ('/call', MainPage),
], debug=True)
