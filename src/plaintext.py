import config # config variables
import webapp2 # serving web content via gae
from SoppParser import SoppParser # parser for sopp.no

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		hig = SoppParser(config.SOPP_HIG)
		hig.scrape()
		hig.extract()
		hig.verify()
		hig.parse()
		self.response.write(hig.plainText());

application = webapp2.WSGIApplication([
    ('/plaintext', MainPage),
], debug=True)
