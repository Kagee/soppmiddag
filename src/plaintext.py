import config # config variables
import webapp2 # serving web content via gae
import lxml.html # parsing html
import scraper

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		root = lxml.html.fromstring(scraper.scrape(config.SOPP_URL, "Sopp-Middag-Scraper-hildenae-at-gmail-com"))
		table = scraper.extractTable(root)
		ctable = scraper.cleanup(table)
		d = scraper.tableToDict(ctable);
		self.response.write(scraper.plainText(d, ';'));

application = webapp2.WSGIApplication([
    ('/plaintext', MainPage),
], debug=True)
