#! /usr/bin/env python
import lxml.html # parsing html
import re # regexp
import HTMLParser # resolve HTML entities
import urllib2 # downloading webpages
import logging
import config

class SoppParser:
	def __init__(self, url):
		self.url = url

	def verify(self): # Verify that we have five days of dishes
		assert None != \
			(re.search(r"(?i)mandag", lxml.html.tostring(self.plist[0])) and \
			re.search(r"(?i)tirsdag", lxml.html.tostring(self.plist[1])) and \
			re.search(r"(?i)onsdag",  lxml.html.tostring(self.plist[2])) and \
			re.search(r"(?i)torsdag", lxml.html.tostring(self.plist[3])) and \
			re.search(r"(?i)fredag",  lxml.html.tostring(self.plist[4]))), \
			"Missing a day (man-fre) from the list of <p>'\n%s" % \
			("\n".join(lxml.html.tostring(x) for x in self.plist))

	def scrape(self):
		headers = { 'User-Agent': "hildenae-at-gmail.com-soppmiddagscraper" }
		req = urllib2.Request(self.url, headers=headers)
		f = urllib2.urlopen(req)
		self.text = f.read()
		f.close()

	def extract(self):
		root = lxml.html.fromstring(self.text)
		dinnerDiv = root.cssselect("div.module-article.turkis.clearfix")
		assert len(dinnerDiv) > 0, \
			"Found no div matching div.module-article.turkis.clearfix"
		if len(dinnerDiv) != 1:
			logging.warning("Got more than one matching " + \
				"dinnerDiv, this might be a problem.")
		# Get a list of <p> elements inside div
		self.plist = dinnerDiv[0].cssselect("p")
		assert len(self.plist) == 5, "Got only %s <p>'s, expected 5" % len(ps)  
		
	def parse(self):
		h = HTMLParser.HTMLParser() # to resolve HTML entities
		self.menu = {} # Dictionary to hold results
		weekday = 0 # Weekday counter, starting at Mandag=0
		for pel in self.plist:
			# convert from HTML to string as we need to look at the tags as text
			pstr = lxml.html.tostring(pel).strip();
			pstr = h.unescape(pstr) # Resolve HTML entitites to characters
			# FYI: Formatting text using nonbreaking spaces is a STUPID IDEA!
			pstr = re.sub(r"\xa0", ' ', pstr) # Remove nonbreaking spaces
			pstr = re.sub(r"  ", '', pstr) # Remove double spaces

			# Insert a newline before any capital characters 
			# after a <br>|<br />|<br/>. This seems like the best way to 
			# differenciate between <br>s because the name of the dish 
			# was to long, and <br>s to indicate a new dish
			pstr = re.sub(r"<br[ ]*[/]*>[ ]*([A-Z\xC6\xD8\xC5])", r"\n\1", pstr)
			pel = lxml.html.fromstring(pstr); # Convert back to HTML/lxml
			# Get only the text content (removing any tag)
			ptext = pel.text_content()
			lines = ptext.split("\n") # Dishes are separated by newline
			# The day of week and first dish is on the 
			# same line,  but separated by a colon
			day, lines[0] = lines[0].split(":")
			dishes = [line.strip().replace("m/", "med ") for line in lines] # Remove extra whitespace around text.
			logging.debug(day + ":", " eller ".join(dishes))
			self.menu[weekday] = dishes;
			weekday += 1

	def mergeDishes(self, dayNum):
		dishes = self.menu[dayNum]
		numDishes = len(dishes)
		if numDishes == 1:
			merged = dishes[0]
		elif len(dishes) == 2:
			merged = dishes[0] + " eller " + dishes[1]
		else:
			merged = "%s%s%s" % (", ".join(dishes[0:numDishes-1]),", eller ", dishes[numDishes-1])
		return merged.capitalize()

	def plainTextPrint(self):
		days = ["Mandag","Tirsdag","Onsdag","Torsdag","Fredag"]
		lines = []
		for dayNum in range(0,5):
			lines.append("%s;%s\n" % (days[dayNum], self.mergeDishes(dayNum)))
		return "\n".join(lines)

hig = SoppParser(config.SOPP_HIG)
hig = SoppParser("http://localhost:8000/hig.html")
#hil = SoppParser(config.SOPP_HIL)
#hig = SoppParser("http://fuu.bar/soppmiddag")
#hig = SoppParser("http://offle.hild1.no/finnes/ikke")
#hig = SoppParser("http://offle.hild1.no/~hildenae/files/static/IMG_20110622_185758.jpg")
hig.scrape()
hig.extract()
hig.verify()
hig.parse()
print hig.plainTextPrint()
#hig.print()
#hil.print()
