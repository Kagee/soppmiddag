import twilio.twiml

def handle(sms):
	resp = twilio.twiml.Response()
	resp.message(u"No dinner for you!")
	return resp
