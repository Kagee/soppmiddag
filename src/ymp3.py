import twilio.twiml

def handle(sms):
	resp = twilio.twiml.Response()
	resp.message(u"Youtube rules!")
	return resp
