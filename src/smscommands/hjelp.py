import twilio.twiml

def handle(sms):
	resp = twilio.twiml.Response()
	resp.message(u"<kodeord>: <forklaring>. middag: dagens middag ved HiG. hjelp: denne hjelpeteksten.")
	return resp
