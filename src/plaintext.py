import config # config variables
import webapp2 # serving web content via gae
import logging
from SoppParser import SoppParser # parser for sopp.no
from WeekMenu import WeekMenu
class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		hig = SoppParser(config.SOPP_HIG)
		q = WeekMenu.today()
		if q:
			logging.info("Cache hit")
			hig.setMenu(q.menu)
		else:
			logging.info("Cache miss")
			hig.scrape()
			hig.extract()
			hig.extract()
			hig.parse()	
			w = WeekMenu(school='hig', source=hig.getSourceText(), menu=hig.getMenu())
			w.put()
		self.response.write(hig.plainText())

application = webapp2.WSGIApplication([
    ('/plaintext', MainPage),
], debug=True)
