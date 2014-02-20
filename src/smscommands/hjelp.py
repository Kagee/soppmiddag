import twilio.twiml

def handle(sms):
	resp = twilio.twiml.Response()
	resp.message(u"Dette nummeret st\xF8tter ingen kommandoer.")
	return resp
