import config
import twilio
from twilio import twiml
from twilio.rest import TwilioRestClient
from twilio.util import RequestValidator


URL='http://offle.hild1.no:1593'
SIGNATURE='RFlEYnWUKr8N00lDWjAm8lq4Hd4='

params = {
	'AccountSid'='AC3157d24ac5ef896cb85d9b5f450f9651',
	'ApiVersion'='2010-04-01',
	'Body'='Body',
	
}

MessageSid=SMcbe8f85a9cdfe48163de70384efaf5c0
FromState=AR
ToState=CT
SmsSid=SMcbe8f85a9cdfe48163de70384efaf5c0
To=+4759440259
ToCountry=US
FromCountry=US
SmsMessageSid=SMcbe8f85a9cdfe48163de70384efaf5c0
SmsStatus=received
NumMedia=0
From=+4791142170

   validator = RequestValidator(config.AUTH_TOKEN)
        params = {}
        for name in self.request.arguments():
            params[name] = self.request.get(name);

        #try:
        #   signature = self.request.headers["X-Twilio-Signature"]
        #except KeyError:
        signature = '78tKL7bCCcE4/6LqWbAluYCxYfk='

        if(validator.validate(url, params, signature)):
            self.response.write("Valid\n")
        else:
            self.response.write("Invalid\n")


